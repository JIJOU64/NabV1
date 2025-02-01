<template>
  <header v-bind="$attrs" class="p-4 flex items-center justify-between bg-blue-500 text-white">
    <div class="flex items-center space-x-2">
      <HomeIcon class="w-6 h-6 text-white" />
      <span>Accueil</span>
    </div>
    
    <!-- Images du logo -->
    <div class="flex items-center space-x-4">
      <img v-if="imageUrlLogo" :src="imageUrlLogo" alt="Logo" class="h-10">
      <img v-if="imageUrlPhoto" :src="imageUrlPhoto" alt="Image de Fond" class="h-10">
    </div>
  </header>
</template>

<script setup>
console.log("Liaison page?")

// Import des icônes Heroicons
import { HomeIcon } from '@heroicons/vue/24/outline'

// Déclaration des images
const imageUrlLogo = new URL('@/assets/images/LogoNabiha.png', import.meta.url).href;
const imageUrlPhoto = new URL('@/assets/images/ImageBiasr.WebP', import.meta.url).href;
</script>



