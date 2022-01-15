import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from "axios";
import VueAxios from "vue-axios";
import Log from './common/Log'

Log.debug('.env', process.env)
Log.debug('main init vue')

Vue.config.productionTip = false

axios.defaults.baseURL = process.env.VUE_APP_SERVER_HOST;
Vue.use(VueAxios, axios)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
