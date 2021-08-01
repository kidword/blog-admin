<template>
    <div id="UEtor">
        <script id='editor' type="text/plain"></script>
    </div>
</template>
<style>

</style>
<script>
import '@/UE/ueditor.config.js'
import '@/UE/ueditor.all.min.js'
import '@/UE/lang/zh-cn/zh-cn.js'

import '@/UE/ueditor.parse.min.js'

export default {
  name: 'UEtor',
  data() {
    return {
      editor: null
    }
  },
  prop: {
    defaultMsg: {type: String},
    config: {type: Object}
  },
  mounted() {
    const _this = this
    _this.editor = UE.getEditor('editor', _this.config)
  },

  methods: {
    getUEContent(){
        return this.editor.getUEContent()
    }
  },

  destroyed(){
      this.editor.destroy()
  }

}
</script>
