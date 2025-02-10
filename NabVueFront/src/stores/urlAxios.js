import { defineStore } from 'pinia'

export const useUrlStore = defineStore('url', {
  state: () => ({
    baseUrl: 'http://127.0.0.1:8000'
  })
})