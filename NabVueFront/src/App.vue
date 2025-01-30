
<template>
  <div class="min-h-screen flex flex-col bg-gray-100 text-gray-900">
    
    <CrmHeader class="bg-blue-500 text-white p-4" />
      
    <main class="flex-grow p-6">
      <router-view />
    </main>

    <CrmFooter class="bg-gray-800 text-white p-4" />

  </div>
</template>

<script setup>
import CrmHeader from './components/CrmHeader.vue';
import CrmFooter from './components/CrmFooter.vue';
</script>

<style scoped>

</style>
