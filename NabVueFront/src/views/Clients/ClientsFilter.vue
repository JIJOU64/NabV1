<template>
  <div class="client">
    <section class="section">
      <div class="container">
        <!-- Titre principal -->
        <h1 class="text-center text-3xl font-semibold mb-4">Menu Client</h1>
        <h2 class="text-center text-xl text-gray-600 mb-8">Accès au clients</h2>

        <!-- Formulaire -->
        <form @submit.prevent="handleSubmit" class="space-y-4">
          <div class="flex flex-col">
            <label for="userChoice" class="text-lg font-medium">Choisissez un filtre :</label>
            <div class="mt-2">
              <select
                v-model="userChoice"
                id="userChoice"
                name="user_choice_client"
                class="block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
              >
                <option
                  v-for="progress in progressList"
                  :key="progress.id_progress"
                  :value="progress.id_progress"
                >
                  {{ progress.name_progress }}
                </option>
              </select>
            </div>
          </div>

          <!-- Bouton de soumission -->
          <div class="flex justify-center mt-6">
            <button
              type="submit"
              class="px-6 py-3 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition"
            >
              Accéder
            </button>
          </div>
        </form>

        <!-- Message d'erreur s'il y a une erreur avec l'API -->
        <div v-if="error" class="mt-4 p-4 bg-red-100 text-red-700 border border-red-300 rounded-md">
          Une erreur est survenue lors de la récupération des clients.
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useUrlStore } from '@/stores/urlAxios'
import axios from 'axios'
import { useRouter } from 'vue-router' // Pour rediriger vers une autre page

// Variables
const error = ref(false) // Pour afficher une erreur en cas de problème avec la requête
const progressList = ref([]) // Liste des progressions clients
const userChoice = ref(null) // Stocke la sélection de l'utilisateur
const router = useRouter()

// On accède à l'URL de base
const urlStore = useUrlStore()
const baseUrl = urlStore.baseUrl

// Fonction pour récupérer les données
const fetchClientProgress = async () => {
  try {
    let nextUrl = `${baseUrl}/crmapp/api/client-progress/` // URL initiale
    const allResults = [] // Tableau pour stocker tous les résultats

    while (nextUrl) {
      const response = await axios.get(nextUrl) // Requête à l'URL actuelle
      const data = response.data
      allResults.push(...data.results) // Ajouter les résultats actuels
      nextUrl = data.next // Mettre à jour l'URL pour la page suivante (ou null si dernière page)
    }
    allResults.sort((a, b) => a.id_progress - b.id_progress)

    // Ajouter une option pour tous les clients sauf les archivés
    const excludeArchivedOption = {
      id_progress: 0, // ID personnalisé pour cette option
      name_progress: 'Tous les clients sauf archivés'
    }
    progressList.value = [excludeArchivedOption, ...allResults] // Stocker tous les résultats
  } catch (err) {
    console.error('Erreur lors de la récupération des données :', err)
    error.value = true // Afficher un message d'erreur si nécessaire
  }
}

// Fonction de soumission du formulaire
const handleSubmit = () => {
  error.value = false // Réinitialisation de l'erreur avant chaque nouvelle requête
  try {
    // Redirection des donnés avec state
    router.push({
      path: '/client/choice',
      query: { user_choice_client: userChoice.value }
    })
  } catch (error) {
    console.error('Erreur lors de la soumission', error)
    error.value = true // Afficher le message d'erreur si la requête échoue
  }
}

// Appeler la fonction lorsqu'on monte le composant
onMounted(() => {
  fetchClientProgress()
})
</script>

<style scoped>
/* Si nécessaire, vous pouvez ajouter des styles personnalisés ici */
</style>

  
