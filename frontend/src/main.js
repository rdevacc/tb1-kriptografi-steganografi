import { createApp } from 'vue'
import App from './App.vue'
import { BootstrapVue3 } from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.min.css'  // Bootstrap CSS
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'  // BootstrapVue 3 CSS

const app = createApp(App)
app.use(BootstrapVue3)
app.mount('#app')
