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

// Custom simple logger : Allow to write log in production.
const fs = require('fs');
const { Console } = require('console');
const output = fs.createWriteStream('./stdout.log');
const errorOutput = fs.createWriteStream('./stderr.log');
const logger = new Console({ stdout: output, stderr: errorOutput });
// Is development or is production
const isDevelopment = process.env.NODE_ENV !== 'production'
const isProduction = process.env.NODE_ENV == 'production'
// API PATH
let api_path = "";

  /*
  *  |---------------------------------------------------------------------|
  *  |  Platform              |     Name           |      API PATH         |
  *  |---------------------------------------------------------------------|
  *  |  Windows               |     win32          |  dirname\api\api.exe  |
  *  |  Linux                 |     linux          |                       |
  *  |  MacOS                 |     darwin         |                       |
  *  |---------------------------------------------------------------------|
  */
  
  /* ********************************* WINDOWS *********************************** */
const getScriptPath = () => {
  if (process.platform === 'win32') {
    if(isDevelopment) {
      api_path = path.join(__dirname, PY_FOLDER, PY_MODULE + '.exe')
    }
    else if(isProduction) {
      api_path = path.join(__dirname, PY_FOLDER, PY_MODULE + '.exe').replace("\\resources\\app.asar","");
    } else {
      api_path = path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE); 
    }
    logger.log("API PATH : WIN 32 : "+api_path) 
  } 
  /* ********************************** LINUX *********************************** */
  else if (process.platform === 'linux') {
    if(isDevelopment) {
      api_path = "";
    }
    else if(isProduction) {
      api_path = "";
    } else {
      api_path = "";
    }
    logger.log("API PATH : LINUX : "+api_path)
  } 
  /* ********************************* MACOS *********************************** */
  else if (process.platform === 'darwin') {
    if(isDevelopment) {
      api_path = "";
    }
    else if(isProduction) {
      api_path = "";
    } else {
      api_path = "";
    } 
    logger.log("API PATH : MACOS : "+api_path)
  }
  return api_path;
}

/*************************************************************
 * pythonProcess
 * 
 * parameter:
 *  args: ['name_of_method', 'arguments_method']
 *************************************************************/
export async function pythonProcess(args) {
  const { stdout } = await execFile(getScriptPath(), args)
  return stdout
}
