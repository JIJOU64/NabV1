import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

createApp(App)
    .use(createPinia()) // Apply Pinia
    .use(router)        // Apply the router
    .mount('#app')      // Mount application in element with the ID 'app'
