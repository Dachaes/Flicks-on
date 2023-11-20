<template>
  <div class="user">
    <img class="user-img" src="@/assets/user/anonymous_user.png" alt="user">
  </div>
  <div class="profile-container1">
    <div class="blank"></div>
    <p class="edit" @click="edit">Edit</p>
    <p class="sign-out" @click="logOut">Log Out</p>
  </div>
  <div class="profile-container2">
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
  .profile-container1 {
    display: flex;
    flex-direction: column;

    height: 300px;
    text-align: end;

    border-bottom: 1px solid rgb(227, 227, 227);
    background-color: rgb(187, 252, 252);
  }
  .blank{
    height: 250px;
  }
  .edit {
  margin: 5px;
  padding-right: 10px;
  }

  .sign-out {
    margin: 5px;
    padding-right: 10px;
  }

  .profile-container2 {
    height: 200px;
  }

  .user-img {
    top: 230px;
    position: absolute;
    justify-content: center;
    width: 130px;
  }
</style>