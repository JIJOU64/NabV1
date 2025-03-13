import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

export const useAuth = defineStore("auth", () => {
    const user = ref(null)

    const authenticate = (username, password) => {
        if ( username ==="Jane Doe" && password === "123") {
            user.value = { username }
        } else {
            alert("Identifiants incorrects !");
        }
    }

    const logout = () => {
        user.value = null
    }

    return {
        user,
        authenticate,
        logout,
    }
})

/*
const authenticate = (username, password) => {
        if ( username ==="Jane Doe" && password === "123") {
            user.value = { username }
        } else {
            alert("Identifiants incorrects !");
        }
    }

    const logout = () => {
        user.value = null
    }

    return {
        user,
        authenticate,
        logout,
    }
*/