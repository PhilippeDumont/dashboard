<template>
  <v-app>
      <v-container>
          <SideBar />
      </v-container>
  </v-app>
</template>

<script>
    import SideBar from './components/SideBar';
    export default {
  name: 'App',

  components: {
    SideBar
  },

  data: () => ({
    //
  }),
};
</script>
