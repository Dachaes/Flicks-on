<template>
  <div class="edit-container" v-if="userStore.userData">
    <img class="login-logo" src="@/assets/movie/movieAltImage.png" alt="" width="200">
    
    <div class="edit-form" >
      <form  @submit.prevent="updateUser">
        <h3>회원 정보 수정</h3>
        <div>
          <label for="firstname" class="form-label">Firstname : </label>
          <input type="text" id="firstname" v-model="firstName" class="form-input">
        </div>
        <div>
          <label for="lastname" class="form-label">Lastname : </label>
          <input type="text" id="lastname" v-model="lastName" class="form-input">
        </div>
        <div>
          <label for="nickname" class="form-label">Nickname : </label>
          <input type="text" id="nickname" v-model="nickName" class="form-input">
        </div>
        <div>
          <label for="email" class="form-label">Email : </label>
          <input type="text" id="email" v-model="email" class="form-input">
        </div>
        <div>
          <label for="age" class="form-label">Age : </label>
          <input type="number" id="age" v-model="age" class="form-input">
        </div>
        <input class="submit-button" type="submit" value="Edit Profile">
      </form>
    </div>
  </div>
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
.edit-container{
  position: fixed;
  top: 10%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 700px;
  height: 60%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 350px 0px;
  border-radius: 10px;
  background-color: rgb(39, 39, 39);
  padding: 10px;
  border-radius: 10px;
}

@media (max-width: 680px) {
  .edit-container{
    width: 500px;
  }
}


.login-logo {
  margin: 0;
  height: 100%;
  border-radius: 7px;
  flex: 0.5;
  margin-right: 3px;
}

h3 {
  font-size: 2rem;
  margin-bottom: 1rem;
  text-align: center;;
}

.edit-form {
  flex: 0.5;
  margin: 0;
  padding: 20px;
  color:black;
  width: 100%;
  height: 100%;
  background-color: #fff;
  border: 1px solid #ccc;
  align-items: center;
  border-radius: 7px;
}

.form-label {
  font-size: 19px;
  display: block;
  margin-bottom: 2px;
}

.form-input {
  width: 100%;
  height: 80%;
  padding: 5px;
  font-size: 18px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 5px;
}
.submit-button {
  display: block;
  width: 100%;
  margin-top: 10px;
  padding: 10px;
  font-size: 17px;
  background-color:rgb(34, 34, 34);
  color: rgb(219, 219, 219);;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.5s;
}

.submit-button:hover {
  background-color: #414141;
}
</style>