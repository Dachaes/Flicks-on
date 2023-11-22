<template>
  <div class="login-container">
    <img class="login-logo" src="@/assets/movie/movieAltImage.png" alt="" width="200">

    <div class="login-form">
      <form @submit.prevent="signUp">
        <div>
          <label for="username" class="form-label">ID : </label>
          <input type="text" v-model.trim="username" id="username" class="form-input">
        </div>
        <div>
          <label for="nickname" class="form-label">Nickname : </label>
          <input type="text" v-model.trim="nickname" id="nickname" class="form-input">
        </div>
        <div>
          <label for="password1" class="form-label">Password : </label>
          <input type="password" v-model.trim="password1" id="password1" class="form-input">
        </div>
        <div>
          <label for="password2" class="form-label">Password Confirmation : </label>
          <input type="password" v-model.trim="password2" id="password2" class="form-input">
        </div>
        <input class="submit-button" type="submit" value="Create New Account">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'

const store = useUserStore()
const username = ref(null)
const nickname = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payLoad = {
    username: username.value,
    nickname: nickname.value,
    password1: password1.value,
    password2: password2.value,
  }
  store.signUp(payLoad)
}
</script>

<style scoped>
.login-container{
  position: fixed;
  top: 10%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 700px;
  height: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 350px 0px;
  border-radius: 10px;
  background-color: rgb(39, 39, 39);
  padding: 10px;
  border-radius: 10px;
}

@media (max-width: 680px) {
  .login-container{
    width: 500px;
  }
}

.login-logo {
  margin: 0;
  height: 100%;
  border-radius: 7px;
  flex: 0.5;
  margin-right: 3px;
}


.login-form {
  flex: 0.5;
  margin: 0;
  padding: 20px;
  color:black;
  width: 100%;
  height: 100%;
  background-color: #fff;
  border: 1px solid #ccc;
  align-items: center;
  border-radius: 7px;
}

.form-label {
  font-size: 20px;
  display: block;
  margin-bottom: 2px;
}

.form-input {
  width: 100%;
  height: 80%;
  padding: 5px;
  font-size: 18px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 5px;
}

.submit-button {
  display: block;
  width: 100%;
  margin-top: 10px;
  padding: 10px;
  font-size: 16px;
  background-color:rgb(34, 34, 34);
  color: rgb(219, 219, 219);;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.submit-button:hover {
  transition: background-color 0.5s;
  background-color: #414141;
}
</style>