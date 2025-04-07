<template>
  <div class="flex justify-center bg-neutral-900 p-4 min-h-screen items-start">
    <div
      class="w-full max-w-3xl bg-neutral-800 rounded-lg p-6 shadow-lg text-white"
    >
      <!-- Header mit Titel & Username -->
      <div
        class="flex justify-between items-center border-b border-neutral-700 pb-2 mb-4"
      >
        <h2 class="text-3xl font-bold">{{ recipe.title }}</h2>
        <div class="flex items-center space-x-2">
          <img
            src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
            alt="User Icon"
            class="w-6 h-6 rounded-full"
          />
          <span v-if="user.username" class="text-neutral-400">{{
            user.username
          }}</span>
        </div>
      </div>

      <div class="text-neutral-400 mb-4">{{ recipe.description }}</div>

      <div class="grid grid-cols-2 gap-4">
        <div class="bg-neutral-700 p-4 rounded-lg">
          <div
            class="flex justify-between items-center border-b border-neutral-600 pb-2 mb-2"
          >
            <h3 class="text-xl font-semibold">ℹ️ Ingredients:</h3>
          </div>
          <ul>
            <li
              v-for="(ingredient, index) in recipe.ingredients"
              :key="index"
              class="text-neutral-300"
            >
              • {{ ingredient.quantity }} {{ ingredient.name }}
            </li>
          </ul>
        </div>

        <div class="bg-neutral-700 p-4 rounded-lg">
          <div
            class="flex justify-between items-center border-b border-neutral-600 pb-2 mb-2"
          >
            <h3 class="text-xl font-semibold">🧮 Instructions:</h3>
          </div>
          <ol class="list-decimal list-inside text-neutral-300">
            <li
              v-for="(step, index) in recipe.instructions
                ? recipe.instructions.split('\n')
                : []"
              :key="index"
            >
              {{ step }}
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const user = ref({});
const recipe = ref({});

const fetchRecipe = async () => {
  let token = localStorage.getItem("token");
  try {
    const response = await axios.get(
      `http://127.0.0.1:8002/api/recipes/${route.params.id}`,
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    recipe.value = response.data;

    const userRes = await axios.get(
      "http://127.0.0.1:8002/api/users/" + recipe.value.created_by
    );
    user.value = userRes.data;
  } catch (error) {
    console.error(
      "Fehler beim Abrufen des Rezepts:",
      error.response?.data || error.message
    );
  }
};

onMounted(fetchRecipe);
</script>
