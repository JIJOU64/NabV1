<!--
<template>

  <v-app>
    <CrmHeader />
    
    //Section principale sans image de fond
    <v-main>
      <v-container fluid class="pa-0">
        <router-view></router-view> //Ceci affiche le contenu des autres pages
      </v-container>
    </v-main>

    <CrmFooter />
  </v-app>

</template>
-->
<template>
  <v-app>
    <!-- Inclure les composants CrmHeader et CrmFooter -->
    <CrmHeader />
    
    <v-main>
      <v-container fluid>
        <router-view /> <!-- Affiche le contenu des autres pages -->
      </v-container>
    </v-main>

    <CrmFooter />
  </v-app>
</template>
<script setup>
import CrmHeader from './components/CrmHeader.vue';
import CrmFooter from './components/CrmFooter.vue';
</script>

<style scoped>
/* Pas d'image de fond dans App.vue */
</style>
