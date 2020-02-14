<template>
  <div class="home">
    <v-container fluid>
      <v-row>

        <v-col cols="8">
          <v-row>
            <create></create>
          </v-row>
          <v-divider />
          <v-row>
            <open></open>
          </v-row>
        </v-col>

        <v-col cols="4">
          <explication></explication>
        </v-col>

      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Create from '@/components/home/Create.vue'
import Open from '@/components/home/Open.vue'
import Explication from '@/components/home/Explication.vue'

export default {
  name: 'Home',
  components: {
    Create,
    Open,
    Explication
  }
}
</script>

<style scoped>
  .home {
    margin-left: 100px;
    z-index: 1;
  }
</style>
