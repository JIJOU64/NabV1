<template>
    <section class="section">
      <div class="container">
        <h1 class="text-center text-3xl font-semibold mb-4">Informations sur le client</h1>
        <h2 class="text-center text-xl text-gray-600 mb-8">Détails du client sélectionné</h2>
  
        <!-- Carte de présentation des données -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div class="card bg-white p-4 shadow-md rounded-lg">
            <header class="text-lg font-medium border-b pb-2 mb-4">
              Informations Utilisateur
            </header>
            <div class="content">
              <p><strong>ID Utilisateur :</strong> {{ dataClient.id_user }}</p>
              <p><strong>Nom :</strong> {{ dataClient.first_name }} {{ dataClient.last_name }}</p>
              <p><strong>Numéro de téléphone :</strong> {{ dataClient.phone_number }}</p>
              <p><strong>Adresse :</strong> {{ dataClient.address }}</p>
              <p><strong>Email :</strong> {{ dataClient.email }}</p>
            </div>
          </div>
  
          <div class="card bg-white p-4 shadow-md rounded-lg">
            <header class="text-lg font-medium border-b pb-2 mb-4">
              Informations Client
            </header>
            <div class="content">
              <p>
                <strong>ID Client :</strong>
                {{ dataClient.id_client_clients_data?.id_client || 'Non configuré' }}
              </p>
              <p>
                <strong>Date de création :</strong>
                {{ formatDateFrench(dataClient.id_client_clients_data?.file_creation_date) }}
              </p>
  
              <p>
                <strong>Date de clôture :</strong>
                {{ formatDateFrench(dataClient.id_client_clients_data?.file_closing_date) }}
              </p>
              <p>
                <strong>Avancement du client :</strong>
                {{
                  dataClient.id_client_clients_data?.id_progress_client_progress?.name_progress ||
                  'Non configuré'
                }}
              </p>
            </div>
          </div>
  
          <div class="card bg-white p-4 shadow-md rounded-lg">
            <header class="text-lg font-medium border-b pb-2 mb-4">
              Informations sur la formation
            </header>
            <div class="content">
              <p>
                <strong>Financement par CPF :</strong>
                {{
                  dataClient.id_client_clients_data?.id_training_training_data?.follow_edof ||
                  'Non configuré'
                }}
              </p>
              <p><strong>Début du bilan :</strong> Non configuré</p>
              <p><strong>Fin du bilan :</strong> Non configuré</p>
              <p>
                <strong>Nombre d'heures :</strong>
                {{
                  dataClient.id_client_clients_data?.id_training_training_data?.number_hours ||
                  'Non configuré'
                }}
              </p>
              <p><strong>Coût de la formation :</strong> Non configuré</p>
              <p><strong>Nombre de stagiaires :</strong> Non configuré</p>
              <p><strong>Nom du statut :</strong> Non configuré</p>
              <p><strong>Nom de la formation :</strong> Non configuré</p>
              <p><strong>Mode :</strong> Non configuré</p>
            </div>
          </div>
  
          <div class="card bg-white p-4 shadow-md rounded-lg">
            <header class="text-lg font-medium border-b pb-2 mb-4">
              Suivi après formation
            </header>
            <div class="content">
              <p>
                <strong>Fiche d'évaluation :</strong>
                {{
                  dataClient.id_client_clients_data?.id_training_training_data
                    ?.followupafter_set?.[0]?.evaluation_sheet || 'Non configuré'
                }}
              </p>
              <p><strong>Date prévue pour l'évaluation :</strong> Non configuré</p>
              <p><strong>Date réelle de l'évaluation :</strong> Non configuré</p>
              <p><strong>Intervalle :</strong> Non configuré</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { useUrlStore } from '@/stores/urlAxios'
  import axios from 'axios'
  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useAuth } from '@/stores/auth'
  
  // Accès à la route actuelle pour récupérer les paramètres
  const route = useRoute()
  // Pour changer de page
  const router = useRouter()
  
  console.log('Bienvenue dans la configuration de ClientData')
  // Variable réactive pour stocker les données du client sélectionné
  const selectedClient = ref(null)
  const dataClient = ref({}) // Stocker les données du client
  const error = ref(false) // Pour afficher une erreur en cas de problème avec la requête
  const auth = useAuth()

  // Fonction pour récupérer les données du client choisi crmapp/api/user-profiles/<int:pk>/
  const fetchDataClient = async (userId) => {
    try {

      const accessToken = auth.accessToken
      if (!accessToken) {
        router.push('/login')
      }
      const urlStore = useUrlStore()
      const baseUrl = urlStore.baseUrl
  
      // Récupération des données du client choisi depuis l'API DRF
      const response = await axios.get(`${baseUrl}/api/user-profile/${userId}`)
  
      // Log de la réponse pour vérifier son contenu
      console.log('Réponse de l\'API:', response.data)
  
      dataClient.value = response.data
    } catch (err) {
      console.error('Erreur lors de la récupération des clients :', err)
      error.value = true // Affichage du message d'erreur si la requête échoue
    }
  }
  
  // Monté du composant
  onMounted(() => {
    // On récupère le paramètre de la query string
    selectedClient.value = route.query.chosen_client
    console.log(`Valeur reçue selectedClient.value : ${selectedClient.value}`)
    // Vérifiez si selectedClient a une valeur valide avant d'effectuer une requête
    if (selectedClient.value) {
      fetchDataClient(selectedClient.value)
    } else {
      console.warn('Aucun choix utilisateur trouvé dans les paramètres de la requête.')
    }
  })
  
  // Méthode pour formater une date
  const formatDateFrench = (dateStr) => {
    if (!dateStr) return 'Non configuré'
  
    const options = { year: 'numeric', month: 'long', day: 'numeric' }
    const date = new Date(dateStr)
    return date.toLocaleDateString('fr-FR', options)
  }
  </script>
  
  <style scoped>
  /* Si nécessaire, vous pouvez ajouter des styles personnalisés ici */
  </style>
  