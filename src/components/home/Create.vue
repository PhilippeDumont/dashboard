<template>
    <div>
        <v-container>
            <v-row>
                <v-col>
                    <h1>Create your project</h1>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="6">
                    <v-text-field label="Name Project" :rules="rules" hide-details="auto"></v-text-field>
                </v-col>
            </v-row>

            <v-row align="center">
                <v-col cols="7" >What kind of plateform do you use ?</v-col>
                <v-col cols="5">
                    <v-select
                        :items="items"
                        label="Plateform"
                        outlined
                        dense
                        hide-details
                    ></v-select>
                </v-col>
            </v-row>

            <v-row>
                <v-btn
                color="blue-grey"
                class="ma-2 white--text text-left"
                width="250"
                >
                    <!-- <div style="text-align:center"></div> -->
                    <v-icon medium dark>mdi-plus</v-icon>
                    Import ITEMS file
                </v-btn>
            </v-row>

            <v-row>
                <v-btn
                color="blue-grey"
                class="ma-2 white--text"
                width="250"
                >
                    <v-icon medium dark>mdi-plus</v-icon>
                    Import ACTIONS file
                </v-btn>
            </v-row>
        </v-container>
    </div>
</template>

<script>

export default {
  name: 'Create',
  components: {
    
  },
  data: () => ({
      rules: [
        value => !!value || 'Required.',
        value => (value && value.length >= 3) || 'Min 3 characters',
      ],
      items: ['Default', 'Edix', 'Slack']
  })
}
</script>
