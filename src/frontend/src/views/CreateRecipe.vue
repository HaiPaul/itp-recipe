<template>
  <div class="flex justify-center items-center bg-neutral-900 p-4 h-screen">
    <div class="w-full max-w-3xl bg-neutral-800 rounded-lg p-6">
      <h2 class="text-white text-lg mb-4">Neues Rezept erstellen</h2>
      <form @submit.prevent="createRecipe">
        <div class="mb-4">
          <label class="text-white block">Titel</label>
          <input
            v-model="recipe.title"
            class="w-full p-2 rounded bg-neutral-700 text-white"
          />
        </div>

        <div class="mb-4">
          <label class="text-white block">Beschreibung</label>
          <textarea
            v-model="recipe.description"
            class="w-full p-2 rounded bg-neutral-700 text-white"
          ></textarea>
        </div>

        <div class="mb-4">
          <label class="text-white block">Anweisungen</label>
          <textarea
            v-model="recipe.instructions"
            class="w-full p-2 rounded bg-neutral-700 text-white"
          ></textarea>
        </div>

        <div class="mb-4">
          <label class="text-white block">Zutaten</label>
          <div
            v-for="(ingredient, index) in recipe.ingredients"
            :key="index"
            class="flex gap-2 mb-2"
          >
            <input
              v-model="ingredient.name"
              placeholder="Zutat"
              class="w-1/2 p-2 rounded bg-neutral-700 text-white"
            />
            <input
              v-model="ingredient.quantity"
              placeholder="Menge"
              class="w-1/2 p-2 rounded bg-neutral-700 text-white"
            />
            <button
              type="button"
              @click="removeIngredient(index)"
              class="text-red-500"
            >
              &times;
            </button>
          </div>
          <button type="button" @click="addIngredient" class="text-green-400">
            + Zutat hinzufügen
          </button>
        </div>

        <button type="submit" class="bg-blue-500 text-white p-2 rounded w-full">
          Rezept erstellen
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const recipe = ref({
  title: "",
  description: "",
  instructions: "",
  ingredients: [],
  created_by: Number(localStorage.getItem("user_id")),
});

const addIngredient = () => {
  recipe.value.ingredients.push({ name: "", quantity: "" });
};

const removeIngredient = (index) => {
  recipe.value.ingredients.splice(index, 1);
};

const createRecipe = async () => {
  let token = localStorage.getItem("token");
  try {
    const response = await axios.post(
      "http://127.0.0.1:8002/api/recipes",
      recipe.value,
      {
        headers: { Authorization: `Bearer ${token}` },
      }
    );
    alert("Rezept erfolgreich erstellt!");
  } catch (error) {
    console.error(
      "Fehler beim Erstellen des Rezepts:",
      error.response?.data || error.message
    );
    alert("Fehler beim Erstellen des Rezepts");
  }
};
</script>
