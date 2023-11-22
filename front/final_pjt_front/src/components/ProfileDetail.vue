<template>
  <div class="user">
    <img class="user-img" src="@/assets/user/anonymous_user.png" alt="user">
  </div>
  <div class="profile-container">
    <div class="blank"></div>
    <p class="edit" @click="edit">Edit Profile</p>
    <p class="logout" @click="logOut">Log Out</p>
    <p class="signout" @click="SignOut">Sign Out</p>
  </div>

</template>

<script setup>
import { onMounted } from 'vue';
import { useUserStore } from '../stores/users';
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const router = useRouter()

const logOut = function () {
  userStore.logOut()
}

const edit = function () {
  router.push({name:'edit'})
}

onMounted(() => userStore.getUserDetail())

</script>

<style scoped>
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
    background-image: linear-gradient(0deg, rgb(20, 20, 20) 0%, #454545 100%);
    background-color:  #333;
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