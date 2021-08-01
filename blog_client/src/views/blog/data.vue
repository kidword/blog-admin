<template>
  <div>
      123
  </div>
</template>
<style>

</style>
<script>
import { addArticle } from "@/api/blog";
import checkPermission from "@/utils/permission";
export default {
  data() {
    return {
      
    };
  },
  computed: {},
  watch: {
    
  },
  created() {
    this.addArticle()
  },
  methods: {
    checkPermission,
    // 调用添加文章方法
    addArticle() {
      //  let params = {
      //    content: "<p>测试</p>",
      //    category: 'python',
      //    user: 1
      //  }
       addArticle().then(response => {
        console.log(response.data)
       })
    }
  }
};
</script>
