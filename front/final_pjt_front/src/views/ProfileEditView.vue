<template>
  <form @submit.prevent="updateUser">
    <div v-if="userStore.userData">
      <div>
        <label for="email">email : </label>
        <input type="text" id="email" v-model="email">
      </div>
      <div>
        <label for="nickname">nickname : </label>
        <input type="text" id="nickname" v-model="nickName">
      </div>
      <div>
        <label for="firstname">firstname : </label>
        <input type="text" id="firstname" v-model="firstName">
      </div>
      <div>
        <label for="lastname">lastname : </label>
        <input type="text" id="lastname" v-model="lastName">
      </div>
      <div>
        <label for="age">age : </label>
        <input type="number" id="age" v-model="age">
      </div>
      <div>
        <label for="image">이미지 업로드 : </label>
        <input type="file" id="image" @change="handleImageChange">
      </div>
    </div>
    <input type="submit" value="수정하기">
  </form>
  <button @click="deleteUser">탈퇴하기</button>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '../stores/users';


const userStore = useUserStore()

const email = ref(userStore.userData.email)
const nickName = ref(userStore.userData.nickname)
const firstName = ref(userStore.userData.first_name)
const lastName = ref(userStore.userData.last_name)
const age = ref(userStore.userData.age)
const image = ref(null)

const handleImageChange = (event) => {
  image.value = event.target.files[0];
}

const updateUser = function () {
  const payload = {
    email: email.value,
    nickName: nickName.value,
    firstName: firstName.value,
    lastName: lastName.value,
    age:age.value,
  }
  userStore.updateUserImage(image.value)
  userStore.updateUserDetail(payload)

}

// const deleteUser = function () {
//   userStore.deleteUser()
// }

</script>

<style scoped>

</style>