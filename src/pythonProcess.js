'use strict'

const path = require('path')
const util = require('util')
const execFile = util.promisify(require('child_process').execFile)


/*************************************************************
 * Don't forget to insert the compile python file in dist_electron.
 *************************************************************/

const PY_DIST_FOLDER = 'api/dist'
const PY_FOLDER = 'api'
const PY_MODULE = 'api' // without .py suffix

const getScriptPath = () => {
  if (process.platform === 'win32') {
    return path.join(__dirname, PY_FOLDER, PY_MODULE + '.exe')
  }
  return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE)
}


/*************************************************************
 * pythonProcess
 * 
 * parameter:
 *  args: ['name_of_method', 'arguments_method']
 *************************************************************/
export async function pythonProcess(args) {
  console.log(getScriptPath())
  console.log("pythonProcess: " + args)
  const { stdout } = await execFile(getScriptPath(), args)
  return stdout
}

