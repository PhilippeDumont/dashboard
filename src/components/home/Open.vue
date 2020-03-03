<template>
    <v-container>

        <!--SHOW CARDS FOR EVERY PROJECT CREATED-->
        <v-row align="center" class="row-select">
            <span><h1 class="title">Open a project</h1></span>
            <v-spacer></v-spacer>
            <span>
                <v-text-field
                    label="Search a project"
                ></v-text-field>
            </span>
            <span>
                <v-tooltip right>
                    <template v-slot:activator="{ on }">
                        <v-btn icon id="sortProj" v-on="on">
                            <v-icon v-if="ascending">mdi-sort-ascending</v-icon>
                            <v-icon v-else>mdi-sort-descending</v-icon>
                        </v-btn>
                    </template>
                    <span>Sort projects</span>
                </v-tooltip>
            </span>
        </v-row>

        <v-row>
            <v-col v-for="project in getListProjects" v-bind:key="project.id">
                <v-card class="card" width="160" height="300">
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
                                <v-btn icon @click="openDialogDelete(project.id)" v-on="on">
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

        <!-- modal update -->
        <modal-update :isOpen="isDialogUpdate" :idProject="idProject" @closeUpdateDialog="closeUpdateDialog()"></modal-update>

        <modal-delete :isOpen="isDialogDelete" :idProject="idProject" @closeDeleteDialog="closeDeleteDialog()"></modal-delete>

        <!-- SNACKBAR TO SHOW THE SUCCESS OF THE DELETE OR UPDATE OR RENAME-->
        <SnackBar></SnackBar>



    </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { sendRequest } from '@/utils.js';

import ModalDelete from '@/components/home/modals/ModalDelete.vue';
import ModalUpdate from '@/components/home/modals/ModalUpdate.vue';
import SnackBar from '@/components/utils/SnackBar.vue';

export default {
    name: 'Open',
    components: {
        ModalDelete,
        ModalUpdate,
        SnackBar
    },
    data: () => ({
        idProject: null,
        project: null,
        isDialogUpdate: false,
        isDialogDelete: false,
        isProjectDeleted: false,
        isProjectUpdated: false,
        ascending: false,
        wantToRename: false,
        newProjectName: ""
    }),
    computed: {
        ...mapGetters([
            'getListProjects'
        ])
    },
    methods: {
        ...mapActions([
            'setCurrentProject',
            'deleteProject',
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
            console.log(this.newProjectName)
            console.log(project.id)
            sendRequest('api-python', 'rename_project', project.id, this.newProjectName).then((arg) =>{
                console.log(arg)
                console.log("pass")
                this.newProjectName = ""
            }).catch((e) =>{
                console.log(e)
            })
            project.setIsRename(false)
        },
        // clickDeleteProject() {
        //     this.loadingDelete = true;
        //     sendRequest('api-python', 'delete_project_by_id', this.project.id).then((arg) =>{
        //         console.log(arg)
        //         this.deleteProject(this.project)
        //         this.loadingDelete = false;
        //         this.isDialogDelete = false;
        //         this.isProjectDeleted = true;
        //     }).catch((e) => {
        //         console.log(e)
        //     })
        // },


        openDialogUpdate(idProject) {
            this.idProject = idProject
            this.isDialogUpdate = true
        },
        closeUpdateDialog() {
            this.isDialogUpdate = false
            this.isProjectUpdated = true
        },
        
        
        openDialogDelete(idProject){
            this.idProject = idProject
            this.isDialogDelete = true
        },
        closeDeleteDialog(){
            this.isDialogDelete = false
            this.isProjectDeleted = true
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
