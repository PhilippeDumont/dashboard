<template>

    <!--FORM TO CREATE A PROJECT-->

    <v-container>
        <v-row>
            <v-col>
                <h1 class="title">Create your project</h1>
            </v-col>
        </v-row>

        <v-form ref="form" v-model="valid">

            <!--INPUT FOR PROJECT_NAME-->
            <v-row>
                <v-col cols="6">
                    <v-text-field label="Name Project" v-model="projectName" :rules="rules" required></v-text-field>
                </v-col>
            </v-row>

            <!--DROPDOWN TO CHOOSE THE PLATFORM WHERE THE DATA COMES FROM-->
            <v-row align="center" class="row-select">
                <span>What kind of plateform do you use ?</span>
                <span>
                    <v-select label="Plateform" v-model="plateform" :items="items"
                        :rules="[v => !!v || 'Item is required']" outlined dense hide-details="auto" required>
                    </v-select>
                </span>
            </v-row>


            <!--BUTTON TO IMPORT ITEMS FILE-->
            <v-row>
                <v-col>
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathItemsFile()">
                        <v-icon medium dark>mdi-plus</v-icon>
                        Import ITEMS file
                    </v-btn>
                    <!--ICONS AND FILE TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                    <span v-if="isPathItems">{{ itemsFile }}</span>
                    <v-icon v-if="isPathItems" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-else color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>

            <!--BUTTON TO IMPORT ACTIVITIES FILE-->
            <v-row>
                <v-col>
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathActivitiesFile()">
                        <v-icon medium dark>mdi-plus</v-icon>
                        Import ACTIVITIES file
                    </v-btn>
                    <!--ICONS AND FILE TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                    <span v-if="isPathActivities">{{ activitiesFile }}</span>
                    <v-icon v-if="isPathActivities" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-else color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>

            <!--BUTTON TO CREATE THE PROJECT-->
            <v-row>
                <v-col>
                    <!--BUTTON DISABLED IF NO DATA ITEMS AND ACTIVITIES-->

                    <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="createProject()"
                        :disabled="!isPathItems || !isPathActivities || !valid">
                        Create
                    </v-btn>
                    <!--ICONS TO SHOW IF PROJECT IS CREATED OR NOT-->
                    <v-icon v-if="isProjectCreated" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-else color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>

        </v-form>

        <!-- SNACKBAR TO SHOW THE SUCCESS OF THE CREATION -->
        <v-snackbar v-model="isProjectCreated">
            Project created with success !
            <v-btn color="pink" text @click="isProjectCreated = false">
                Close
            </v-btn>
        </v-snackbar>

    </v-container>
</template>

<script>
import { sendRequest, getFileNameOfPath } from '@/utils.js';
import { mapActions } from 'vuex';
import { Project } from '@/model/Project.js'

export default {
    name: 'Create',
    data: () => ({
        valid: true,
        //project_name init
        projectName: '',
        //constraints for form elements
        rules: [
            value => !!value || 'Required.',
            value => (value && value.length >= 3) || 'Min 3 characters',
            value => (value && value.length <= 40) || 'Max 40 characters'
        ],
        //plateform init
        plateform: null,
        //content of plateform dropdown
        items: ['Default', 'Edx', 'Slack'],
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
        //boolean to know if project is created
        isProjectCreated: false,
    }),
    methods: {
        ...mapActions([
            'addProject'
        ]),
        //reset form elements
        resetForm() {
            this.$refs.form.reset()
            this.isPathItems = false
            this.isPathActivities = false
        },
        //verify if form is valid
        isFormValid() {
            return this.$refs.form.validate() && this.isPathItems && this.isPathActivities
        },
        //create new project
        async createProject() {
            try {
                let idProject = parseInt(await sendRequest('api-python', 'create_new_project', this.projectName))
                console.log('id: ' + idProject)
                await this.importItems(idProject)
                await this.importActivities(idProject)
                await this.addCurrentProjectInStore(idProject)

                this.isProjectCreated = true
                this.resetForm()

                this.$router.push('/Level1')
            }
            catch(error) {
                console.log(error)
            }
        },
        // import items from a CSV file for the project with the specified id
        async importItems(idProject) {
            await sendRequest('api-python', 'import_item_file', idProject, this.pathItems)
        },
        // import activities from a CSV file for the project with the specified id
        async importActivities(idProject) {
            await sendRequest('api-python', 'import_activity_file', idProject, this.pathActivities)
        },
        // add the new project to the store by getting the datas after his creation
        async addCurrentProjectInStore(idProject) {
            // get the project's datas
            let p = await sendRequest('api-python', 'get_project_by_id', idProject)

            // add the project into the store
            p = JSON.parse(p)
            console.log(p)
            let newProject = new Project(p.id, p.name, p.creation_date, p.last_opening_date, p.nb_activities, p.nb_items)
            this.addProject(newProject)
        },
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
        }
    }
}
</script>

<style scoped>

.custom-loader {
    animation: loader 1s infinite;
    display: flex;
}

.row-select {
    height: 94px;
}

span {
    margin: 10px;
}
</style>
