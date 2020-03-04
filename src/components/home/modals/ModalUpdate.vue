<template>
    <v-container>

        <v-dialog v-model="isOpenInterne" persistent width="500">
            <v-card>
                <v-card-title>
                    Update project
                    <v-spacer></v-spacer>
                    <v-icon @click="close(false)">mdi-close</v-icon>
                </v-card-title>
                <v-divider />
                <v-card-text>
                    <v-col>

                        <!--BUTTON TO IMPORT ITEMS FILE-->
                        <v-row class="justify-center">
                            <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathItemsFile()">
                                <v-icon medium dark>mdi-plus</v-icon>
                                Select ITEMS file
                            </v-btn>
                            <!--ICONS TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <v-icon v-if="isPathItems" color="green">mdi-checkbox-marked-circle</v-icon>
                            <v-icon v-else color="red">mdi-close-circle</v-icon>
                        </v-row>
                        <v-row class="justify-center">
                            <!--FILE TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <span v-if="isPathItems">{{ itemsFile }}</span>
                        </v-row>

                        <!--BUTTON TO IMPORT ACTIVITIES FILE-->
                        <v-row class="justify-center">
                            <v-btn color="blue-grey" class="ma-2 white--text" width="250"
                                @click="getPathActivitiesFile()">
                                <v-icon medium dark>mdi-plus</v-icon>
                                Select ACTIVITIES file
                            </v-btn>
                            <!--ICONS TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <v-icon v-if="isPathActivities" color="green">mdi-checkbox-marked-circle</v-icon>
                            <v-icon v-else color="red">mdi-close-circle</v-icon>
                        </v-row>
                        <v-row class="justify-center">
                            <!--FILE TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <span v-if="isPathActivities">{{ activitiesFile }}</span>
                        </v-row>

                        <!--BUTTON TO CREATE THE PROJECT-->
                        <v-row class="justify-center" style="margin-right: 15px">
                            <!--BUTTON DISABLED IF NO DATA ITEMS AND ACTIVITIES-->

                            <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="clickUpdateProject()"
                                :disabled="!isPathItems || !isPathActivities || loader"
                                :loading="loader">
                                Update
                            </v-btn>
                        </v-row>
                    </v-col>
                </v-card-text>
            </v-card>
        </v-dialog>

    </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { sendRequest, getFileNameOfPath } from '@/utils.js';

export default {
    name: 'ModalUpdate',
    //props: ['isOpen', 'idProject'],
    props: {
        isOpen: {
            type: Boolean,
            default: false
        },
        idProject: {
            type: Number
        }
    },
    data: () => ({
        //path of the items data file
        pathItems: null,
        //name of the items data file
        itemsFile: null,
        //boolean to know if there is a path for items
        isPathItems: null,
        //path of the activities data file
        pathActivities: null,
        //name of the activities data file
        activitiesFile: null,
        //boolean to know if there is a path for activities
        isPathActivities: null,
        //boolean to know if project is updated
        isProjectUpdated: false,
        isOpenInterne: false,
        loader: false
    }),
    // created() {
    //     this.isOpenInterne = this.isOpen
    // },
    computed: {
        ...mapGetters([
            'getAllProjects'
        ])
    },
    methods: {
        ...mapActions([
            'setMsgSnackBar',
            'setSnackBarToShow',
            'setColorSnackBar'
        ]),
        //get the path of the items data file
        getPathItemsFile() {
            sendRequest('open-dialog').then((arg) =>{
                if (arg) {
                    this.pathItems = arg
                    this.itemsFile = getFileNameOfPath(this.pathItems)
                    this.isPathItems = true
                }
            }).catch((e) => {
                console.log(e)
            })
        },
        //get the path of the activities data file
        getPathActivitiesFile() {
            sendRequest('open-dialog').then((arg) =>{
                if (arg) {
                    this.pathActivities = arg
                    this.activitiesFile = getFileNameOfPath(this.pathActivities)
                    this.isPathActivities = true
                }
            }).catch((e) => {
                console.log(e)
            })
        },
        clickUpdateProject() {
            this.loader = true
            sendRequest('api-python', 'update_project_by_id', this.idProject, this.pathActivities, this.pathItems).then(() =>{
                this.close(true)
                this.loader = false
                this.setSnackBarToShow(true)
                this.setMsgSnackBar("Project updated with success")
                this.setColorSnackBar("green")
            }).catch((e) => {
                this.loader = false
                console.log(e)
                this.setSnackBarToShow(true)
                this.setMsgSnackBar("Error: "+e)
                this.setColorSnackBar("red")
            })
            this.loadingUpdate = false
        },
        close(success) {
            this.pathActivities = null
            this.activitiesFile = null
            this.isPathActivities = false
            this.pathItems = null
            this.itemsFile = null
            this.isPathItems = false
            this.$emit('close-update-dialog', success) // bool for success
        }
    },
    watch: {
        isOpen: function(val) {
            this.isOpenInterne = val
        }
    }
}
</script>

<style scoped>
    .custom-loader {
        animation: loader 1s infinite;
        display: flex;
    }
</style>
