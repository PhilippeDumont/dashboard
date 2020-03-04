<template>
  <svg @wheel="wheelLeftRight" :width="graphLocalWidth" :height="height" ref="_svg"
      :viewBox="'0' + ' 0 ' + graphLocalWidth + ' ' + height">

      <line v-for="(stat, index) in normalizedValue" v-bind:key="index" @mouseover="handleMouseOverBar" @mouseout="handleMouseOutBar"
        :x1="index * barSpace + margin + barPosition" :y1="height" :x2="index * barSpace + margin + barPosition"
        :y2="height - stat" :stroke-width="barStroke" :stroke="barColor" />

      <polygon v-show="overRectangle" :fill="arrowColor" :fill-opacity="arrowOpacity" :points="'0,10 10,0 10,' + arrowSize + ',0,10'"
        :transform="'translate(' + selectorLeftPosition.x+ ',' + selectorLeftPosition.y + ') scale(1)'" />

      <polygon v-show="overRectangle" :fill="arrowColor" :fill-opacity="arrowOpacity" :points="'0,10 10,0 10,' + arrowSize + ',0,10'"
        :transform="'translate(' + selectorRightPosition.x+ ',' + selectorRightPosition.y + ') scale(1) rotate(180, ' + 0 + ',' + 10 + ')'" />

      <rect class="draggable" ref="rect" draggable="false" :x="xRect" y="0" :width="rectWidth" :height="height"
        :fill="rectColor" :fill-opacity="rectOpacity" transform="matrix(1 0 0 1 0 0)" @mousedown="handleMouseDown"
        @mouseup="handleMouseUp" @mouseover="handleMouseOver" @mouseout="handleMouseOut" @wheel="wheelZoom" />

      {{ processLoop() }}
    </svg>
</template>

<script>
export default {
 props: ['stat', 'height'],
  data () {
    return {
      width: 0,
      barPosition: 0,
      barSpace: 10,
      barStroke: 3,
      barColor: "#37697E",
      rectWidth: 80,
      canvas: null,
      xRect: 200,
      coords: {
        x: 0,
        y: 0
      },
      positionMouseInRect: 0,
      selectState: false,
      overRectangle: false,
      arrowSize: 20,
      arrowColor: "#000",
      arrowOpacity: 0.5,
      margin: 20,
      viewBoxX: 0,
      viewBoxSpeed: 2,
      isShowInstruction: true,
      overBar: false,
      XlabelBar: 0,
      YlabelBar: 30,
      rectOpacity: 0.3,
      rectColor: "#000",
      labelBarContent: ''
    }
  },
  computed: {
    graphLocalWidth () {
      return this.width + this.margin
    },
    graphGlobalWidth () {
      if (this.stat) {
        return this.stat.length * this.barSpace + this.margin
      } else {
        return 0
      }
    },
    normalizedValue () {
      if (this.stat) {
        let max = Math.max(...this.stat)
        return this.stat.map((x) => {
          let res = (x / max) * this.height
          res = parseInt(res)
          return res
        })
      } else {
        return []
      }
    },
    selectorLeftPosition () {
      return {
        x: this.xRect,
        y: this.height / 2 - this.arrowSize / 2
      }
    },
    selectorRightPosition () {
      return {
        x: this.xRect + this.rectWidth,
        y: this.height / 2 - this.arrowSize / 2
      }
    }
  },
  methods: {
    processLoop () {
      if (this.localPositionRectLeft() <= 0) {
        this.xRect = this.viewBoxX
      }

      if (this.localPositionRectRight() >= this.graphLocalWidth) {
        this.xRect = this.graphLocalWidth - this.rectWidth + this.viewBoxX
      }
    },
    handleMouseDown (e) {
      e.preventDefault()
      document.addEventListener('mousemove', this.handleMouseMove)
      document.addEventListener('mouseup', this.handleMouseUp)
      this.coords = {
        x: e.pageX,
        y: e.pageY
      }
      this.positionMouseInRect = e.pageX - this.$refs._svg.getBoundingClientRect().left - this.xRect + this.viewBoxX
      if (this.isInRange(this.positionMouseInRect, this.rectWidth, 10)) {
        this.selectState = 'right'
      }
      if (this.isInRange(this.positionMouseInRect, 0, 10)) {
        this.selectState = 'left'
      }
    },
    handleMouseUp (e) {
      e.preventDefault()
      this.selectState = false
      this.positionMouseInRect = 0
      document.removeEventListener('mousemove', this.handleMouseMove)
      document.removeEventListener('mouseup', this.handleMouseUp)
      this.coords = {}
      this.$emit('updateTime', this.getSelectedInterval())
    },
    handleMouseMove (e) {
      if (this.selectState === 'right') {
        let xDiff = this.coords.x - e.pageX
        this.coords.x = e.pageX
        this.rectWidth = this.rectWidth - xDiff
        if (this.rectWidth < 10) {
          this.rectWidth = 10
          this.xRect = this.xRect - xDiff
        }
        if (this.globalPositionRectRight() >= this.$refs._svg.getBoundingClientRect().width) {
          this.rectWidth = this.$refs._svg.getBoundingClientRect().width - this.xRect
        }
      }
      if (this.selectState === 'left') {
        let xDiff = this.coords.x - e.pageX
        this.coords.x = e.pageX
        this.xRect = this.xRect - xDiff
        if (this.xRect >= 0) {
          this.rectWidth = this.rectWidth + xDiff
        }
        if (this.rectWidth < 10) {
          this.rectWidth = 10
        }
        if (this.xRect <= 0) {
          this.xRect = 0
        }
      }
      if (e.pageX > this.$refs._svg.getBoundingClientRect().left - (this.positionMouseInRect) && e.pageX < this.$refs._svg.getBoundingClientRect().right + this.positionMouseInRect) {
        const xDiff = this.coords.x - e.pageX
        this.coords.x = e.pageX
        this.xRect = this.xRect - xDiff
        if (this.xRect < 0) {
          this.xRect = 0
        }
      }
    },
    handleMouseOver (e) {
      e.preventDefault()
      this.overRectangle = true
    },
    handleMouseOut (e) {
      e.preventDefault()
      this.overRectangle = false
    },
    wheelZoom (e) {
      e.preventDefault()
      this.barSpace = this.barSpace - this.normalizedSigne(e.deltaY)
      if (this.barSpace <= this.barStroke) {
        this.barSpace = this.barStroke + 1
      }
      if (this.barSpace >= 50) {
        this.barSpace = 50
      }
      this.$emit('updateTime', this.getSelectedInterval())
    },
    normalizedSigne (value) {
      if (value > 0) {
        return 1
      }
      if (value < 0) {
        return -1
      }
      if (value === 0) {
        return 0
      }
    },
    wheelLeftRight (e) {
      e.preventDefault()
      if (!this.overRectangle) {
        this.barPosition = this.barPosition - this.normalizedSigne(e.deltaY) * 20
        if (this.barPosition <= -this.graphGlobalWidth) {
          this.barPosition = -this.graphGlobalWidth
        }
        if (this.barPosition >= this.graphGlobalWidth) {
          this.barPosition = this.graphGlobalWidth
        }
      }
      this.$emit('updateTime', this.getSelectedInterval())
    },
    localPositionRectLeft () {
      return this.xRect - this.viewBoxX
    },
    localPositionRectRight () {
      return this.xRect + this.rectWidth - this.viewBoxX
    },
    globalPositionRectRight () {
      return this.xRect + this.rectWidth
    },
    isInRange (position, center, marge) {
      let res = (position < center + marge && position > center - marge)
      return res
    },
    getSelectedInterval () {
      let left = this.xRect
      let right = this.xRect + this.rectWidth
      let begin = (-this.margin - this.barPosition + left) / this.barSpace
      let end = (-this.margin - this.barPosition + right) / this.barSpace
      begin = parseInt(begin)
      end = parseInt(end)
      begin = (begin < 0) ? 0 : begin
      end = (end > this.stat.length) ? this.value.length : end
      let res = {begin: begin, end: end}
      return res
    },
    handleMouseOverBar (e) {
      e.preventDefault()
      this.XlabelBar = Math.ceil(e.clientX - this.$refs._svg.getBoundingClientRect().left)
      let value = Math.ceil((-this.margin - this.barPosition + this.XlabelBar) / this.barSpace)
      // let date = value
      // this.labelBarContent = moment(date).format('MMMM YYYY')
      this.labelBarContent = value
      this.overBar = true
    },
    handleMouseOutBar (e) {
      e.preventDefault()
      this.overBar = false
    },
    getTimeLineSize() {
      this.width = this.$parent.$el.getBoundingClientRect().width
    }
  },
  mounted() {
    this.$nextTick(function() {
      window.addEventListener('resize', this.getTimeLineSize);
      //Init
      this.getTimeLineSize()
    })
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.getTimeLineSize);
  }
}
</script>

<style scoped>
  draggable {
    z-index: 110px;
    user-drag: none;
    user-select: none;
    -moz-user-select: none;
    -webkit-user-drag: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    cursor: move;
  }

  .debug {
    display: none;
    position: absolute;
    top: 0px;
    left: 70px;
    z-index: 100px;
  }

  @keyframes pulse {
    0% {
      opacity: 0.6;
    }

    100% {
      opacity: 1;
    }
  }

  .button {
    color: #fff;
    text-transform: uppercase;
    margin-left: 40px;
    margin-right: 50px;
    margin-top: 5px;
    background-color: #1AB188;
    text-align: center;
    padding: 5px;
    border: solid 2px rgb(97, 238, 200)
  }

  .svg-text {
    font: italic 30px sans-serif;
    fill: #fff;
  } 
</style>
