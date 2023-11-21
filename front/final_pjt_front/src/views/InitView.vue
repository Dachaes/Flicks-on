<template>
  <div>
    <button @click="getMoviesInfo">버튼</button>
    <div v-for="genre in genres" :key="genre.id">
      <button @click="selectGenres(genre.name)">{{ genre.name }}</button>
    </div>
    <div v-if="comp">
      <button>제출</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useUserStore } from '../stores/users';
import axios from 'axios'

const userStore = useUserStore()
const genres = ref(null)
const selectedGenres = ref([])

const getMoviesInfo = function () {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/api/v1/init/${userStore.userPk}/`,
    })
      .then((res) => {
        genres.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

const selectGenres = function (genreName) {
  selectedGenres.value.push(genreName)
  console.log(selectedGenres.value)
  console.log(selectedGenres.value.length)
}

const comp = computed(() => {
  return selectedGenres.value.length > 2 ? true : false
})

</script>

<style scoped>

</style>