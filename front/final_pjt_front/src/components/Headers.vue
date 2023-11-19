<template>
  <div class="header-container">
    <!-- <img class="logo-img" @mouseover="convert_logo('logo2')" @mouseout="convert_logo('logo1')" @click="goMain()" :src="logoSrc" height="80" alt="logo"> -->
    <!-- <img class="logo-img"
          @mouseenter="convertLogo=true" @mouseleave="convertLogo=false"
          @click="goMain()" :src="convertLogo? './assets/logo/logo2-1.png':'./assets/logo/logo1.png'" height="80" alt="logo"> -->
    <img class="logo-img" @click="goMain()" src="@/assets/logo/logo1.png" height="80" alt="logo">

    <img class="user-img" @click="goProfile()" src="@/assets/user/anonymous_user.png" height="50" alt="logo1">
  </div>
</template>

<script setup>
  // import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { useUserStore } from '../stores/users';

  const router = useRouter()
  const userStore = useUserStore()
  // const logoSrc = ref(import.meta.glob("@/assets/logo/logo1.png"))
  // const convertLogo = ref(false) -> 2

  const goMain = () => { router.push({name: 'main'}) }
  const goProfile = () => { router.push({name: 'profile', params: {user_name: userStore.userName}}) }

  // const convert_logo = (hovered) => {
  //   if (hovered === 'logo2') {
  //     logoSrc.value = import.meta.glob("@/assets/logo/logo2-1.png")
  //   }
  //   else {
  //     logoSrc.value = import.meta.glob("@/assets/logo/logo1.png")
  //   }
  // }
</script>

<style scoped>
  .header-container {
    display: flex;
    align-items: center;
    border-bottom: 1px solid rgb(227, 227, 227);
    position: sticky;
    top: 0;
    background-color: white;
    z-index: 100;
  }

  .logo-img {
    padding-left: 65px;
    margin: auto;
  }

  .user-img {
    margin-right: 15px;
  }
</style>