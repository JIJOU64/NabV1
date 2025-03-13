<template>
  <header 
    v-bind="$attrs"
    :style="imageUrlPhoto ? { backgroundImage: `url(${imageUrlPhoto})` } : {}" 
    class="p-4 flex items-center justify-between bg-blue-500 text-white bg-cover bg-center">
    
    <!-- Logo -->
    <div class="flex items-center space-x-4">
      <img v-if="imageUrlLogo" :src="imageUrlLogo" alt="Logo" class="h-10" />
    </div>

    <!-- Menu de navigation -->
    <div class="flex w-full justify-end lg:flex-row flex-col lg:space-x-4 space-y-4 lg:space-y-0">
      <router-link to="/" class="flex items-center space-x-2">
        <HomeIcon class="w-6 h-6 text-white" />
        <span>Accueil</span>
      </router-link>
      <router-link to="/client" class="flex items-center space-x-2">
        <UserIcon class="w-6 h-6 text-white" />
        <span>Clients</span>
      </router-link>
      <router-link to="#bilans" class="flex items-center space-x-2">
        <ChartBarIcon class="w-6 h-6 text-white" />
        <span>Bilans</span>
      </router-link>
      <router-link to="#documents" class="flex items-center space-x-2">
        <DocumentIcon class="w-6 h-6 text-white" />
        <span>Documents</span>
      </router-link>
      <!-- Affichage de l'utilisateur ou "Se connecter" -->
      <router-link v-if="!auth.user" to="/login" class="flex items-center space-x-2">
        <ArrowRightCircleIcon class="w-6 h-6 text-white" />
        <span>Se connecter</span>
      </router-link>
      <span
       v-else
       @click="logout"
        class="flex items-center space-x-2 cursor-pointer hover:underline">
        <ArrowRightCircleIcon class="w-6 h-6 text-white" />
        <span>{{ username }}</span>
      </span>
    
    </div>
  </header>
</template>

<script setup>
import { HomeIcon, UserIcon, ChartBarIcon, DocumentIcon, ArrowRightCircleIcon  } from '@heroicons/vue/24/outline'
import { useAuth } from '@/stores/auth'
import { computed } from 'vue'

const auth = useAuth()

const username = computed(() => auth.user?.username)

const logout = () => {
  auth.logout()
}


// Déclaration des images
const imageUrlLogo = new URL('@/assets/images/LogoNabiha.png', import.meta.url).href
const imageUrlPhoto = new URL('@/assets/images/ImageBiasr.WebP', import.meta.url).href


</script>
