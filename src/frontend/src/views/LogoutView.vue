<script setup>
import { onMounted } from "vue";
import axios from "axios";

onMounted(() => {
  axios.post("http://127.0.0.1:8002/api/auth/logout");

  alert("Logout sucessful!");
  console.log("Logout sucessful!");
  localStorage.removeItem("token");
  localStorage.removeItem("user_id");
  localStorage.removeItem("username");
});
</script>
