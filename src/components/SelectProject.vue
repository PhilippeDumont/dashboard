<template>

<!--DROPDOWN WITH ALL THE PROJECT-->
<!--PROJECT OPEN IS SHOWN-->

<v-row justify="center">
 <div id="selector_projects">
    <v-expansion-panels>
     <v-expansion-panel>    
       <v-expansion-panel-header v-if="getCurrentProject()">{{ getCurrentProject().name }}</v-expansion-panel-header>
       <v-expansion-panel-header v-else>None current project</v-expansion-panel-header>
       <v-expansion-panel-content>
           <v-row>
            <!-- Project Item -->
             <v-col cols="12" v-for="(project,index) in getAllProjectsSortedByDate().slice(0, 3)" :key="index">
                 <v-row>
                   <v-col cols="8">
                     <span>{{project.name}}</span>
                   </v-col>
                   <v-col cols="4">
                     <v-tooltip right>
                            <template v-slot:activator="{ on }">
                                <v-btn text icon @click="setCurrentProject(project)" v-on="on">
                                  <v-icon>mdi-folder-open</v-icon>
                                </v-btn>
                            </template>
                            <span>Open project</span>
                        </v-tooltip>
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
import { mapActions, mapGetters } from 'vuex'

export default {
  methods: {
      ...mapActions([
       'setCurrentProject'
      ]),
      ...mapGetters([
        'getAllProjectsSortedByDate',
        'getCurrentProject'
      ])
  },

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
  width: 220px;
  position: fixed;
  /*TO BE BEFORE EVERYTHING*/
  z-index: 3;
  top: 35px;
}
</style>