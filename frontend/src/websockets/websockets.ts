import type { NotificationApiInjection } from 'naive-ui/es/notification/src/NotificationProvider'

export interface WebSocketMessage {
  type: string
  data: any
}

export function processWebSocket(
  message: WebSocketMessage,
  global: ReturnType<(typeof import('@/stores/global'))['useGlobal']>,
  notificationProvider: NotificationApiInjection
): void {
  switch (message.type) {
    case 'test': {
      break
    }
    case 'notification': {
      message.data.timeout = message.data.timeout || 0

      notificationProvider.create({
        type: message.data.severity,
        title: message.data.title,
        content: message.data.message,
        duration: message.data.timeout
      })
      break
    }
    default: {
      console.log(message)
    }
  }
}
