<template>
  <v-container>
    <CrmHeader />

    <!-- Section principale -->
    <router-view></router-view>

    <CrmFooter />
  </v-container>
</template>

<script setup>
import CrmHeader from './components/CrmHeader.vue';
import CrmFooter from './components/CrmFooter.vue';
</script>

<style>
.hero {
    background-image: url('@/assets/images/ImageBiasr.WebP');
    background-size: cover;
    background-position: center;
}
</style>
