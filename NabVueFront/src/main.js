import './assets/main.css'

// Vuetify import
//import 'vuetify/styles'
//import { createVuetify } from 'vuetify'
//import * as components from 'vuetify/components'
//import * as directives from 'vuetify/directives'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import vuetify from './plugins/vuetify'


// Initializing Vuetify
//const vuetify = createVuetify({
    //components,
    //directives,
  //})

createApp(App)
    .use(vuetify)      // Apply Vuetify
    .use(createPinia()) // Apply Pinia
    .use(router)        // Apply the router
    .mount('#app')      // Mount application in element with the ID 'app'
