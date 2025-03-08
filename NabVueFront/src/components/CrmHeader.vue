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

      <!-- Bouton de déconnexion -->
      <button v-if="isAuthenticated" @click="logout" class="flex items-center space-x-2">
        <span>Déconnexion</span>
      </button>
      
      <!-- Bouton de connexion -->
      <router-link v-else to="/login" class="flex items-center space-x-2">
        <span>Se connecter</span>
      </router-link>


    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { HomeIcon, UserIcon, ChartBarIcon, DocumentIcon } from '@heroicons/vue/24/outline'

// Déclaration des images
const imageUrlLogo = new URL('@/assets/images/LogoNabiha.png', import.meta.url).href
const imageUrlPhoto = new URL('@/assets/images/ImageBiasr.WebP', import.meta.url).href

// Vérification si l'utilisateur est authentifié
const isAuthenticated = ref(!!localStorage.getItem('authToken'))

// Fonction de déconnexion
const logout = () => {
  localStorage.removeItem('authToken')
  isAuthenticated.value = false
  const router = useRouter()
  router.push('/login') // Rediriger vers la page connexion après la deconnexion
}
</script>
