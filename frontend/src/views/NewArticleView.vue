<template>
  <NCard title="Information">
    <NForm>
      <NFormItem label="Title">
        <NInput />
      </NFormItem>
      <NFormItem label="Tags">
        <NSelect multiple tag filterable />
      </NFormItem>
    </NForm>
  </NCard>

  <NCard title="Content">
    <EditorJSComponent
      :data="{ blocks: [] }"
      :editable="true"
      :on-save="(data) => console.log(data)"
      style="margin-bottom: 12px"
    />
  </NCard>

  <NCard title="Actions">
    <NButton type="success">Publish Article</NButton>
  </NCard>
</template>

<script setup lang="ts">
import { EditorJSComponent } from '@/components'
import type { OutputData } from '@editorjs/editorjs'
import { NButton, NCard, NForm, NFormItem, NInput, NSelect } from 'naive-ui'

function onEditorSave(data: OutputData) {
  console.log(data)
}
</script>
