<template>
    <v-container>

        <!--SHOW CARDS FOR EVERY PROJECT CREATED-->
        <v-row>
            <v-col>
                <h1 class="title">Open a project</h1>
            </v-col>
        </v-row>

        <v-row>
            <v-col v-for="project in getListProjects" v-bind:key="project.id">
                <v-card class="card" width="150" height="300">
                    <v-img :src="require('@/assets/graph.svg')" height="150" width="150"></v-img>
                    <v-card-text style="overflow-y: auto; height:100px">
                        {{project.name}}
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn icon @click="choseAndOpenProject(project)">
                            <v-icon>mdi-folder-open</v-icon>
                        </v-btn>
                        <v-btn icon @click="openDialogUpdate(project.id)">
                            <v-icon>mdi-file-import</v-icon>
                        </v-btn>
                        <v-btn icon @click="openDialogDelete(project)">
                            <v-icon>mdi-close-circle</v-icon>
                        </v-btn>
                        <v-spacer></v-spacer>
                    </v-card-actions>
                </v-card>

            </v-col>
        </v-row>

        <!-- modal update -->
        <modal :isOpen="dialog" :idProject="idProject" @update="update"></modal>

        <v-dialog v-model="confirmDelete" max-width="600px" persistent>
            <v-card>
                <v-card-title class="justify-center">
                    <svg style="width:45px; height:45px; color: red;" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
                    </svg>
                    <br />
                    <h5>If you delete the project, you will not be able to recover your datas ?</h5>
                </v-card-title>
                <v-card-actions style="font-size: 18px;" class="justify-end">
                    <v-btn @click="closeDialog" class="mx-2 mt-4" :disabled="loadingDelete">Cancel</v-btn>
                    <v-btn class="error mx-2 mt-4" @click="deleteProject()" :disabled="loadingDelete"
                        :loading="loadingDelete">Agree</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

    </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { sendRequest } from '@/utils.js';

import Modal from '@/components/home/update/Modal.vue';

export default {
    name: 'Open',
    components: {
        Modal
    },
    data: () => ({
        dialog: false,
        idProject: null,
        confirmDelete: false,
        loadingDelete: false,
        project: null
    }),
    computed: {
        ...mapGetters([
            'getListProjects'
        ])
    },
    methods: {
        ...mapActions([
            'setCurrentProject',
            'deleteProject'
        ]),
        choseAndOpenProject(project) {
            this.setCurrentProject(project)
            this.$router.push('/Level1')
        },
        deleteProject() {
            this.loadingDelete = true;
            sendRequest('api-python', 'delete_project_by_id', this.project.id).then((arg) =>{
                console.log(arg)
                this.s_deleteProject(this.project)
                this.loadingDelete = false;
                this.confirmDelete = false;
            }).catch((e) => {
                console.log(e)
            })
        },

        openDialogUpdate(idProject) {
            this.idProject = idProject
            this.dialog = true
        },
        update(bool) {
            this.dialog = bool
        },
                    
        openDialogDelete(project){
            this.project = project;
            this.confirmDelete = true;
        },
        closeDialog(){
            this.confirmDelete = false;
        }
    }
}
</script>

<style scoped>
.card {
    box-shadow: 6px 6px 20px 4px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition:0.2s;
}
.card:hover{
    box-shadow: 6px 6px 25px 4px rgba(0, 0, 0, 0.18);
    transform: scale(1.02);
}
</style>
