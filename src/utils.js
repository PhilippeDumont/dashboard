import { ipcRenderer }  from 'electron'

/*************************************************************
 * SendRequest use ipc to run a function in the Main Process
 * 
 * params:
 * requestName: is the name of the request in the Electron Main process
 * ...args: is a list of argument for this request
 * 
 * return a Promise who is resolve when the Electron Main process is over
 *************************************************************/
export async function sendRequest(requestName, ...args) {
    return new Promise((resolve) => {
        ipcRenderer.send(requestName, args)
        ipcRenderer.once(requestName + '-reply', (event, arg) => {
            resolve(arg);
        })

    })
}