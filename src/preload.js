const { contextBridge } = require('electron');
const { version } = require('../package.json');

contextBridge.exposeInMainWorld('blinkyLights', {
  version,
  electron: process.versions.electron
});
