<template>
    <div>
        <v-container fluid>
            <div v-if="currentProject">
                {{ currentProject.name }}
            </div>
            <div v-else>
                <AlertNoProject/>
            </div>

        </v-container>
    </div>
</template>

<script>
import AlertNoProject from '@/components/utils/AlertNoProject.vue'
import { mapState } from 'vuex'

export default {
    components: {
    AlertNoProject
  },
    computed: mapState({
        currentProject: 'currentProject'
    }),
}
</script>

<style scoped>

</style>