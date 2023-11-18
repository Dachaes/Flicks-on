<template>
  <div>
    <h1>사인 업 뷰</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">아이디 : </label>
        <input type="text" v-model.trim="username" id="username">
      </div>
      <div>
        <label for="nickname">닉네임 : </label>
        <input type="text" v-model.trim="nickname" id="nickname">
      </div>
      <div>
        <label for="password1">비밀번호 : </label>
        <input type="password" v-model.trim="password1" id="password1">
      </div>
      <div>
        <label for="password2">비밀번호 확인 : </label>
        <input type="password" v-model.trim="password2" id="password2">
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

</style>