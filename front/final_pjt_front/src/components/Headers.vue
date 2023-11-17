<template>
  <div>
    <header class="header-container">
      <h1>헤더</h1>
      <img src="@/assets/logo/logo1.png"  alt="">
      <a @click="goPage('profile')">프로필 뷰</a>
    </header>
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
  .header-container {
    display: flex;
    justify-content: center;
    background-color: aqua;
    
  }

  .nav {

  
  background-color: #f1efef;
}

nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 1rem;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}
</style>