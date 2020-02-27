<template>
<div id="settings">
  <v-container fluid>
     <v-row>
      <v-col cols="12">
          <h3 id="version"></h3>
      </v-col>
      <v-col cols="12">
          <v-row>
              <v-col cols="4">
                  <v-btn :rounded="true" color="primary" :loading="loadingUpdate" @click="checkForUpdate()">Check for update</v-btn>
              </v-col>
              <v-col cols="4">
                  <v-btn color="primary" v-if="updateAvailable" @click="restartApp()">Restart App</v-btn>
              </v-col>
               <v-col cols="4">
                    <p id="message"></p>
              </v-col>
          </v-row>
      </v-col>
     </v-row>
  </v-container>
</div>
</template>

<script>

import { ipcRenderer } from 'electron'
export default {
    data: () => ({
        loadingUpdate: false,
        updateAvailable: false,
        version: null,
        message: null,
    }),
    mounted: function() {
     this.version = document.getElementById("version");
     this.message = document.getElementById("message");
      ipcRenderer.send('app_version');

      ipcRenderer.on('app_version', (event, arg) => {
       ipcRenderer.removeAllListeners('app_version');
       this.version.innerText = 'Version ' + arg.version;
      });
    },
    methods: {
        checkForUpdate() {
            ipcRenderer.send('check_for_update');
            this.loadingUpdate = true;
             // Start Download
             ipcRenderer.on('update_available', () => {
                 ipcRenderer.removeAllListeners('update_available');
                 this.message.innerText = 'A new update is available. Downloading now...';
                 this.updateAvailable = true;
                 console.log("update_available")
             });

             // Stop Download
             ipcRenderer.on('update_not_available', () => {
                 ipcRenderer.removeAllListeners('update_not_available');
                 this.message.innerText = 'Not update.';
                 this.updateAvailable = false;
                 this.loadingUpdate = false;
                 console.log("update_not_available")
             });
             // Finish download
             ipcRenderer.on('update_downloaded', () => {
              ipcRenderer.removeAllListeners('update_downloaded');
              this.loadingUpdate = false;
              this.message.innerText = 'Update Downloaded. It will be installed on restart. Restart now?';
             });
        },
        restartApp() {
            this.updateAvailable = false;
            ipcRenderer.send('restart_app');
        }
    }
}
</script>

<style scoped>
  #settings {
    margin-left: 100px;
    z-index: 1;
  }
  #version {
    margin-top: 50px;
  }

</style>
