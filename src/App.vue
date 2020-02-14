<template>
  <v-app>
    <SideBar />
    <home></home>
  </v-app>
</template>

<script>
    import SideBar from '@/components/SideBar';
    import Home from '@/views/Home.vue'
    export default {
      name: 'App',

      components: {
        SideBar,
        Home
      },

      data: () => ({
        //
      }),
    };
</script>
