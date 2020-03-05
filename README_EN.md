# Dashboard

## Application overview

Dashboard allowing the visualization of data in the form of graphs with different analyse level.

## Project setup
1) Download or clone the git repository on your computer.
2) Execute one of the comands below

### Compiles Application and Local API and hot-reloads for development
```bash
npm run electron:serve
```

### Compiles and minifies for production(no release on GitHub)
```bash
npm run electron:build
```
#### Windows
The file which contains the compile application is called 'dist_electron'. 
 * This file has a compress directory called 'win-unpacked' containing application. 
 ![alt text](Documentation/pictures/Build/win-unpacked.png)
 * This file has a basic installer.
 ![alt text](Documentation/pictures/Build/installer.png)

 
### Compiles and minifies for release on GitHub
```bash
npm run release
```

<span style="color: red;">The release of application need the token from Github, please check this page for more informations : <a href="https://github.com/settings/tokens">Generate Token on GitHub</a></span>.

<span style="color: red;">If you are contributor in the project and you have a token from GitHub, you should create a file nammed "electron-builder.yml" and introduce this code : </span>

```yml
appId: dashboard
publish:
  provider: github
  token: /* YOUR TOKEN */
```

# API

[APi Documentation](Documentation/EN/Api/Api_EN.md)