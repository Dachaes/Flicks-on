<template>
  <div class="login-main">
    <div class="login-logo">
      <img src="@/assets/movie/movieAltImage.png" alt="" width="200">
    </div>
    <div class="create-login-page login-form">
      <form @submit.prevent="logIn" class="">
        <div>
          <label for="username" class="form-label">아이디 : </label>
          <input type="text" v-model.trim="username" id="username" class="form-input">
        </div>
        <div>
          <label for="password" class="form-label">비밀번호 : </label>
          <input type="password" v-model.trim="password" id="password" class="form-input">
        </div>
        <input type="submit" class="submit-button" value="로그인">
      </form>
      <div class="login-signup">
        <span>아직 회원이 아닌신가요 ? </span>
        <button @click="goPage('signup')">Create Account</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const username = ref(null)
const password = ref(null)


const logIn = function() {
  const payLoad = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payLoad)
}

const goPage = function (pageName) {
  router.push({name: pageName})
}

</script>

<style scoped>
.login-main{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 350px 0px;
}
.login-logo {
  margin: 0;
}
.login-logo > img {
  height: 300px;
}
.create-login-page {
  max-width: 600px;
  margin: 0;
  padding: 20px;
  color:black
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.login-form {
  width: 400px;
  height: 500px;
  background-color: #fff;
  border: 1px solid #ccc;
  /* border-radius: 5px; */
  padding: 20px;
  align-items: center;
}

.form-label {
  font-size: 16px;
  display: block;
  margin-bottom: 8px;
}

.form-select,
.form-input {
  width: 100%;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.submit-button {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-button:hover {
  background-color: #0056b3;
}
.login-signup{
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
}
</style>