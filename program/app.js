const {app, BrowserWindow, ipcMain, Menu, Tray} = require('electron') // http://electronjs.org/docs/api
const path = require('path') // https://nodejs.org/api/path.html
const url = require('url') // https://nodejs.org/api/url.html
const { PythonShell } = require("python-shell");

let window = null

// Wait until the app is ready
app.once('ready', () => {
  // Create a new window
  window = new BrowserWindow({
    width: 1480,
    height: 900,
    minwidth: 1480,
    minheight: 900,
    show: false,
    resizable: true,
    icon: path.join(__dirname, './assets/logo 64x64.png'),
    webPreferences: {
      nodeIntegration: true
    }

  })

  // Load a URL in the window to the local index.html path
  window.loadURL(url.format({
    pathname: path.join(__dirname, 'index.html'),
    protocol: 'file:',
    slashes: true
  }))

  // Show window when page is ready
  window.once('ready-to-show', () => {
    window.show()
  })

})

//백앤드
ipcMain.on('ardulight_1', (event, argument) => {
  console.log(argument);
  event.sender.send('ardulight_2', "ok");
  
  let options = {
    scriptPath: "",
    args: [argument.port, argument.command]
  };

  PythonShell.run("./py/ardulight_arg.py", options, function(err, data) {
    if (err) {
      event.sender.send("ardulight_2", {result: "err", error: err})
      console.log(err)
    } else {
      
      if(data[0].indexOf(`[${argument.port}]`) != -1) {
        event.sender.send("ardulight_2", {result: "ok"})
      } else {
        event.sender.send("ardulight_2", {result: "err", error: err})
      }
      
    }
  });
})