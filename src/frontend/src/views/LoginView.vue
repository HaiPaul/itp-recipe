<template>
  <div class="row d-flex justify-content-center mx-auto mt-5">
    <div class="col-4 pt-6">
      <form @submit.prevent="submit">
        <div class="form-group">
          <label for="usernameField">Username</label>
          <input
            v-model="form.username"
            type="text"
            class="form-control"
            id="usernameField"
          />
        </div>
        <div class="form-group">
          <label for="passwordField">Password</label>
          <input
            v-model="form.password"
            type="password"
            class="form-control"
            id="passwordField"
          />
        </div>
        <div class="d-flex justify-content-center">
          <button type="submit" class="btn btn-primary">Login</button>
        </div>
      </form>
      <div class="d-flex justify-content-center mt-3">
        <button class="btn btn-secondary" @click="microsoftLogin">
          Login with Microsoft
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import qs from "qs";

const form = ref({
  username: "",
  password: "",
});

async function submit(event) {
  try {
    const response = await axios.post(
      "http://127.0.0.1:8002/api/auth/login",
      qs.stringify({
        username: form.value.username,
        password: form.value.password,
      }),
      {
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      }
    );

    alert("Login successful!");
    console.log("Login successful!");

    localStorage.setItem("token", response.data.access_token);

    let username = JSON.parse(
      atob(response.data.access_token.split(".")[1])
    ).username;

    localStorage.setItem("username", username);

    const user = await axios.get(
      "http://127.0.0.1:8002/api/users/name/" + username
    );
    localStorage.setItem("user_id", user.data.id);
  } catch (error) {
    console.error("Login failed:", error.response?.data || error.message);
    alert("Login failed. Please check your credentials.");
  }
}

const microsoftLogin = () => {
  window.location.href = "http://localhost:8002/api/auth/login";
};
</script>
