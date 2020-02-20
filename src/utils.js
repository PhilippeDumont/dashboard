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
        console.log("REQUEST NAME :"+requestName+"ARGS :"+args)
        try {
            ipcRenderer.send(requestName, args)
        } catch(e) {
            console.log("IPC RENDERER SEND ERROR: "+e)
        }

        try {
            ipcRenderer.once(requestName + '-reply', (event, arg) => {
                resolve(arg);
            })
        } catch(e) {
            console.log("IPC RENDERER ONCE ERROR: "+e)
        }
        
        

    })
}