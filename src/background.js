'use strict'

import { app, protocol, BrowserWindow , ipcMain, dialog } from 'electron'
import { pythonProcess } from './pythonProcess.js'
import {
  createProtocol,
  /* installVueDevtools */
} from 'vue-cli-plugin-electron-builder/lib'
const isDevelopment = process.env.NODE_ENV !== 'production'

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let win

// Scheme must be registered before the app is ready
protocol.registerSchemesAsPrivileged([{scheme: 'app', privileges: { secure: true, standard: true } }])

function createWindow () {
  // Create the browser window.
  win = new BrowserWindow({ width: 800, height: 600, webPreferences: {
    nodeIntegration: true
  } })

  if (process.env.WEBPACK_DEV_SERVER_URL) {
    // Load the url of the dev server if in development mode
    win.loadURL(process.env.WEBPACK_DEV_SERVER_URL)
    if (!process.env.IS_TEST) win.webContents.openDevTools()
  } else {
    createProtocol('app')
    // Load the index.html when not in development
    win.loadURL('app://./index.html')
    }

  win.on('closed', () => {
    win = null
  })
}

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (win === null) {
    createWindow()
  }
})

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', async () => {
  if (isDevelopment && !process.env.IS_TEST) {
    // Install Vue Devtools
    // Devtools extensions are broken in Electron 6.0.0 and greater
    // See https://github.com/nklayman/vue-cli-plugin-electron-builder/issues/378 for more info
    // Electron will not launch with Devtools extensions installed on Windows 10 with dark mode
    // If you are not using Windows 10 dark mode, you may uncomment these lines
    // In addition, if the linked issue is closed, you can upgrade electron and uncomment these lines
    // try {
    //   await installVueDevtools()
    // } catch (e) {
    //   console.error('Vue Devtools failed to install:', e.toString())
    // }

  }
  createWindow()
})

// Exit cleanly on request from parent process in development mode.
if (isDevelopment) {
  if (process.platform === 'win32') {
    process.on('message', data => {
      if (data === 'graceful-exit') {
        app.quit()
      }
    })
  } else {
    process.on('SIGTERM', () => {
      app.quit()
    })
  }
}



// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.

/*************************************************************
 * API Python
 * Execute a script python
 * requestName: 'api-python'
 * args: [functionName, {functionArg}]
 * The list of function name is listed in the python API
 * ***********************************************************
 * List of requests present in the API :
 * -------------------------------------------------------------------------------------------------------------------
 * | Function name        | Description                            | Function args model                             |
 * |-----------------------------------------------------------------------------------------------------------------|
 * | init_db              | Allow to create a database with the    | init_db, project_name                           |
 * |                      | name of the project                    |                                                 |
 * |-----------------------------------------------------------------------------------------------------------------|
 * | import_item_file     | Allow to load items by a file with a   | import_item_file, [project_name, file_path]     |
 * |                      | CSV format in the specified project    |                                                 |
 * |-----------------------------------------------------------------------------------------------------------------|
 * | import_activity_file | Allow to load activities by a file     | import_activity_file, [project_name, file_path] |
 * |                      | with a CSV format in the specified     |                                                 |
 * |                      | project                                |                                                 |
 * -------------------------------------------------------------------------------------------------------------------
 * 
 *************************************************************/
ipcMain.on('api-python', (event, args) => {
  console.log("ipc-api-python: " + args);
  pythonProcess(args).then((value) => {
     event.reply('api-python-reply', value)
   }).catch((e) => {
     console.log('Error in python file')
     console.log(e)
   })
})


/*************************************************************
 * API OS
 * Open the Operating System File dialog
 * requestName: 'open-dialog'
 * args: None
 *************************************************************/

ipcMain.on('open-dialog', (event) => {
  dialog.showOpenDialog({properties: [ 'openFile', 'multiSelections' ]}).then((e) => {
    let path = e.filePaths[0];
    event.reply('open-dialog-reply', path);
  }).catch((e) => {
    console.log(e)
  })
})
