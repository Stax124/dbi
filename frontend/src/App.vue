<template>
  <NConfigProvider :theme="currentTheme">
    <NMessageProvider>
      <NNotificationProvider>
        <NavBar />
        <div class="main-content-wrapper">
          <div class="main-content">
            <RouterView />
          </div>
        </div>
      </NNotificationProvider>
    </NMessageProvider>
  </NConfigProvider>
</template>

<script setup lang="ts">
import {
  NConfigProvider,
  NMessageProvider,
  NNotificationProvider,
  darkTheme,
  lightTheme
} from 'naive-ui'
import { computed } from 'vue'
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'

const currentTheme = computed(() => {
  return localStorage.getItem('theme') === 'dark' ? darkTheme : lightTheme
})

const textColor = computed(() => {
  return localStorage.getItem('theme') === 'dark' ? '#fff' : '#000'
})

// Set default theme
localStorage.setItem('theme', localStorage.getItem('theme') || 'dark')
</script>

<style scoped>
body {
  color: v-bind('textColor');
}

.main-content-wrapper {
  display: flex;
  justify-content: center;
  padding: 24px;
}

.main-content {
  width: 80vw;
}
</style>
