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
import { sha256 } from '@/helper'
import { serverUrl } from '@/shared'
import { NButton, NCard, NInput } from 'naive-ui'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useGlobal } from '../stores/global'

const global = useGlobal()

const email = ref('')
const password = ref('')
const router = useRouter()
const loading = ref(false)

async function login() {
  const url = new URL(`${serverUrl}/api/users/login`)
  url.searchParams.append('email', email.value)
  url.searchParams.append('password', await sha256(password.value))
  loading.value = true
  fetch(url)
    .then((data) => {
      loading.value = false
      console.log('logged in')
      data.json().then(
        (res) => {
          console.log(res.token)
          global
            .getUser()
            .then(() => {
              router.push('/')
            })
            .catch((err) => {
              console.log(err)
            })
        },
        (err) => {
          console.log(err)
        }
      )
    })
    .catch((err) => {
      console.log(err)
      loading.value = false
    })
}
</script>
