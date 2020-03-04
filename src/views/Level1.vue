<template>
 <div id="level-one-container">
            <div v-if="currentProject">
              <v-row>
                <v-col cols="8">
                 <!-- TIMELINE GRAPH-->
                 <v-card id="timeline-container">
                  
                   <v-row>
                     <v-col cols="4">
                       <v-card-title id="title_timeline">Which period ?</v-card-title>
                     </v-col>

                     <v-col cols="2">
                       <div class="filter_box">
                        <span class="title_date_filter">Start</span>
                        <v-select
                         label="Month"
                        >
                        </v-select>
                       </div>
                     </v-col>

                      <v-col cols="2">
                       <div class="title_date_filter">
                        <span style="visibility: hidden;">Start</span>
                        <v-select
                         label="Year"
                        >
                        </v-select>
                       </div>
                     </v-col>

                      <v-col cols="2">
                       <div class="title_date_filter">
                        <span>End</span>
                        <v-select
                        label="Month"
                        >
                        </v-select>
                       </div>
                      </v-col>

                      <v-col cols="2">
                       <div class="title_date_filter">
                        <span style="visibility: hidden;">End</span>
                        <v-select
                        label="Year"
                        >
                        </v-select>
                       </div>
                     </v-col>
                     
                   </v-row>
                  <TimeLine :stat="[5, 10, 3, 50]" :width="200" :height="50"></TimeLine>
                 </v-card>
                </v-col>
              </v-row>
            </div>
            <div v-else>
                <AlertNoProject/>
            </div>
 </div>
</template>

<script>

import AlertNoProject from '@/components/utils/AlertNoProject.vue'
import { mapState, mapActions } from 'vuex'
import TimeLine from '@/components/Level1/TimeLine.vue'

export default {
    components: {
    AlertNoProject,
    TimeLine
  },
    computed: mapState({
        currentProject: 'currentProject'
    }),

    created() {
      this.setExpansionBarVisibility(true)
    },
    methods: {
      ...mapActions([
        'setExpansionBarVisibility',
      ]),
      ...mapGetters([
        'getAllProjectsSortedByDate',
        'getCurrentProject'
      ])
    }
}
</script>

<style scoped>
  #title_timeline {
    font-size: 14px;
  }
  #title_date_filter {
    font-size: 8px;
  }
  #level-one-container {
    margin-left: 100px;
    margin-top: 100px;
  }
  #timeline-container {
    margin-left: 20px;
  }
  .filter_box {
    display: flex;
    flex-direction: column;
  }
  .container {
      height: 100%;
  }
</style>
