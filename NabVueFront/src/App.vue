
<template>
  <v-app>
    
    <CrmHeader />
      
    <router-view />

    <CrmFooter />
  </v-app>
</template>

<script setup>
import CrmHeader from './components/CrmHeader.vue';
import CrmFooter from './components/CrmFooter.vue';
</script>

<style scoped>
/* Pas d'image de fond dans App.vue */
</style>
