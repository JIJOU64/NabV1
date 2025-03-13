import { defineStore } from 'pinia'; // Ajoute cet import
import { ref } from 'vue';
import axios from 'axios';
import { useUrlStore } from './urlAxios'

export const useAuth = defineStore("auth", () => {
    const user = ref(null);
    const accessToken = ref(null);  // Pour stocker le token d'accès
    const refreshToken = ref(null); // Pour stocker le token de rafraîchissement
    const urlStore = useUrlStore()
    const baseUrl = urlStore.baseUrl

    const authenticate = async (username, password) => {
        try {
            // Envoie la requête POST pour récupérer les tokens
            const response = await axios.post(`${baseUrl}/api/token/`, {
                username,
                password
            });

            // Affiche la réponse du serveur dans la console
            console.log("Réponse du serveur :", response.data);

            // Vérifie si les tokens sont reçus
            if (response.data.access && response.data.refresh) {
                console.log("Access token :", response.data.access);
                console.log("Refresh token :", response.data.refresh);

                // Mettre à jour les valeurs du store avec les tokens et l'utilisateur
                user.value = { username };  // Met à jour le user avec le nom d'utilisateur
                accessToken.value = response.data.access;
                refreshToken.value = response.data.refresh;

                // Stockage dans localStorage
                localStorage.setItem("access_token", response.data.access);
                localStorage.setItem("refresh_token", response.data.refresh);
                
                console.log("Utilisateur connecté:", user.value);
            } else {
                console.log("Pas de tokens reçus");
            }
        } catch (error) {
            console.error("Erreur d'authentification :", error.response?.data || error.message);
        }
    };

    const logout = () => {
        user.value = null;
        accessToken.value = null;
        refreshToken.value = null;

        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");
    }

    return {
        user,
        accessToken,
        refreshToken,
        authenticate,
        logout
    };
});


