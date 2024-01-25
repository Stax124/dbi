import { serverUrl } from '@/shared'
import { type IUser } from '@/types'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGlobal = defineStore('global', () => {
  const theme = ref('dark')
  const user = ref<IUser | null>(null)

  async function getUser() {
    const res = await fetch(`${serverUrl}/api/users/get-user`)
    if (res.status === 200) {
      user.value = await res.json()
    }
  }

  return {
    theme,
    user,
    getUser
  }
})
