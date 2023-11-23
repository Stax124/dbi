<template>
  <div id="editorjs-container"></div>
</template>

<script setup lang="ts">
import EditorJS, { type OutputData } from '@editorjs/editorjs'
import Header from '@editorjs/header'
import List from '@editorjs/list'
import ImageLink from '@editorjs/simple-image'
import Table from '@editorjs/table'
import { type PropType } from 'vue'

const props = defineProps({
  data: {
    type: Object as PropType<OutputData>,
    required: true
  },
  onSave: {
    type: Function as PropType<(data: OutputData) => void>,
    required: true
  },
  editable: {
    type: Boolean,
    default: false
  }
})

const editor = new EditorJS({
  /**
   * Id of Element that should contain the Editor
   */
  holder: 'editorjs-container',

  /**
   * Available Tools list.
   * Pass Tool's class or Settings object for each Tool you want to use
   */
  tools: {
    header: Header,
    list: List,
    imageLink: ImageLink,
    table: Table
  },
  onChange: () => {
    editor.save().then(props.onSave)
  },
  data: props.data,
  readOnly: !props.editable
})
</script>
