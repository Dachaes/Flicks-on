<template>
  <div>
    <h1>헤더</h1>
    <button @click="goPage('profile')">프로필 뷰</button>
  </div>
</template>

<script setup>
  import ProfileView from '@/views/ProfileView.vue'

  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goPage = function (pageName) {
    router.push({name: pageName, params: {user_name: 'amy'}})
  }
</script>

<style scoped>

</style>