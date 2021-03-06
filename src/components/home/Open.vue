<template>
    <v-container>

        <!--SHOW CARDS FOR EVERY PROJECT CREATED-->
        <v-row align="center" class="row-select">
            <span><h1 class="title">Open a project</h1></span>
            <v-spacer></v-spacer>
            <span>
                <v-text-field
                    label="Search a project"
                    v-model="search"
                ></v-text-field>
            </span>
            <span>
                <v-tooltip right>
                    <template v-slot:activator="{ on }">
                        <v-btn icon id="sortProj" v-on="on" @click="changeSortType('date-open')">
                            <v-icon :color="colorDate">mdi-calendar</v-icon>
                        </v-btn>
                    </template>
                    <span>Sort projects by use</span>
                </v-tooltip>
            </span>
            <span>
                <v-tooltip right>
                    <template v-slot:activator="{ on }">
                        <v-btn icon id="sortProj" v-on="on">
                            <v-icon v-if="isAscending" :color="colorAlpha" @click="changeSortType('alpha-asc')">mdi-sort-ascending</v-icon>
                            <v-icon v-else :color="colorAlpha" @click="changeSortType('alpha-desc')">mdi-sort-descending</v-icon>
                        </v-btn>
                    </template>
                    <span>Sort {{ isAscending ? "A-Z" : "Z-A" }}</span>
                </v-tooltip>
            </span>
        </v-row>

        <v-row>
            <v-col v-for="project in getAllProjects(this.sortType, this.search)" v-bind:key="project.id">
                <v-card class="card" width="150" height="300">
                    <v-img :src="require('@/assets/graph.svg')" height="150" width="150"></v-img>
                    <v-card-text style="overflow-y: auto; height:100px">
                        <span v-if="!project.isRename">{{project.name}}</span>
                        <v-text-field
                            v-else
                            v-model="newProjectName"
                            label="New name"
                            v-on:keyup.enter="updateProjectName(project)"
                        ></v-text-field>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-tooltip top>
                            <template v-slot:activator="{ on }">
                                <v-btn icon @click="choseAndOpenProject(project)" v-on="on">
                                    <v-icon>mdi-folder-open</v-icon>
                                </v-btn>
                            </template>
                            <span>Open project</span>
                        </v-tooltip>
                        <v-tooltip top>
                            <template v-slot:activator="{ on }">
                                <v-btn icon @click="activeTextFieldToRename(project)" v-on="on">
                                    <v-icon>mdi-pencil</v-icon>
                                </v-btn>
                            </template>
                            <span>Rename project</span>
                        </v-tooltip>
                        <v-tooltip top>
                            <template v-slot:activator="{ on }">
                                <v-btn icon @click="openDialogUpdate(project.id)" v-on="on">
                                    <v-icon>mdi-publish</v-icon>
                                </v-btn>
                            </template>
                            <span>Reimport data</span>
                        </v-tooltip>
                        <v-tooltip top>
                            <template v-slot:activator="{ on }">
                                <v-btn icon @click="openDialogDelete(project)" v-on="on">
                                    <v-icon>mdi-delete</v-icon>
                                </v-btn>
                            </template>
                            <span>Delete project</span>
                        </v-tooltip>
                        <v-spacer></v-spacer>
                    </v-card-actions>
                </v-card>

            </v-col>
        </v-row>

        <modal-update :isOpen="isDialogUpdate" :idProject="idProject" @close-update-dialog="closeUpdateDialog"></modal-update>

        <modal-delete :isOpen="isDialogDelete" :project="project" @close-delete-dialog="closeDeleteDialog"></modal-delete>

    </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { sendRequest } from '@/utils.js';

import ModalDelete from '@/components/home/modals/ModalDelete.vue';
import ModalUpdate from '@/components/home/modals/ModalUpdate.vue';


export default {
    name: 'Open',
    components: {
        ModalDelete,
        ModalUpdate
    },
    data: () => ({
        idProject: null,
        project: null,
        isDialogUpdate: false,
        isDialogDelete: false,
        isProjectDeleted: false,
        isProjectUpdated: false,
        sortType: "date-open",
        isAscending: true,
        search: "",
        colorAlpha: null,
        colorDate: "blue",
        ascending: false,
        wantToRename: false,
        newProjectName: ""
    }),
    computed: {
        ...mapGetters([
            'getAllProjects'
        ])
    },
    methods: {
        ...mapActions([
            'setCurrentProject',
            'deleteProject',
            'setNameProject',
            'setMsgSnackBar',
            'setSnackBarToShow',
            'setColorSnackBar'
        ]),
        choseAndOpenProject(project) {
            this.setCurrentProject(project)
            sendRequest('api-python', 'update_last_opening_date_project', project.id).then((arg) =>{
                console.log(arg)
            }).catch((e) =>{
                console.log(e)
            })
            this.$router.push('/Level1')
        },

        activeTextFieldToRename(project){
            project.setIsRename(true)
            this.newProjectName = project.name
        },
        updateProjectName(project){
            sendRequest('api-python', 'rename_project', project.id, this.newProjectName).then((arg) =>{
                let valueToRename = {'project': project, 'nameToRename': this.newProjectName}
                this.setNameProject(valueToRename)
                console.log(arg)
                this.newProjectName = ""
                this.setSnackBarToShow(true)
                this.setMsgSnackBar("Project renamed with success")
                this.setColorSnackBar("green")
            }).catch((e) =>{
                console.log(e)
                this.setSnackBarToShow(true)
                this.setMsgSnackBar("Error: "+e)
                this.setColorSnackBar("red")
            })
            project.setIsRename(false)
        },

        changeSortType(sortType) {
            this.sortType = sortType

            if (sortType.includes("alpha")) {
                this.colorAlpha = "blue"
                this.colorDate = null
                this.isAscending = !this.isAscending
            }
            else {
                this.colorAlpha = null
                this.colorDate = "blue"
            }

        },

        openDialogUpdate(idProject) {
            this.idProject = idProject
            this.isDialogUpdate = true
        },
        closeUpdateDialog(bool) {
            this.idProject = null
            this.isDialogUpdate = false
            this.isProjectUpdated = bool
        },
        
        
        openDialogDelete(project){
            this.project = project
            this.isDialogDelete = true
        },
        closeDeleteDialog(bool){
            this.project = null
            this.isDialogDelete = false
            this.isProjectDeleted = bool
        }
    }
}
</script>

<style scoped>
.card {
    box-shadow: 6px 6px 20px 4px rgba(0, 0, 0, 0.2);
    transition:0.2s;
}
.card:hover{
    box-shadow: 6px 6px 25px 4px rgba(0, 0, 0, 0.18);
    transform: scale(1.02);
}

.row-select {
    height: auto;
    width: auto;
}

#sortProj{
     transition: transform 0.5s;
     transform: rotate(360deg)
}

#sortProj:active{
    transform: rotate(0deg);
    transition: 0s;
}

span{
margin: 10px;
}

.v-text-field{
    right: 0;
}
</style>
