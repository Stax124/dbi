<template>
  <div
    style="display: flex; justify-content: center; align-items: center; height: calc(100vh - 56px)"
  >
    <NCard
      title="Login"
      style="max-width: 550px"
      :content-style="{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        flexDirection: 'column'
      }"
    >
      <NInput v-model:value="email" placeholder="Email" style="margin-bottom: 8px" />
      <NInput
        v-model:value="password"
        placeholder="Password"
        type="password"
        show-password-on="click"
        :minlength="8"
        :maxlength="256"
        style="margin-bottom: 8px"
      />
      <NButton type="primary" @click="login" :loading="loading">Login</NButton>
    </NCard>
  </div>
</template>

<script setup lang="ts">
import { serverUrl } from '@/shared'
import { useCookies } from '@vueuse/integrations/useCookies'
import { NButton, NCard, NInput } from 'naive-ui'
import { ref } from 'vue'

const email = ref('')
const password = ref('')
const cookies = useCookies()

const loading = ref(false)

function login() {
  const url = new URL(`${serverUrl}/api/users/login`)
  url.searchParams.append('email', email.value)
  url.searchParams.append('password', password.value)
  loading.value = true
  fetch(url)
    .then((data) => {
      data.json().then((token) => {
        if (token.length) cookies.set('token', token)
        window.location.href = '/'
      })
      loading.value = false
    })
    .catch((err) => {
      console.log(err)
      loading.value = false
    })
}
</script>
