<template>
  <v-main app fluid>
    <!-- Ajout de la classe d-flex pour utiliser flexbox, justify-center pour centrer horizontalement, et align-center pour centrer verticalement -->
    <v-container fluid class="d-flex justify-center align-center" style="min-height: 100vh;">
      <v-card>
        <v-card-title class="text-h4 white--text text-center">
          Votre Univers Pro, Votre gestion Intuitive
        </v-card-title>
        <v-card-subtitle class="text-h6 white--text text-center">
          Application de Bureau et Mobile Personnalisée
        </v-card-subtitle>
        
      </v-card>
      
      
    </v-container>
  </v-main>
</template>


<!--
<template>
  <v-main app fluid>
    <div
      class="d-flex justify-center align-center"
      style="height: 100vh; width: 100%;"
    >
      <img
        :src="imageUrl"
        alt="Logo"
        style="max-width: 100%; max-height: 100%; object-fit: cover;"
      />
    </div>
  </v-main>
</template>




<template>
  <v-main app
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
      <v-col cols="12">
        <v-card-title class="text-h4 white--text">
          Votre Univers Pro, Votre gestion Intuitive
        </v-card-title>
        <v-card-subtitle class="text-h6 text-white">
          Application de Bureau et Mobile Personnalisée
        </v-card-subtitle>
      </v-col>
    </v-row>
  </v-main>
</template>


-->

<script setup>
// L'URL de l'image
const imageUrl = new URL('@/assets/images/ImageBiasr.WebP', import.meta.url).href;
</script>

<style scoped>
/* Aucune modification CSS nécessaire ici, tout est dans les propriétés inline */
</style>
