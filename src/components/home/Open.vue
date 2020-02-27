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
                    <v-card-text style="overflow-y: auto; height:100px" >
                        {{project.name}}
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn icon>
                            <v-icon>mdi-folder-open</v-icon>
                        </v-btn>
                        <v-btn icon>
                            <v-icon>mdi-file-import</v-icon>
                        </v-btn>
                        <v-btn icon>
                            <v-icon>mdi-close-circle</v-icon>
                        </v-btn>
                        <v-spacer></v-spacer>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Open',
  computed: {
      ...mapGetters([
          'getListProjects'
      ])
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
