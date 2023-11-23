const loc = window.location
const apiPort = 8080

let new_uri
if (loc.protocol === 'https:') {
  new_uri = 'wss:'
} else {
  new_uri = 'ws:'
}

export const serverUrl = import.meta.env.DEV
  ? `http://localhost:${apiPort}`
  : loc.protocol + '//' + loc.host
export const webSocketUrl = import.meta.env.DEV
  ? `ws://localhost:${apiPort}`
  : new_uri + '//' + loc.host
