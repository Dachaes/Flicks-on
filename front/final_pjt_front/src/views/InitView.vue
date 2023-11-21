<template>
  <div>
    <button @click="getMoviesInfo">버튼</button>
    <div v-for="movie in movies">
      {{ movie }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '../stores/users';
import axios from 'axios'

const userStore = useUserStore()
const movies = ref(null)

const getMoviesInfo = function () {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/api/v1/init/${userStore.userPk}/`,
    })
      .then((res) => {
        console.log(res.data)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
</script>

<style scoped>

</style>