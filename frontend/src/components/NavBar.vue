<template>
  <div class="navbar-wrapper">
    <div class="navbar">
      <NButton text>
        <NIcon size="24" :color="homeIconColor">
          <Home />
        </NIcon>
      </NButton>

      <div style="display: flex; flex-direction: row; align-items: center">
        <NButton class="nav-button" :bordered="false" @click="router.push('/')">
          <template #icon>
            <NIcon>
              <Home />
            </NIcon>
          </template>
          Home
        </NButton>
        <NButton class="nav-button" ghost :bordered="false">
          <template #icon>
            <NIcon>
              <Newspaper />
            </NIcon>
          </template>
          Articles
        </NButton>
        <NButton class="nav-button" ghost :bordered="false" @click="router.push('/new-article')">
          <template #icon>
            <NIcon>
              <Pencil />
            </NIcon>
          </template>
          Write new article
        </NButton>

        <NTooltip>
          <template #trigger>
            <NAvatar round :src="global.user?.avatar" />
          </template>

          <div style="display: flex; flex-direction: column" v-if="global.user">
            <NText>Username: {{ global.user?.username }}</NText>

            <NDivider />

            <NButton class="avatar-dropdown-button">
              <template #icon>
                <NIcon>
                  <PersonCircleOutline />
                </NIcon>
              </template>
              Profile
            </NButton>
            <NButton class="avatar-dropdown-button">
              <template #icon>
                <NIcon>
                  <Settings />
                </NIcon>
              </template>
              Settings
            </NButton>
            <NButton class="avatar-dropdown-button" @click="logout">
              <template #icon>
                <NIcon>
                  <LogOut />
                </NIcon>
              </template>
              Log out
            </NButton>
          </div>

          <div style="display: flex; flex-direction: column" v-else>
            <NButton class="avatar-dropdown-button" @click="router.push('/login')">
              <template #icon>
                <NIcon>
                  <LogIn />
                </NIcon>
              </template>
              Login
            </NButton>
            <NButton class="avatar-dropdown-button" @click="router.push('/register')">
              <template #icon>
                <NIcon>
                  <LogIn />
                </NIcon>
              </template>
              Register
            </NButton>
          </div>
        </NTooltip>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { serverUrl } from '@/shared'
import {
  Home,
  LogIn,
  LogOut,
  Newspaper,
  Pencil,
  PersonCircleOutline,
  Settings
} from '@vicons/ionicons5'
import { NAvatar, NButton, NDivider, NIcon, NText, NTooltip } from 'naive-ui'
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { useGlobal } from '../stores/global'
import { useWebsocket } from '../stores/websockets'

const global = useGlobal()
const router = useRouter()
const websocket = useWebsocket()

const homeIconColor = computed(() => {
  return websocket.readyState === 'OPEN' ? '#00ff00' : '#ff0000'
})

async function logout() {
  const res = await fetch(`${serverUrl}/api/users/logout`, {
    method: 'POST'
  })

  if (res.status === 200) {
    global.user = null
  }
}
</script>

<style scoped>
.navbar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background-color: rgb(32, 36, 40);
  height: 56px;
  margin: 0 24px;
}

.navbar-wrapper {
  width: 100%;
  background-color: rgb(32, 36, 40);
  z-index: 10;
}

.nav-button:not(:last-child) {
  margin-right: 4px;
}

.avatar-dropdown-button:not(:last-child) {
  margin-bottom: 4px;
}
</style>
