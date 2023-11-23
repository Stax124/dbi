<template>
  <EditorJSComponent
    :data="{ blocks: [] }"
    :editable="true"
    :on-save="(data) => console.log(data)"
  />
</template>

<script setup lang="ts">
import { EditorJSComponent } from '@/components'
import type { OutputData } from '@editorjs/editorjs'

function onEditorSave(data: OutputData) {
  console.log(data)
}
</script>
