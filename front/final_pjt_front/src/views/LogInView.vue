<template>
  <div class="login-container">
    <img class="login-logo" src="@/assets/movie/movieAltImage.png" alt="" width="200">

    <div class="login-form">
      <form @submit.prevent="logIn">
        <div>
          <label for="username" class="form-label">ID : </label>
          <input type="text" v-model.trim="username" id="username" class="form-input">
        </div>
        <div>
          <label for="password" class="form-label">Password : </label>
          <input type="password" v-model.trim="password" id="password" class="form-input">
        </div>
        <input type="submit" class="submit-button" value="Log In">
      </form>

      <div class="login-signup">
        <span class="signup-message">아직 회원이 아니신가요 ? </span>
        <button class="signup" @click="goPage('signup')">Join Us!</button>
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
  .signup-message {
    display: none;
    padding-right: 0px;

  }
}

.login-logo {
  margin: 0;
  height: 100%;
  border-radius: 7px;
  flex: 0.5;
  margin-right: 3px;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
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
  transition: background-color 0.5s;
}

.submit-button:hover {
  background-color: #414141;
}

.login-signup{
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
}

.signup {
  color: rgb(219, 219, 219);
  border-radius: 5px;
  padding: 0 15px;
  background-color: rgb(34, 34, 34);
  transition: background-color 0.5s;
}

.signup:hover {
  background-color: #333;
}
</style>