<template>
  <div class="box">
    <div v-if="posterImage1" class="image-back">
      <img :src="posterImage1" alt="">
      <!-- <img :src="posterImage2" alt=""> -->
      <!-- <img :src="posterImage3" alt=""> -->
    </div>
  </div>
  <div class="user">
    <!-- <img class="user-img" src="@/assets/user/anonymous_user.png" alt="user"> -->
  </div>
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

const posterImage1 = ref(userStore.userRecommendList[15].poster_path)
// const posterImage1 = ref('../assets/movie/movieAltImage.png')
const posterImage2 = ref(userStore.userRecommendList[16].poster_path)
// const posterImage2 = ref('../assets/movie/movieAltImage.png')
const posterImage3 = ref(userStore.userRecommendList[17].poster_path)
// const posterImage3 = ref('../assets/movie/movieAltImage.png')

const edit = function () {
  router.push({name:'edit'})
}

onMounted(() => userStore.getUserDetail())

</script>

<style scoped>
  .box {
    position: absolute;
    height: 400px;
    clip: rect(0 0 50% 0);
  }
  .image-back{
    position: absolute;
    left: 20%;
    bottom: 100%;
    height: 400px;
    z-index: -2;
    opacity: 40%;
  }
  .user {
    display: flex;
    position: relative;
    justify-content: center;
    align-items: center;
  }
  .profile-container {
    display: flex;
    flex-direction: column;

    height: 400px;
    text-align: end;
    margin-top: 10px;
    margin-bottom: 250px;
    /* background-image: linear-gradient(0deg, rgb(20, 20, 20) 0%, #454545 100%); */
    /* background-color:  #333; */
  }
  .blank{
    height: 250px;
  }
  .edit, .logout, .signout {
  margin: 5px;
  padding-right: 10px;
  }

  .edit:hover, .logout:hover, .signout:hover {
    opacity: 50%;
  }


  .user-img {
    top: 230px;
    position: absolute;
    justify-content: center;
    width: 170px;
  }
</style>