<template>
  <v-app>
      <v-container id="app-container" fluid>
          <SideBar />
          <SelectProject v-if="getExpansionBarVisibility"></SelectProject>
          <router-view></router-view>
      </v-container>
  </v-app>
</template>
<script>
import SideBar from '@/components/SideBar';
import SelectProject from '@/components/SelectProject';
import { sendRequest } from '@/utils.js';
import { Project } from '@/model/Project.js'
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'App',
    data: () => ({
        projectsList: null
    }),
    components: {
        SideBar,
        SelectProject,
    },
    methods: {
        ...mapActions([
            'setListProjects'
        ])
    },
    // check if the database with the list of projects exists, if this is not the case, create it
    // get the list of projects
    computed: {
       ...mapGetters([
            'getExpansionBarVisibility'
        ])
    },
    // check if the database with the list of projects exists, if this is not the case, create it
    // get the list of projects
    beforeCreate() {
        sendRequest('api-python', 'init_db_projects').then((arg) => {
            console.log("init_db_projects: "+arg)

            sendRequest('api-python', 'get_projects').then((arg) => {

                let listProjects = []

                const obj = JSON.parse(arg)
                obj.forEach(element => {
                    listProjects.push(new Project(element.id, element.name, element.creation_date, element.last_opening_date, element.nb_activities, element.nb_items))
                })

                this.setListProjects(listProjects)

            }).catch((e) => {
                console.log(e)
            })

        }).catch((e) => {
            console.log(e)
        })
    }
};
</script>

<style>
    #app-container {
        margin: 0;
        padding: 0;
        height: 100%;
        width: 100%;
    }

    ::-webkit-scrollbar {
        height: 10px;
        width: 10px;
    }

    ::-webkit-scrollbar-button {
        height: 0px;
        width: 0px;
    }

    ::-webkit-scrollbar-corner {
        background: transparent;
    }

    ::-webkit-scrollbar-thumb {
        background: #2196f3;
        border: 0px none #2196f3;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #2196f3;
        filter: grayscale(50%);
    }

    ::-webkit-scrollbar-thumb:active {
        background: #2196f3;
    }

    ::-webkit-scrollbar-track {
        background: #013F52;
        border: 0px none #013F52;
    }

    ::-webkit-scrollbar-track:hover {
        background: #013F52;
    }

    ::-webkit-scrollbar-track:active {
        background: #013F52;
    }
</style>