<template>
    <div class="flex justify-center items-center  bg-neutral-900 p-4">
        <div class="max-w-md h-[85vh] overflow-y-auto bg-neutral-900 rounded-lg p-4 w-auto">
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
  
  const recipes = [
  { id: 1, title: 'First Item', description: 'This is the first item', username: 'user1' },
  { id: 2, title: 'Second Item', description: 'This is the second item', username: 'user2' },
  { id: 3, title: 'Third Item', description: 'This is the third item', username: 'user3' },
  { id: 4, title: 'Fourth Item', description: 'This is the fourth item', username: 'user4' },
  { id: 5, title: 'Fifth Item', description: 'This is the fifth item', username: 'user5' },
  { id: 6, title: 'Fifth Item', description: 'This is the fifth item', username: 'user5' },
  { id: 7, title: 'Fifth Item', description: 'This is the fifth item', username: 'user5' },
    // ... more items
  ];
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