const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('files', { pickName: () => ipcRenderer.invoke('pick-name') });
