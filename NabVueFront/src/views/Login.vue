<template>
  <div class="flex items-center justify-center min-h-screen bg-gradient-to-r from-blue-500 to-indigo-600">
    <div class="w-full max-w-md p-8 bg-white rounded-2xl shadow-lg">
      <h2 class="text-2xl font-bold text-center text-gray-700 mb-6">Login</h2>
      
      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Username</label>
          <input v-model="username" type="text" class="mt-1 w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500" required>
        </div>
        
        <div>
          <label class="block text-sm font-medium text-gray-700">Password</label>
          <input v-model="password" type="password" class="mt-1 w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500" required>
        </div>
        
        <button type="submit" class="w-full py-3 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700 transition duration-300">
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuth } from '@/stores/auth';
//import axios from 'axios'

const username = ref('');
const password = ref('');
const auth = useAuth();
const router = useRouter();

const handleLogin = async () => {
  const isAuthenticated = await auth.handleLogin(username.value, password.value);
  if (isAuthenticated) {
    router.push('/');
  } else {
    alert("Utilisateur ou mot de passe invalide, veuillez recommecer")
  }
};
/*
const handleLogin = async () => {
await auth.authenticate(username.value, password.value);  // Attendre que l'authentification soit terminée
console.log("Utilisateur connecté: ", auth.user);

if (auth.user) {
  // Ajout  du token d'accès pour toutes les autres requêtes
  axios.defaults.headers.common['Authorization'] = `Bearer ${auth.accessToken}`
  router.push('/'); // Rediriger vers la page d'accueil
} else {
  alert("Utilisateur ou mot de passe invalide, veuillez recommencer")
}
};*/
</script>
