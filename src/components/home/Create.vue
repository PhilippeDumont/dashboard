<template>
    <v-container>
        <v-row>
            <v-col>
                <h1 class="title">Create your project</h1>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="6">
                <v-text-field label="Name Project" :rules="rules" hide-details="auto"></v-text-field>
            </v-col>
        </v-row>

        <v-row align="center">
            <span>What kind of plateform do you use ?</span>
            <span>
                <v-select :items="items" label="Plateform" outlined dense hide-details></v-select>
            </span>
        </v-row>

        <v-row>
            <v-col>
                <v-btn color="blue-grey" class="ma-2 white--text text-left" width="250">
                    <v-icon medium dark>mdi-plus</v-icon>
                    Import ITEMS file
                </v-btn>
                <v-icon color="green">mdi-checkbox-marked-circle</v-icon>
                <v-icon color="red">mdi-cancel</v-icon>
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <v-btn color="blue-grey" class="ma-2 white--text" width="250">
                    <v-icon medium dark>mdi-plus</v-icon>
                    Import ACTIONS file
                </v-btn>
                <v-icon color="green">mdi-checkbox-marked-circle</v-icon>
                <v-icon color="red">mdi-cancel</v-icon>
            </v-col>
        </v-row>

        <v-row>
            <v-col>
                <v-btn class="ma-2 white--text" :color="colorBtnCreate" width="250" :loading="loading"
                    @click="loader = 'loading'">
                    Create
                    <template v-slot:loader>
                        <span>Loading...</span>
                    </template>
                </v-btn>
                <v-icon color="green">mdi-checkbox-marked-circle</v-icon>
                <v-icon color="red">mdi-cancel</v-icon>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
  name: 'Create',
  components: {
    
  },
  data: () => ({
      loader: null,
      loading: false,
      colorBtnCreate: 'blue-grey',
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
        
        value => (value && value.length <= 40) || 'Max 40 characters'
      ],
      items: ['Default', 'Edx', 'Slack']
  }),
  watch: {
      loader () {
        const l = this.loader;
        this[l] = !this[l];

        this.colorBtnCreate = 'error';

        setTimeout(() => {
            this[l] = false;
            this.colorBtnCreate = 'success';
        }, 3000);

        this.loader = null;
      },
    }
}
</script>

<style scoped>
  span {
      margin: 10px
  }

  .custom-loader {
      animation: loader 1s infinite;
      display: flex;
  }

  @-moz-keyframes loader {
      from {
          transform: rotate(0);
      }

      to {
          transform: rotate(360deg);
      }
  }

  @-webkit-keyframes loader {
      from {
          transform: rotate(0);
      }

      to {
          transform: rotate(360deg);
      }
  }

  @-o-keyframes loader {
      from {
          transform: rotate(0);
      }

      to {
          transform: rotate(360deg);
      }
  }

  @keyframes loader {
      from {
          transform: rotate(0);
      }

      to {
          transform: rotate(360deg);
      }
  }
</style>