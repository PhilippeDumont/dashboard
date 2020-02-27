<template>
  <v-app>
      <v-container>
          <SideBar />
          <SelectProject></SelectProject>
          <router-view></router-view>
      </v-container>
  </v-app>
</template>

<script>
import SideBar from '@/components/SideBar';
import SelectProject from '@/components/SelectProject';
import { sendRequest } from '@/utils.js';
import { Project } from '@/model/Project.js'

export default {
    name: 'App',
    data: () => ({
        projectsList: null
    }),
    components: {
        SideBar,
        SelectProject,
    },
    // check if the database with the list of projects exists, if this is not the case, create it
    // get the list of projects
    created() {
        sendRequest('api-python', 'init_db_projects').then((arg) => {
            console.log("init_db_projects: "+arg);

            sendRequest('api-python', 'get_projects').then((arg) => {

                let listProjects = []

                const obj = JSON.parse(arg)
                obj.forEach(element => {
                    listProjects.push(new Project(element.id, element.name, element.creation_date, element.last_opening_date, element.nb_activities, element.nb_items))
                });

                this.$store.commit('SET_LIST_PROJECTS', listProjects)

            }).catch((e) => {
                console.log(e);
            });

        }).catch((e) => {
            console.log(e);
        });

        
    }
};
</script>

<style>
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
        background: blueviolet;
        border: 0px none blueviolet;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: blueviolet;
        filter: grayscale(50%);
    }

    ::-webkit-scrollbar-thumb:active {
        background: blueviolet;
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