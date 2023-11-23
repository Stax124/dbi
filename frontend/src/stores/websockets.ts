import { webSocketUrl } from '@/shared'
import { processWebSocket, type WebSocketMessage } from '@/websockets/websockets'
import { useWebSocket } from '@vueuse/core'
import { useMessage, useNotification } from 'naive-ui'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import { useGlobal } from './global'

export const useWebsocket = defineStore('websocket', () => {
  const notificationProvider = useNotification()
  const messageProvider = useMessage()
  const global = useGlobal()

  const onConnectedCallbacks: (() => void)[] = []
  const onDisconnectedCallbacks: (() => void)[] = []
  const onRefreshCallbacks: (() => void)[] = []

  const websocket = useWebSocket(`${webSocketUrl}/api/websockets/master`, {
    heartbeat: {
      message: 'ping',
      interval: 30000
    },
    autoReconnect: true,
    onMessage: (ws: WebSocket, event: MessageEvent) => {
      if (event.data === 'pong') {
        return
      }

      const data = JSON.parse(event.data) as WebSocketMessage
      if (data.type === 'refresh_models') {
        onRefreshCallbacks.forEach((callback) => callback())
        console.log('Models refreshed')
        return
      }
      processWebSocket(data, global, notificationProvider)
    },
    onConnected: () => {
      messageProvider.success('Connected to server')
      onConnectedCallbacks.forEach((callback) => callback())
    }
  })

  function ws_text() {
    switch (readyState.value) {
      case 'CLOSED':
        return 'Closed'
      case 'CONNECTING':
        return 'Connecting'
      case 'OPEN':
        return 'Connected'
    }
  }

  function get_color() {
    switch (readyState.value) {
      case 'CLOSED':
        return 'error'
      case 'CONNECTING':
        return 'warning'
      case 'OPEN':
        return 'success'
    }
  }

  const readyState = ref(websocket.status)
  const loading = computed(() => readyState.value === 'CONNECTING')
  const text = computed(() => ws_text())
  const color = computed(() => get_color())

  return {
    websocket,
    readyState,
    loading,
    text,
    ws_open: websocket.open,
    color,
    onConnectedCallbacks,
    onDisconnectedCallbacks,
    onRefreshCallbacks
  }
})
