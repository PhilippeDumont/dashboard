<template>
 <div id="settings">
  <v-container fluid>
     <v-row>
      <v-col cols="12">
          <h3 id="version">Version : <span>{{versionApp}}</span> </h3>
      </v-col>
      <v-col cols="12">
          <v-row>
              <v-col cols="4">
                  <v-btn :rounded="true" color="#013F52" :disabled="loadingUpdate" :loading="loadingUpdate" @click="checkForUpdate()">Download Update</v-btn>
              </v-col>
              <v-col cols="4">
                  <p id="update_message">Update status : {{update_message}}</p>            
              </v-col>
               <v-col cols="4">
                  <v-btn v-if="updateAvailable" color="#013F52" :rounded="true"  @click="restartApp()">Restart App for update</v-btn>  
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
        versionApp: "",
        updateMessage: "",
    }),
    mounted: function() {
     //GET VERSION APP
        // Ask version application
        ipcRenderer.send('app_version')
        // Reply on event listener
        ipcRenderer.on('app_version', (event, arg) => {
            ipcRenderer.removeAllListeners('app_version')
            this.versionApp =  arg.version
        });  
    },
    methods: {
        checkForUpdate() {
            ipcRenderer.send('check_for_update');
            this.loadingUpdate = true;
             // Update available
             ipcRenderer.on('update_available', () => {
                 ipcRenderer.removeAllListeners('update_available');
                 this.updateAvailable = true;
                 this.updateMessage = "Update update_available ! , Download now..."
             });

             // Update not available
             ipcRenderer.on('update_not_available', () => {
                 ipcRenderer.removeAllListeners('update_not_available');  
                 this.updateAvailable = false;
                 this.loadingUpdate = false;
                 this.updateMessage = "Not update available"
             });
             // Finish download update
             ipcRenderer.on('update_downloaded', () => {
              ipcRenderer.removeAllListeners('update_downloaded');
              this.loadingUpdate = false;
              this.updateAvailable = false;
              this.updateMessage = 'Update Downloaded. It will be installed on restart. Click on restart app to install update direcly';
             });
        },
        restartApp() {
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
    font-family: 'Roboto','sans-serif'
  }
  .v-btn {
      color: white;
  }
</style>
