<template>
    <div class="ClientChoice">
      <section class="section">
        <div class="container">
          <!-- Titre principal -->
          <h1 class="text-center text-3xl font-semibold mb-4">Menu Client</h1>
          <h2 class="text-center text-xl text-gray-600 mb-8">Données du client</h2>
          <h1 :class="texterougeClass" class="text-center text-2xl mt-4">Le choix précédent est {{ userChoice }}</h1>
  
          <!-- Formulaire -->
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div class="flex flex-col">
              <label for="selectedClient" class="text-lg font-medium">Veuillez choisir un client :</label>
              <div class="mt-2">
                <select
                  v-model="selectedClient"
                  id="selectedClient"
                  name="chosen_client"
                  class="block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
                >
                  <option
                    v-for="(client, index) in clients"
                    :key="index"
                    :value="client.id_user"
                  >
                    {{ index + 1 }} - {{ client.first_name }} {{ client.last_name }} (id_user = {{ client.id_user }})
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
  import { useRoute } from 'vue-router'
  import { ref, onMounted } from 'vue'
  import { useUrlStore } from '@/stores/urlAxios'
  import axios from 'axios'
  import { useRouter } from 'vue-router' // Pour rediriger vers une autre page
  
  const texterougeClass = ref('text-red-500') // Tailwind pour la couleur rouge
  
  // Accès à la route actuelle pour récupérer les paramètres
  const route = useRoute()
  
  // Variables réactives
  const userChoice = ref(null) // Stockage de la valeur du choix de l'utilisateur
  const selectedClient = ref(null) // Stocke le client actuellement sélectionné
  const clients = ref([]) // Liste des clients filtrés
  const error = ref(false) // Pour afficher une erreur en cas de problème avec la requête
  const router = useRouter()
  
  // Fonction pour récupérer les clients selon le tri choisi
  const fetchFilterClient = async () => {
    try {
      const urlStore = useUrlStore()
      const baseUrl = urlStore.baseUrl
  
      // Récupération des clients depuis l'API DRF
      const response = await axios.get(`${baseUrl}/crmapp/api/client-filter/filter`, {
        params: { user_choice_client: userChoice.value }
      })
  
      // Log de la réponse pour vérifier son contenu
      console.log("Réponse de l'API:", response.data)
  
      // Mettre à jour la liste des clients
      clients.value = response.data
    } catch (err) {
      console.error('Erreur lors de la récupération des clients :', err)
      error.value = true // Afficher le message d'erreur si la requête échoue
    }
  }
  
  // Monté du composant
  onMounted(() => {
    // on récupère le paramètre de la query string
    userChoice.value = route.query.user_choice_client
    console.log(`Valeur reçue userChoice.value : ${userChoice.value}`)
    // Vérifiez si userChoice a une valeur valide avant d'effectuer une requête
    if (userChoice.value) {
      userChoice.value = parseInt(userChoice.value, 10) + 1 // Incrémente userChoice
      console.log(`Valeur incrémentée pour userChoice : ${userChoice.value}`)
      fetchFilterClient()
    } else {
      console.warn('Aucun choix utilisateur trouvé dans les paramètres de la requête.')
    }
  })
  
  // Fonction de soumission du formulaire
  const handleSubmit = () => {
    error.value = false // Réinitialisation de l'erreur avant chaque nouvelle requête
    try {
      // Redirection des données avec state
      router.push({
        path: '/client/data',
        query: { chosen_client: selectedClient.value }
      })
    } catch (error) {
      console.error('Erreur lors de la soumission', error)
      error.value = true // Afficher le message d'erreur si la requête échoue
    }
  }
  </script>
  
  <style scoped>
  /* Si nécessaire, vous pouvez ajouter des styles personnalisés ici */
  </style>
  