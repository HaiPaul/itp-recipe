<template>
  <header>
    <nav class="bg-neutral-700 text-white shadow-md">
      <div class="container mx-auto p-3">
        <div class="flex justify-between items-center">
          <!-- Logo -->
          <router-link class="text-4xl font-bold" to="/browse"
            >ITP-Recipe</router-link
          >

          <!-- Mobile Menu Button -->
          <button
            @click="isMenuOpen = !isMenuOpen"
            class="md:hidden text-white focus:outline-none"
          >
            <svg
              class="w-6 h-6"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16m-7 6h7"
              ></path>
            </svg>
          </button>

          <!-- Desktop Navigation Links -->
          <div
            class="hidden md:flex md:items-center md:justify-center flex-grow"
          >
            <ul class="flex space-x-6 text-xl">
              <li>
                <router-link class="hover:text-gray-300 transition" to="/browse"
                  >Browse</router-link
                >
              </li>
              <li>
                <router-link class="hover:text-gray-300 transition" to="/create"
                  >Create</router-link
                >
              </li>
              <li>
                <router-link
                  class="hover:text-gray-300 transition"
                  to="/myRecipes"
                  >My Recipes</router-link
                >
              </li>
              <li>
                <router-link class="hover:text-gray-300 transition" to="/logout"
                  >Logout</router-link
                >
              </li>
              <li>
                <router-link class="hover:text-gray-300 transition" to="/login"
                  >Login</router-link
                >
              </li>
            </ul>
          </div>
        </div>

        <!-- Mobile Navigation Links -->
        <div
          v-show="isMenuOpen"
          class="md:hidden mt-3 transition-all duration-300 ease-in-out"
        >
          <ul class="flex flex-col items-center space-y-3 text-lg">
            <li>
              <router-link class="hover:text-gray-300 transition" to="/browse"
                >Browse</router-link
              >
            </li>
            <li>
              <router-link class="hover:text-gray-300 transition" to="/create"
                >Create</router-link
              >
            </li>
            <li>
              <router-link
                class="hover:text-gray-300 transition"
                to="/myRecipes"
                >My Recipes</router-link
              >
            </li>
            <li>
              <router-link class="hover:text-gray-300 transition" to="/logout"
                >Logout</router-link
              >
            </li>
            <li>
              <router-link class="hover:text-gray-300 transition" to="/login"
                >Login</router-link
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from "vue";

const isMenuOpen = ref(false); // Controls mobile menu toggle
</script>

<style scoped>
a {
  cursor: pointer;
}
</style>
