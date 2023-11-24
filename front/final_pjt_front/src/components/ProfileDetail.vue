<template>
  <!-- <div v-if="posterImage1" class="image-box">
    <img :src="posterImage1" class="image" alt="">
  </div> -->
  <div class="profile-container">
    <div class="blank"></div>
    <p class="edit" @click="edit">Edit Profile</p>
    <p class="logout" @click="logOut">Log Out</p>
    <p class="signout" @click="SignOut">Sign Out</p>
  </div>
  
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useUserStore } from '../stores/users';
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

const logOut = function () {
  userStore.logOut()
}

// const posterImage1 = ref(userStore.userRecommendList[15].poster_path)

const edit = function () {
  router.push({name:'edit'})
}

onMounted(() => userStore.getUserDetail())

</script>

<style scoped>
  /* .user {
    display: flex;
    position: relative;
    justify-content: center;
    align-items: center;
  } */
  .profile-container {
    display: flex;
    flex-direction: column;

    height: 400px;
    text-align: end;
    margin-top: 10px;
    margin-bottom: 100px;
    background-image: url('../assets/banner/img6.png');
    background-size: cover;
    background-position: center;
    opacity: 0.78;
  }
  .profile-container:after {
    opacity: 0.4;
    z-index: -3;
  }
  .blank{
    height: 290px;
  }
  .edit, .logout, .signout {
    text-shadow: -1px 0px rgb(22, 22, 22);
    margin: 5px;
    padding-right: 10px;
    font-size: 20px;
    color: white;
  }

  .edit:hover, .logout:hover, .signout:hover {
    opacity: 50%;
  }

  /* .user-img {
    top: 230px;
    position: absolute;
    justify-content: center;
    width: 170px;
  } */
</style>