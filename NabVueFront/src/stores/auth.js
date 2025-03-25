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

    const refreshAccessToken = async () => {
        if (!refreshToken.value) {
            console.error("Aucun refresh token disponible.");
            logout();
            return;
        }
        try {
            const response = await axios.post(`${baseUrl}/api/token/refresh/`, {
                refresh: refreshToken.value
            });
            accessToken.value = response.data.access;
            localStorage.setItem("access_token", response.data.access);
            console.log("Access token rafraichi :", accessToken.value);
        } catch (error) {
            console.error("Erreur lors du rafraîchissement du token :", error.response?.data);
            logout();
        }
    }

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
                console.log("Les tokens ne sont pas retournés par l'API");
            }
        } catch (error) {
            console.error("Erreur d'authentification :", error.response?.data || error.message);
        }
    };

    const handleLogin = async (username, password) => {
        await authenticate(username, password);
        if (accessToken.value) {
            axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken.value}`;
            console.log("Utilisateur connecté:" , user.value);
            return true;
        } else {
            return false;
        }
    };

    // Pour vérifier si l'access token est valide, sinon on utilise le refresh token
    const checkTokenValidity = async () => {
        if (!accessToken.value) return;
        
        const currentTime = Math.floor(Date.now() / 1000); // Temps actuel en secondees
        const decodeAccessToken = decodeJwt(accessToken.value); // Décode le token JWT pour vérifier son expériration

        //Si l'access token est expiré, on utilise le refresh token pour en obtenir un nouveau
        if (decodeAccessToken && decodeAccessToken.exp < currentTime) {
            console.log("Accès token expiré, tentative de rafraichissement...");
            await refreshAccessToken();
        } else {
            console.log("Access token valide.");
        }
    };

    axios.interceptors.response.use(
        response => response, 
        async error => {
            if (error.response && error.response.status === 401) {
                console.log("Erreur 401 détectée, tentative de rafraîchissement du token...");

                await refreshAccessToken();

                if (accessToken.value) {
                    // Réessaie la requête avec le nouveau token
                    error.config.headers['Authorization'] = `Bearer ${accessToken.value}`;
                    return axios(error.config);

                }
            }
            return Promise.reject(error);
        }
    );

    // Fonction de décodage du JWT pour obtenir les informations (notamment l'expiration)

    const decodeJwt = (token) => {
        try {
            const base64Url = token.split('.')[1];
            const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));
            return JSON.parse(jsonPayload);
        } catch (e) {
            return null;
        }
    };

    

    const logout = () => {
        user.value = null;
        accessToken.value = null;
        refreshToken.value = null;

        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");

        delete axios.defaults.headers.common['Authorization'];

        console.log("utilisateur déconnecté");
    };

    return {
        user,
        accessToken,
        refreshToken,
        authenticate,
        handleLogin,
        logout,
        checkTokenValidity
    };
});


