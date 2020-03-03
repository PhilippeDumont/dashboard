<template>
    <div>
        <v-snackbar v-model="isOpenInterne" :color="getColorSnackBar">
            {{getMsgSnackBar}}
            <v-btn color="white" text @click="setBooleanShowSnackBar">
                Close
            </v-btn>
        </v-snackbar>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
    data(){
        return{
            isOpenInterne: false
        }
    },
    computed: {
        ...mapGetters([
            'getMsgSnackBar',
            'getSnackBarToShow',
            'getColorSnackBar'
        ]),
    },
    methods: {
        ...mapActions([
            'setSnackBarToShow'
        ]),
        setBooleanShowSnackBar(){
            this.isOpenInterne = false
        }
    },
    watch: {
        getSnackBarToShow: function(val) {
            if (val)
                this.isOpenInterne = val
        },
        isOpenInterne: function(val) {
            if (!val)
                this.setSnackBarToShow(false)
        }
    }
}
</script>

<style scoped>

</style>