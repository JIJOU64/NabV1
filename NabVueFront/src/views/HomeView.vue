<template>
  <v-container
    fluid
    class="d-flex align-center justify-center"
    :style="{
      backgroundImage: 'url(' + imageUrl + ')',
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      height: '100vh'
    }"
  >
    <v-row justify="center" align="center" class="text-center">
      <v-col cols="12" md="8">
        <v-card flat>
          <v-card-title class="text-h4 white--text">
            Votre Univers Pro, Votre gestion Intuitive
          </v-card-title>
          <v-card-subtitle class="text-h6 white--text">
            Application de Bureau et Mobile Personnalisée
          </v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

// L'URL de l'image
const imageUrl = new URL('@/assets/images/ImageBiasr.WebP', import.meta.url).href;
</script>

<style scoped>
/* Ajoute des styles supplémentaires ici si nécessaire */
</style>
