<template>
  <div class="profile-container1">
    <p>Edit</p>
    <p>Sign Out</p>
  </div>
  <div class="profile-container2">
  </div>
</template>

<script setup>
</script>

<style scoped>
  .profile-container1 {
    display: flex;
    flex-direction: column;
    margin-top: 30px;
    padding-bottom: 30px;
    height: 300px;

    border-bottom: 1px solid rgb(227, 227, 227);
    background-color: aqua;
  }
  .profile-container1 p {
    margin: 5px;
    float: right;
  }
  .profile-container2 {
    height: 200px;
    background-color:aquamarine;
  }
</style>