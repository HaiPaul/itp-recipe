<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-4 pt-6">
            <form>
                <div class="form-group">
                    <label for="usernameField">Username</label>
                    <input v-model="form.username" type="text" class="form-control" id="usernameField">
                </div>
                <div class="form-group">
                    <label for="passwordField">Password</label>
                    <input v-model="form.password" type="password" class="form-control" id="passwordField">
                </div>
                <div class="d-flex justify-content-center">
                    <button type="submit" class="btn btn-primary" v-on:click="submit">Login</button>
                </div>
            </form>
            <div class="d-flex justify-content-center mt-3">
                <button class="btn btn-secondary" v-on:click="microsoftLogin">Login with Microsoft</button>
            </div>
        </div>
    </div>

</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '../store/auth';
import axios from 'axios';

const form = ref({
    username: '',
    password: ''
});

async function submit() {
    let data = {username: form.value.username, password: form.value.password}
    console.log(data)
    axios.post("http://127.0.0.1:8002/api/auth/login", data)
    .then(res => {
        alert("Login sucessful!")
        localStorage.setItem("token", res.data.access_token);
    })
};


const microsoftLogin = () => {
    window.location.href = 'http://localhost:8002/api/auth/login';
}

onMounted(() => {
    auth.refreshForLogin();
});


</script>