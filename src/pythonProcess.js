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

// const guessPackaged = () => {
//   const fullPath = path.join(__dirname, PY_DIST_FOLDER)
//   return require('fs').existsSync(fullPath)
// }

const fs = require('fs');
const { Console } = require('console');
const output = fs.createWriteStream('./stdout.log');
const errorOutput = fs.createWriteStream('./stderr.log');
// Custom simple logger
const logger = new Console({ stdout: output, stderr: errorOutput });

const getScriptPath = () => {
  // if (!guessPackaged()) {
  //   return path.join(__dirname, PY_FOLDER, PY_MODULE + '.py')
  // }
  if (process.platform === 'win32') {
    let api_path = path.join(__dirname, PY_FOLDER, PY_MODULE + '.exe').replace("\\win-unpacked\\resources\\app.asar", "");
    logger.log("PATH WIN 32 : "+api_path)
    return api_path
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
  console.log("PATH API :"+getScriptPath())
  console.log("pythonProcess: " + args)
  const { stdout } = await execFile(getScriptPath(), args)
  return stdout
}

