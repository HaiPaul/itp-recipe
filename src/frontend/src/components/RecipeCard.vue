<template>
    <div class="flex justify-center items-center  bg-neutral-900">
      <div 
        @click="goToDetailPage"
        class="w-full max-w-md bg-neutral-800 rounded-lg shadow-md overflow-hidden cursor-pointer transition-transform duration-300 ease-in-out transform hover:scale-105"
      >
        <div class="p-4">
          <div class="text-sm text-neutral-600 text-right">
            {{ recipe.username }}
          </div>
          <h2 class="text-2xl font-bold mb-2 text-white">{{ recipe.title }}</h2>
          <p class="text-white mb-4">{{ recipe.description }}</p>
          
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  
  const props = defineProps({
    recipe: {
      type: Object,
      required: true,
      validator: (obj) => {
        return obj.id && obj.title && obj.description && obj.username;
      }
    }
  });
  
  const router = useRouter();
  
  const goToDetailPage = () => {
    router.push({ name: 'RecipeDetail', params: { id: props.recipe.id } });
  };
  </script>