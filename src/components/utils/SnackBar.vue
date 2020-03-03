<template>
    <div>
        <v-snackbar v-model="getSnackBarToShow" :color="getColorSnackBar">
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
            'setSnackBarToShow',
            'setColorSnackBar'
        ]),
        setBooleanShowSnackBar(){
            this.setSnackBarToShow(false)
        }
    }
}
</script>

<style scoped>

</style>