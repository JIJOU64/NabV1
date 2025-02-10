<template>
  <div class="min-h-screen flex flex-col">
    
    <!-- Header -->
    <CrmHeader class="bg-blue-500 text-white p-4 text-center mb-4 " />
    
    <!-- Contenu principal -->
    <main class="flex-1 bg-gray-100 p-6 min-w-full md:min-w-[1024px] ">
      <router-view />
    </main>

    <!-- Footer -->
    <CrmFooter class="bg-black text-white p-4 text-center mt-4" />
    
  </div>
</template>

<script setup>
import CrmHeader from './components/CrmHeader.vue';
import CrmFooter from './components/CrmFooter.vue';
</script>


