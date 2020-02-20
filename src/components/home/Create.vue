<template>

    <!--FORM TO CREATE A PROJECT-->

    <v-container>
        <v-row>
            <v-col>
                <h1 class="title">Create your project</h1>
            </v-col>
        </v-row>

        <v-form ref="form">

            <!--INPUT FOR PROJECT_NAME-->
            <v-row>
                <v-col cols="6">
                    <v-text-field label="Name Project" v-model="projectName"
                        :rules="rules" 
                        required></v-text-field>
                </v-col>
            </v-row>

            <!--DROPDOWN TO CHOOSE THE PLATFORM WHERE THE DATA COMES FROM-->
            <v-row align="center" class="row-select">
                <span>What kind of plateform do you use ?</span>
                <span>
                    <v-select label="Plateform" v-model="plateform" :items="items" 
                        :rules="[v => !!v || 'Item is required']"
                        outlined
                        dense
                        hide-details="auto"
                        required></v-select>
                </span>
            </v-row>


            <!--BUTTON TO IMPORT ITEMS FILE-->
            <v-row>
                <v-col>
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathItemsFile()">
                        <v-icon medium dark>mdi-plus</v-icon>
                        Import ITEMS file
                    </v-btn>
                    <!--ICONS TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                    <v-icon v-if="isPathItems" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-if="!isPathItems" color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>

            <!--BUTTON TO IMPORT ACTIVITIES FILE-->
            <v-row>
                <v-col>
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathActivitiesFile()">
                        <v-icon medium dark>mdi-plus</v-icon>
                        Import ACTIVITIES file
                    </v-btn>
                    <!--ICONS TO SHOW IF DATA FILE CHOOSEN OR NOT-->
                    <v-icon v-if="isPathActivities" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-if="!isPathActivities" color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>

            <!--BUTTON TO CREATE THE PROJECT-->
            <v-row>
                <v-col>
                    <!--BUTTON DISABLED IF NO DATA ITEMS AND ACTIVITIES-->
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250"
                        @click="initDB()"
                        :disabled="!isPathItems || !isPathActivities">
                        Create
                    </v-btn>
                    <!--ICONS TO SHOW IF PROJECT IS CREATED OR NOT-->
                    <v-icon v-if="isProjectCreated" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-if="!isProjectCreated" color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>
        </v-form>

    </v-container>
</template>

<script>
import { sendRequest } from '@/utils.js';
export default {
    name: 'Create',
    components: {

    },
    data: () => ({
        //project_name init
        projectName: '',
        //constraints for form elements
        rules: [
            value => !!value || 'Required.',
            value => (value && value.length >= 1) || 'Min 3 characters',
            value => (value && value.length <= 40) || 'Max 40 characters'
        ],
        //plateform init
        plateform: null,
        //content of plateform dropdown
        items: ['Default', 'Edx', 'Slack'],
        //path of the items data file
        pathItems: null,
        //boolean to know if there is a path for items
        isPathItems: null,
        //path of the activities data file
        pathActivities: null,
        //boolean to know if there is a path for activities
        isPathActivities: null,
        //boolean to know if project is created
        isProjectCreated: false,
    }),
    methods: {
        //reset form elements
        resetForm() {
            this.$refs.form.reset();
            this.isPathItems = false;
            this.isPathActivities = false;
        },
        //verify if form is valid
        isFormValid() {
            return this.$refs.form.validate() && this.isPathItems && this.isPathActivities;
        },
        //init the database
        initDB() {
            if (this.$refs.form.validate()) {
                console.log(this.projectName);
                sendRequest('api-python', 'init_db', this.projectName).then((arg) => {
                    console.log(arg);
                    this.importDatas();
                }).catch((e) => {
                    console.log("ERROR INIT DB")
                    console.log(e);
                })
            }
        },
        //import the datas in the database
        importDatas() {
            this.pathItems = this.pathItems.replace(/\\/g, '/');      
            sendRequest('api-python', 'import_item_file', [this.projectName, this.pathItems]).then((arg) => {
                console.log("Frontend-arg: "+arg);
                
                sendRequest('api-python', 'import_activity_file', [this.projectName, this.pathActivities]).then((arg) => {
                    console.log("arg-activities "+arg);
                }).catch((e) => {
                    console.log(e);
                })

                this.isProjectCreated = true;
                this.resetForm();
            }).catch((e) => {
                console.log(e);
            });
        },
        //get the path of the items data file
        getPathItemsFile() {
            sendRequest('import-path').then((arg) =>{
                if (arg) {
                    this.pathItems = arg;
                    this.isPathItems = true;
                }
                else {
                    this.pathItems = null;
                    this.isPathItems = false;
                }
            }).catch((e) => {
                console.log(e);
            });
        },
        //get the path of the activities data file
        getPathActivitiesFile() {
            sendRequest('import-path').then((arg) =>{
                if (arg) {
                    this.pathActivities = arg;
                    this.isPathActivities = true;
                }
                else {
                    this.pathActivities = null;
                    this.isPathActivities = false;
                }
            }).catch((e) => {
                console.log(e)
            });
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
    height: 100px;
}

span {
    margin: 10px;
}

@keyframes loader {
    from {
        transform: rotate(0);
    }

    to {
        transform: rotate(360deg);
    }
}

@-moz-keyframes loader {
    from {
        transform: rotate(0);
    }

    to {
        transform: rotate(360deg);
    }
}

@-o-keyframes loader {
    from {
        transform: rotate(0);
    }

    to {
        transform: rotate(360deg);
    }
}

@-webkit-keyframes loader {
    from {
        transform: rotate(0);
    }

    to {
        transform: rotate(360deg);
    }
}
</style>
