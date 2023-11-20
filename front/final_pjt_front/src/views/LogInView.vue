<template>
  <div>
    <h1>로그인 뷰</h1>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">아이디 : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="password">비밀번호 : </label>
        <input type="password" v-model.trim="password" id="password">
      </div>
      <input type="submit">
    </form>
    <button @click="goPage('signup')">Create Account</button>
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

</style>