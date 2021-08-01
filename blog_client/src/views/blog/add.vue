<template>
    <div class="docMain">
        <span>文档正文：</span>
        <UEtor :config=config ref='ue'></UEtor>   
    </div>
</template>
<style>

</style>
<script>
import UEtor from '@/components/UE.vue'

export default {
  name: 'UEtor',
  data() {
    return {
      config: {
          initalFrameWidth: 1038,
          initalFrameHeight: 350,
      },
      docTitle: '',
      docDescription: '',
      docMain: '',
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
