<template>
  <form @submit.prevent="updateUser">
    <div>
      <label for="email">email : </label>
      <input type="text" id="email" v-model="email">
      <label for="nickname">nickname : </label>
      <input type="text" id="nickname" v-model="nickName">
      <label for="firstname">firstname : </label>
      <input type="text" id="firstname" v-model="firstName">
      <label for="lastname">lastname : </label>
      <input type="text" id="lastname" v-model="lastName">
    </div>
    <input type="submit" value="수정하기">
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '../stores/users';
import { useRoute, useRouter } from 'vue-router';


const userStore = useUserStore()
const router = useRouter()

email = ref('')
nickName = ref(userStore.userData.nickname)
firstName = ref(userStore.userData.first_name)
lastName = ref(userStore.userData.last_name)

const payload = {
  email: email.value,
  nickName: nickName.value,
  firstName: firstName.value,
  lastName: lastName.value,
}
const updateUser = function () {
  userStore.updateUserDetail(payload)
    .then((res) => {
      router.push({name: 'profile', params:{user_name:userStore.userPk}})
    })
}

</script>

<style scoped>

</style>