<template>
<v-row justify="center">
 <div id="selector_projects">
    <v-expansion-panels>
     <v-expansion-panel>    
       <v-expansion-panel-header>Project 1</v-expansion-panel-header>
       <v-expansion-panel-content>
           <v-row>
            <!-- Project Item -->
             <v-col md="12"  v-for="(project,index) in projects" :key="index">
                 <v-row>
                   <v-col md="8">
                     <span>{{project.title}}</span>
                   </v-col>
                   <v-col md="4">
                     <v-btn text icon>
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
    export default {
        data() {
            // MOCK FOR PROJECTS
            return {
                projects : [
                    { title : "Project 1" },
                    { title : "Project 2" },
                    { title : "Project 3" }
                ] 
            }
        },
        methods:{
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
  z-index: 1000;
  top: 3px;
}
</style>