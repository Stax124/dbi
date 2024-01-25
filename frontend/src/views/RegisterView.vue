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
      <NInput v-model:value="username" placeholder="Username" style="margin-bottom: 8px" />
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
      <NButton type="primary" @click="register" :loading="loading">Register</NButton>
    </NCard>
  </div>
</template>

<script setup lang="ts">
import { sha256 } from '@/helper'
import { serverUrl } from '@/shared'
import { NButton, NCard, NInput } from 'naive-ui'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const username = ref('')
const password = ref('')
const router = useRouter()
const loading = ref(false)

async function register() {
  loading.value = true
  fetch(`${serverUrl}/api/users/create-user`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      email: email.value,
      username: username.value,
      password: await sha256(password.value)
    })
  })
    .then((res) => {
      loading.value = false

      if (res.status !== 200) {
        console.error(res.statusText)
        return
      }

      console.log('account created')
      router.push('/login')
    })
    .catch((err) => {
      console.log(err)
      loading.value = false
    })
}
</script>
