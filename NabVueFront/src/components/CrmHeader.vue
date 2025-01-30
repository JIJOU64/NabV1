<template>
    Header à faire avec Tailwind
    <img :src=imageUrlLogo alt="Logo">
    <img :imageUrlPhoto alt="Image de Fond">
  </template>

<script setup>
    // L'URL de l'image
    const imageUrlLogo = new URL('@/assets/images/LogoNabiha.png', import.meta.url).href;
    const imageUrlPhoto = new URL('@/assets/images/ImageBiasr.WebP', import.meta.url).href;
</script>

<style scoped>
</style>



