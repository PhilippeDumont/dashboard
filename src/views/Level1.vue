<template>
    <div>
        <v-container fluid>
            <div v-if="getCurrentProject()">
                {{ getCurrentProject().name }}
            </div>
            <div v-else>
                <AlertNoProject/>
            </div>

        </v-container>

    </div>
</template>

<script>

import AlertNoProject from '@/components/utils/AlertNoProject.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
    components: {
      AlertNoProject
    },
    created() {
      this.setExpansionBarVisibility(true)
    },
    methods: {
      ...mapActions([
        'setExpansionBarVisibility',
      ]),
      ...mapGetters([
        'getAllProjectsSortedByDate',
        'getCurrentProject'
      ])
    }
}
</script>

<style scoped>
  .container {
      height: 100%;
  }
</style>
