<template>
  <div>
      <!-- <v-container>
          <v-row>
              <v-col>
                  <h1>Open a project</h1>
              </v-col>
          </v-row>

             list with sheetes
          <v-row justify="space-around">
              <v-col v-for="project in projects" v-bind:key="project">
                  <v-sheet
                  class="mx-auto"
                  height="100"
                  width="100"
                  elevation="6"
                  ></v-sheet>
                  {{project}}
              </v-col>
          </v-row>

          <v-row justify="center">
            <v-col v-for="project in projects" v-bind:key="project">
                <v-card>
                    <v-img src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"></v-img>
                    <v-img src="../../assets/logo.png" height="150" width="150"></v-img>
                    <v-card-text>{{project}}</v-card-text>
                </v-card>
            </v-col>
          </v-row>
      </v-container> -->

      <v-container>
          <v-row>
              <v-col>
                  <h1>Open a project</h1>
              </v-col>
          </v-row>
          <v-row dense>
            <v-col v-for="project in projects" v-bind:key="project">
                <v-card width="150" height="250">
                    <v-img :src="require('../../assets/graph.svg')" height="150" width="150"></v-img>
                    <v-card-text>{{project}}</v-card-text>
                </v-card>
            </v-col>
          </v-row>
      </v-container>

      <!-- <hr/>

      <v-container fluid>
          <v-row dense>
              <v-col
              v-for="card in cards"
              :key="card.title">
                <v-card>
                    <v-img
                    :src="card.src"
                    class="white--text align-end"
                    height="200px"></v-img>
                    <v-cardv-text="card.title"></v-cardv-text="card.title">
                </v-card>
              </v-col>
          </v-row>
      </v-container> -->
  </div>
</template>

<script>

export default {
  name: 'Open',
  components: {
    
  },
  data: () => ({
      projects: ['Projet Slack 2018, un texte un peu trop long', 'Projet Elium 2019', 'Project 2', 'Project'],
      cards: [
        { title: 'Projet Slack 2018', src: require('../../assets/graph.svg'), flex: 6 },
        { title: 'Projet Elium 2019', src: '../../assets/logo.png', flex: 6 },
        { title: 'Project 2', src: '../../assets/logo.png', flex: 6 },
        { title: 'Project', src: '../../assets/logo.png', flex: 6 },
      ],
  })
}
</script>
