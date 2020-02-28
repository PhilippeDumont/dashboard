<template>

<!--DROPDOWN WITH ALL THE PROJECT-->
<!--PROJECT OPEN IS SHOWN-->

<v-row justify="center">
 <div id="selector_projects">
    <v-expansion-panels>
     <v-expansion-panel>    
       <v-expansion-panel-header v-if="currentProject">{{ currentProject.name }}</v-expansion-panel-header>
       <v-expansion-panel-header v-else>Choose a project</v-expansion-panel-header>
       <v-expansion-panel-content>
           <v-row>
            <!-- Project Item -->
             <v-col cols="12"  v-for="(project,index) in listProjects" :key="index">
                 <v-row>
                   <v-col cols="8">
                     <span>{{project.name}}</span>
                   </v-col>
                   <v-col cols="4">
                     <v-btn text icon @click="setCurrentProject(project)">
                       <v-icon>mdi-open-in-app</v-icon>
                     </v-btn>
                   </v-col>
                 </v-row>
            </v-col>
            <!-- ------------ -->
         </v-row>
       </v-expansion-panel-content>
     </v-expansion-panel>
    </v-expansion-panels>
 </div>
</v-row>
</template>


<script>
import { mapState, mapActions } from 'vuex'

export default {
  computed: mapState({
    listProjects: 'listProjects',
    currentProject: 'currentProject'
  }),
  methods: {
      ...mapActions([
       'setCurrentProject'
      ])
  }
}  
</script>

<style scoped>
li {
    list-style: none;
}

li a {
    text-decoration: none;
}

.col {
    align-items: center;
    align-self: baseline;
    padding: 0 20px;
}

#selector_projects{
  width: 200px;
  position: fixed;
  /*TO BE BEFORE EVERYTHING*/
  z-index: 3;
  top: 3px;
}
</style>