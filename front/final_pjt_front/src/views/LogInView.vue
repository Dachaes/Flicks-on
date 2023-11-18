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
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/users'

const store = useUserStore()
const username = ref(null)
const password = ref(null)

const logIn = function() {
  const payLoad = {
    username: username.value,
    password: password.value,
  }
  store.logIn(payLoad)
}

</script>

<style scoped>

</style>