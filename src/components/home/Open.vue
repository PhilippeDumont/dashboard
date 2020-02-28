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
                        <v-btn icon @click="openDialog(project.id)">
                            <v-icon>mdi-file-import</v-icon>
                        </v-btn>
                        <v-btn icon @click="clickDeleteProject(project)">
                            <v-icon>mdi-close-circle</v-icon>
                        </v-btn>
                        <v-spacer></v-spacer>
                    </v-card-actions>
                </v-card>

            </v-col>
        </v-row>

        
        <modal :isOpen="dialog" :idProject="idProject" @update="update"></modal>

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
        idProject: null
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
        clickDeleteProject(project) {
            sendRequest('api-python', 'delete_project_by_id', project.id).then((arg) =>{
                console.log(arg)
                this.deleteProject(project)
            }).catch((e) => {
                console.log(e)
            })
        },
        openDialog(idProject) {
            this.idProject = idProject
            this.dialog = true
        },
        update(bool) {
            this.dialog = bool
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
    transform: scale(1.05);
}

.card:active{
    box-shadow: 6px 6px 18px 2px rgba(0, 0, 0, 0.23);
    transform: scale(0.97);
}
</style>
