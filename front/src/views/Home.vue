<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import Log from '@/common/Log'
import HelloWorld from '@/components/HelloWorld.vue'
import TestApi from '@/api/TestApi'

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data () {
    return {
      result: null
    }
  },
  mounted () {
    this.getTestApi()
  },
  methods: {
    async getTestApi () {
      const ret = await TestApi.get()
      Log.debug(ret)
    }
  }
}
</script>
