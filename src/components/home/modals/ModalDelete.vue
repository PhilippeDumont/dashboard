<template>
    <v-container>

        <v-dialog v-model="isOpenInterne" max-width="600px" persistent>
            <v-card>
                <v-card-title class="justify-center">
                    <svg style="width:45px; height:45px; color: red;" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
                    </svg>
                    <br />
                    <h5>If you delete the project, you will not be able to recover your datas ?</h5>
                </v-card-title>
                <v-card-actions style="font-size: 18px;" class="justify-end">
                    <v-btn @click="close()" class="mx-2 mt-4" :disabled="loadingDelete">Cancel</v-btn>
                    <v-btn class="error mx-2 mt-4" @click="clickDeleteProject()" :disabled="loadingDelete"
                        :loading="loadingDelete">Agree</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

    </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { sendRequest } from '@/utils.js';

export default {
    name: 'ModalDelete',
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
        loadingDelete: false,
        isOpenInterne: false
    }),
    computed: {
        ...mapGetters([
            'getListProjects'
        ])
    },
    methods: {
        ...mapActions([
            'deleteProject'
        ]),
        clickDeleteProject() {
            this.loadingDelete = true;
            sendRequest('api-python', 'delete_project_by_id', this.idProject).then((arg) =>{
                console.log(arg)
                this.deleteProject(this.idProject)
                this.close()
            }).catch((e) => {
                console.log(e)
            })
            this.loadingDelete = false
        },
        close() {
            this.$emit('closeDeleteDialog', false)
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

</style>
