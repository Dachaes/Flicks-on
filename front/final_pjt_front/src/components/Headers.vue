<template>
  <div class="header-container">
    <img class="logo-img" @click="goMain()" src="@/assets/logo/logo_dark.png" alt="logo">
    
    <div class="form">
      <input type="text" class="input" :value="query" @input="updateQuery" placeholder="무슨 영화를 찾으시나요?">
      <img @click="goSearch(query)" src="@/assets/search/search.png" alt="search">
    </div>
    <img class="user-img" @click="goProfile()" src="https://img.icons8.com/external-bearicons-glyph-bearicons/64/FFFFFF/external-User-essential-collection-bearicons-glyph-bearicons.png" alt="external-User-essential-collection-bearicons-glyph-bearicons"/>
    <!-- <img class="user-img" @click="goProfile()" src="@/assets/user/anonymous_user.png" alt="logo1"> -->
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useRouter, onBeforeRouteUpdate } from 'vue-router'
  import { useUserStore } from '../stores/users';

  const router = useRouter()
  const userStore = useUserStore()

  const goMain = () => { router.push({name: 'main'}) }
  const goProfile = () => { router.push({name: 'profile', params: {user_name: userStore.userPk}}) }

  const query = ref('')
  
  const updateQuery = function (event) {
    query.value = event.currentTarget.value
  }
  
  const goSearch = function (query) {
    router.push({name: 'search', params: { query: query } })
  }

  onBeforeRouteUpdate((to, from) => {
    query.value = to.params.query
  })
  
</script>

<style scoped>
  .header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgb(20, 20, 20);
  color: #fff;
  padding: 8px;
  border-bottom: 1px solid #333;
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo-img {
  width: 170px;
  height: auto;
  cursor: pointer;
  margin-left: -20px;
}

.logo-img:hover {
  width: 170px;
  height: auto;
  cursor: pointer;
  margin-left: -20px;
  opacity: 0.5;
}

.form {
  display: flex;
  margin-right: 20px;
}

.input {
  width: 200%;
  height: 40px;
  padding: 13px 25px 8px;
  border: 1px solid #ccc;
  border-radius: 8px;
  /* text-align: center; */
}

.input:hover {
  width: 300px;
  height: 40px;
  padding: 13px 25px 8px;
  border: 1px solid #ccc;
  border-radius: 8px;
  /* text-align: center; */
  opacity: 90%;
}

.form img {
  height: 40px;
  cursor: pointer;
  margin-left: 10px;
}
.form img:hover {
  height: 40px;
  cursor: pointer;
  margin-left: 10px;
  opacity: 0.5;
}

.user-img {
  width: 50px;
  height: auto;
  border-radius: 50%;
  cursor: pointer;
  margin-right: 5px;
}

.user-img:hover {
  width: 50px;
  height: auto;
  border-radius: 50%;
  cursor: pointer;
  margin-right: 5px;
  opacity: 0.5;
}
</style>