<template>
    <v-container>

        <v-dialog v-model="isOpen" persistent width="500">
            <v-card>
                <v-card-title>
                    Update project
                    <v-spacer></v-spacer>
                    <v-icon @click="close()">mdi-close</v-icon>
                </v-card-title>
                <v-divider />
                <v-card-text>
                    <v-col>

                        <!--BUTTON TO IMPORT ITEMS FILE-->
                        <v-row>
                            <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathItemsFile()">
                                <v-icon medium dark>mdi-plus</v-icon>
                                Select ITEMS file
                            </v-btn>
                            <!--ICONS TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <v-icon v-if="isPathItems" color="green">mdi-checkbox-marked-circle</v-icon>
                            <v-icon v-else color="red">mdi-close-circle</v-icon>
                        </v-row>
                        <v-row>
                            <!--FILE TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <span v-if="isPathItems">{{ itemsFile }}</span>
                        </v-row>

                        <!--BUTTON TO IMPORT ACTIVITIES FILE-->
                        <v-row>
                            <v-btn color="blue-grey" class="ma-2 white--text" width="250"
                                @click="getPathActivitiesFile()">
                                <v-icon medium dark>mdi-plus</v-icon>
                                Select ACTIVITIES file
                            </v-btn>
                            <!--ICONS TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <v-icon v-if="isPathActivities" color="green">mdi-checkbox-marked-circle</v-icon>
                            <v-icon v-else color="red">mdi-close-circle</v-icon>
                        </v-row>
                        <v-row>
                            <!--FILE TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                            <span v-if="isPathActivities">{{ activitiesFile }}</span>
                        </v-row>

                        <!--BUTTON TO CREATE THE PROJECT-->
                        <v-row>
                            <!--BUTTON DISABLED IF NO DATA ITEMS AND ACTIVITIES-->

                            <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="updateProject()"
                                :disabled="!isPathItems || !isPathActivities">
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
import { mapGetters } from 'vuex'
import { sendRequest, getFileNameOfPath } from '@/utils.js';

export default {
    name: 'Open',
    props: ['isOpen', 'idProject'],
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
        isProjectUpdated: false
    }),
    computed: {
        ...mapGetters([
            'getListProjects'
        ])
    },
    methods: {
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
        updateProject() {
            sendRequest('api-python', 'update_project_by_id', this.idProject, this.pathActivities, this.pathItems).then(() =>{
                this.close()
            }).catch((e) => {
                console.log(e)
            })
        },
        close() {
            this.pathActivities = null
            this.activitiesFile = null
            this.isPathActivities = false
            this.pathItems = null
            this.itemsFile = null
            this.isPathItems = false
            this.$emit('update', false)
        }
    }
}
</script>

<style scoped>

</style>
