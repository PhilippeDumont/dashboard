<template>
  <v-app>
          <SideBar />
          <SelectProject></SelectProject>
          <router-view></router-view>
  </v-app>
</template>

<script>
import SideBar from '@/components/SideBar';
import SelectProject from '@/components/SelectProject';
export default {
    name: 'App',
    components: {
        SideBar,
        SelectProject,
    }
};
</script>

<style>
    ::-webkit-scrollbar {
        height: 10px;
        width: 10px;
    }

    ::-webkit-scrollbar-button {
        height: 0px;
        width: 0px;
    }

    ::-webkit-scrollbar-corner {
        background: transparent;
    }

    ::-webkit-scrollbar-thumb {
        background: blueviolet;
        border: 0px none blueviolet;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: blueviolet;
        filter: grayscale(50%);
    }

    ::-webkit-scrollbar-thumb:active {
        background: blueviolet;
    }

    ::-webkit-scrollbar-track {
        background: #013F52;
        border: 0px none #013F52;
    }

    ::-webkit-scrollbar-track:hover {
        background: #013F52;
    }

    ::-webkit-scrollbar-track:active {
        background: #013F52;
    }

    
</style>