<template>
    <v-app-bar app dense>
        <v-img
            :src=imageUrl
            alt="Logo"
            width="45"
            height="45"
        ></v-img>
      <v-toolbar-title>Votre Application</v-toolbar-title>
    </v-app-bar>
  </template>
  
<script setup>
    // L'URL de l'image
    const imageUrl = new URL('@/assets/images/LogoNabiha.png', import.meta.url).href;
</script>
  
  <style scoped>
  </style>
  


