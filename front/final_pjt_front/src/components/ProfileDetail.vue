<template>
  <div class="user">
    <img class="user-img" src="@/assets/user/anonymous_user.png" alt="user">
  </div>
  <div class="profile-container1">
    <div class="blank"></div>
    <p class="edit">Edit</p>
    <p class="sign-out">Sign Out</p>
  </div>
  <div class="profile-container2">
  </div>
</template>

<script setup>
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

    height: 330px;
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
    top: 250px;
    position: absolute;
    justify-content: center;
    width: 140px;
  }
</style>