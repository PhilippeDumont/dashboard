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

    console.log("HELLO")

    var python = require('child_process').spawn('python', ['src/hello.py']);
    python.stdout.on('data', function (data) {
        console.log("data: ", data.toString('utf8'));
    });

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
 *************************************************************/

ipcMain.on('api-python', (event, args) => {
  console.log("ipc-api-python: " + args);
  // var python = require('child_process').spawn('python', ['api/']);
  //   python.stdout.on('data', function (data) {
  //       console.log("data: ", data.toString('utf8'));
  //   });

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

// ipcMain.on('open-json-file', (event, args) => {
//   dialog.showOpenDialog({ properties: [ 'openFile', 'multiSelections' ]}).then((e) => {
//     readFileInJson(e.filePaths[0]).then((data) => {
//       console.log(data)
//       event.reply('open-json-file-reply', data )
//     }).catch()
//   }).catch((e) => {
//     console.log(e)
//   })
// })


ipcMain.on('import-activity-file', (event, args) => {
  console.log("ipc-import-activity: " + args);
  dialog.showOpenDialog({ properties: [ 'openFile', 'multiSelections' ]}).then((e) => {
    let path = e.filePaths[0]
    let args = ['import_activity_file', path]

    pythonProcess(args).then((value) => {
      event.reply('import-activity-file-reply', value)
    }).catch((e) => {
      console.log('Error in python file')
      console.log(e)
    })
  }).catch((e) => {
    console.log(e)
  })
})


ipcMain.on('import-item-file', (event, args) => {
  console.log("ipc-import-item: " + args);
  dialog.showOpenDialog({ properties: [ 'openFile', 'multiSelections' ]}).then((e) => {
    let path = e.filePaths[0]
    let args = ['import_item_file', path]

    pythonProcess(args).then((value) => {
      event.reply('import-item-file', value)
    }).catch((e) => {
      console.log('Error in python file')
      console.log(e)
    })
  }).catch((e) => {
    console.log(e)
  })
})
