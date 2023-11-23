import { type IUser } from '@/types'
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useGlobal = defineStore('global', () => {
  const theme = ref('dark')
  const user = ref<IUser | null>(null)

  return {
    theme,
    user
  }
})
