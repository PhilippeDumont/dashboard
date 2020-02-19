<template>
    <v-container>
        <v-row>
            <v-col>
                <h1 class="title">Create your project</h1>
            </v-col>
        </v-row>

        <v-form ref="form">
            <v-row>
                <v-col cols="6">
                    <v-text-field label="Name Project" v-model="projectName"
                        :rules="rules" 
                        required></v-text-field>
                </v-col>
            </v-row>

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

            <v-row>
                <v-col>
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathItemsFile()">
                        <v-icon medium dark>mdi-plus</v-icon>
                        Import ITEMS file
                    </v-btn>
                    <v-icon v-if="isPathItems" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-if="!isPathItems" color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>

            <v-row>
                <v-col>
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250" @click="getPathActivitiesFile()">
                        <v-icon medium dark>mdi-plus</v-icon>
                        Import ACTIVITIES file
                    </v-btn>
                    <v-icon v-if="isPathActivities" color="green">mdi-checkbox-marked-circle</v-icon>
                    <v-icon v-if="!isPathActivities" color="red">mdi-close-circle</v-icon>
                </v-col>
            </v-row>

            <v-row>
                <v-col>
                    <v-btn color="blue-grey" class="ma-2 white--text" width="250"
                        @click="initDB()">
                        Create
                    </v-btn>
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
        projectName: '',
        rules: [
            value => !!value || 'Required.',
            value => (value && value.length >= 3) || 'Min 3 characters',
            value => (value && value.length <= 40) || 'Max 40 characters'
        ],
        plateform: null,
        items: ['Default', 'Edx', 'Slack'],
        pathItems: null,
        isPathItems: null,
        pathActivities: null,
        isPathActivities: null,
        isProjectCreated: false,
        mydata: []
    }),
    methods: {
        resetForm() {
            this.$refs.form.reset();
        },
        isFormValid() {
            return this.$refs.form.validate() && this.isPathItems && this.isPathActivities;
        },
        initDB() {
            if (this.$refs.form.validate()) {
                console.log(this.projectName);
                sendRequest('api-python', 'init_db', this.projectName).then((arg) => {
                    console.log(arg);
                    this.importDatas();
                    this.isProjectCreated = true;
                }).catch((e) => {
                    console.log(e);
                })
            }
        },
        importDatas() {
            sendRequest('api-python', 'import_item_file', [this.projectName, this.pathItems]).then((arg) => {
                console.log(arg);
                
                this.resetForm();
            }).catch((e) => {
                console.log(e);
            });
        },
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
                console.log(e);
            });
        }
    }
}
</script>

<style scoped>
span {
    margin: 10px;
}

.row-select {
    height: 100px;
}

.custom-loader {
    animation: loader 1s infinite;
    display: flex;
}

@-moz-keyframes loader {
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

@-o-keyframes loader {
    from {
        transform: rotate(0);
    }

    to {
        transform: rotate(360deg);
    }
}

@keyframes loader {
    from {
        transform: rotate(0);
    }

    to {
        transform: rotate(360deg);
    }
}
</style>
