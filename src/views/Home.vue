<template>
  <div class="home">
    <v-container class="grey lighten-5">
      <v-row no-gutters>

        <v-col cols="8">
          <v-row>
            <create></create>
          </v-row>
          <v-row>
            <open></open>
          </v-row>
        </v-col>

        <v-col cols="4">
          <explanation></explanation>
        </v-col>

      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Create from '@/components/home/Create.vue'
import Open from '@/components/home/Open.vue'
import Explanation from '@/components/home/Explanation.vue'

export default {
  name: 'Home',
  components: {
    Create,
    Open,
    Explanation
  }
}
</script>
