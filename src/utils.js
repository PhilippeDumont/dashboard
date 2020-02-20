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
            resolve(arg)
        })

    })
}


/*************************************************************
 * These functions are use to manipulate path
 * **********************************************************/

/* ************************************************
 * path: the file path
 *
 * return the path with '/' for path separators
 **************************************************/
export function pathToStandardFormat(path) {
    if (process.platform === 'win32') {
        return path.replace(/\\/g, '/')
    }
}

/**************************************************
 * path: the file path
 * 
 * return the name of the selected file
 **************************************************/
export function getFileNameOfPath(path) {
    let pathItems = path.split('/')
    return pathItems[pathItems.length - 1]
}
