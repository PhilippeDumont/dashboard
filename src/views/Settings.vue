<template>
 <div id="settings">
  <v-container fluid>
     <v-row>
      <v-col cols="12">
          <v-row>
               <v-col cols="4">
                  <v-btn id="btn_download" :rounded="true" color="blue-grey" :disabled="loadingUpdate" :loading="loadingUpdate" @click="openDialog()">Download Update</v-btn>
               </v-col>

             <v-dialog v-model="modalDialog" max-width="500px" persistent> 
               <v-card>
                    <v-card-title class="justify-center">
                      <svg style="width:45px;height:45px;color:red;" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M13,14H11V10H13M13,18H11V16H13M1,21H23L12,2L1,21Z" />
                      </svg>
                      <h4>Are you sure you want update your application ?</h4>
                    </v-card-title>
                    <v-card-actions class="justify-center">
                       <v-btn  @click="closeDialog()" >CANCEL</v-btn> 
                       <v-btn  class="error" @click="checkForUpdate()">UPDATE</v-btn> 
                    </v-card-actions>
               </v-card>
              </v-dialog>

              <v-col cols="4">
                  <p id="update_message">Update status : {{updateMessage}}</p>            
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
import { mapActions } from 'vuex'
export default {
    data: () => ({
        loadingUpdate: false,
        updateAvailable: false,
        updateMessage: "",
        modalDialog: false,
    }),
    created() {
      this.setExpansionBarVisibility(false)
    },
    methods: {
        openDialog() {
            this.modalDialog = true
        },
        closeDialog() {
            this.modalDialog = false
        },
        checkForUpdate() {
            this.closeDialog()
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
        },
        ...mapActions([
         'setExpansionBarVisibility',
        ]),
        
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
  #btn_download {
    color: white;
  }

</style>
