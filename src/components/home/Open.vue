<template>
    <v-container>

        <!--SHOW CARDS FOR EVERY PROJECT CREATED-->
        <v-row>
            <v-col>
                <h1 class="title">Open a project</h1>
            </v-col>
        </v-row>

        <v-row>
            <v-col v-for="project in projects" v-bind:key="project">
                <v-card class="card" width="150" height="250">
                    <v-img :src="require('../../assets/graph.svg')" height="150" width="150"></v-img>
                    <v-card-text>{{project}}</v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>

export default {
  name: 'Open',
  data: () => ({
      //projects examples to test the projects cards
      projects: ['Projet Slack 2018, un texte un peu trop long', 'Projet Elium 2019', 'Project 2', 'Project'],
      cards: [
        { title: 'Projet Slack 2018', src: require('../../assets/graph.svg'), flex: 6 },
        { title: 'Projet Elium 2019', src: '../../assets/logo.png', flex: 6 },
        { title: 'Project 2', src: '../../assets/logo.png', flex: 6 },
        { title: 'Project', src: '../../assets/logo.png', flex: 6 }
      ]
  })
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
