<template>
  <v-app>
          <SideBar />
          <router-view></router-view>
  </v-app>
</template>

<script>
    import SideBar from '@/components/SideBar';
    export default {
      name: 'App',

      components: {
        SideBar,
      },

      data: () => ({
        //
      }),
    };
</script>
