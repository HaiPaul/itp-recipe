<template>
  <div class="flex justify-center items-center bg-neutral-900 p-4 h-screen">
    <div class="w-full max-w-3xl overflow-y-auto bg-neutral-900 rounded-lg p-6 h-full">
      <RecipeCard 
        v-for="recipe in recipes" 
        :key="recipe.id" 
        :recipe="recipe"
        class="mb-4 last:mb-0"
      />
    </div>
  </div>
</template>
  
<script setup>
  import RecipeCard from '../components/RecipeCard.vue';
  import { ref, onMounted } from 'vue';
  import axios from 'axios';

  

  const recipes = ref([]);


const getAllRecipes = async () => {
    let token = localStorage.getItem("token")
    axios.get("http://127.0.0.1:5001/api/recipes", {
      headers: {
        "Authorization": `Bearer ${token}`
      }
    })
    .then(res => {
      this.recipes = res.data
    })
    .error(err => {
      console.error(err)
    })
};

onMounted(getAllRecipes);
  


  </script>

<style scoped>
.overflow-y-auto::-webkit-scrollbar {
  width: 8px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  border-radius: 4px;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background: transparent;
  border-style: solid;
  border-width: 2px;
  border-color: rgb(68, 68, 68);
  border-radius: 4px;
}

.overflow-y-auto::-webkit-scrollbar-thumb:hover {
  background: rgb(68, 68, 68);
}
</style>

