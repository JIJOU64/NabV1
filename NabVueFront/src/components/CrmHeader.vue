<template>
    <v-app-bar
    color="teal-darken-4"
    :image=imageUrlPhoto
    >
      <v-img
          :src=imageUrlLogo
          alt="Logo"
          width="45"
          height="45"
      ></v-img>
      <h1>kdjhfjkqdsh</h1>
      <v-btn icon>
        <v-icon icon="mdi-home" />
        
      </v-btn>
      <v-btn icon>
        <v-icon icon="mdi-account" />
        
      </v-btn>>
      <v-btn icon>
        <v-icon icon="mdi-finance" />
        
      </v-btn>>
      <v-btn icon>
        <v-icon icon="mdi-folder-arrow-left-right-outline" />
        
      </v-btn>>
      
    </v-app-bar>
  </template>
  
<script setup>
    // L'URL de l'image
    const imageUrlLogo = new URL('@/assets/images/LogoNabiha.png', import.meta.url).href;
    const imageUrlPhoto = new URL('@/assets/images/ImageBiasr.WebP', import.meta.url).href;
</script>
  
<style scoped>
</style>
  


