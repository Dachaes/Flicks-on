<template>
  <div class="genre-container">
    <h2>선호하는 장르를 선택해주세요!</h2>
    <div class="genres">
    <div class="genre" v-for="genre in genres" :key="genre.id">
      <button class="genre-button" @click="selectGenres(genre.name)">{{ genre.name }}</button>
    </div>
  </div>
  <div class="submit" v-if="comp">
    <button class="submit-button" @click="addGenre">FINISH</button>
  </div>
</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useUserStore } from '../stores/users';
import { useRouter } from 'vue-router'
import axios from 'axios'

const userStore = useUserStore()
const router = useRouter()
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
  selectedGenres.value.includes(genreName) ? false : selectedGenres.value.push(genreName)
  console.log(selectedGenres.value)
}

const addGenre = () => {
  axios({
      method: 'post',
      url: `${userStore.API_URL}/api/v1/init/${userStore.userPk}/`,
      data:{
        selectedGenres: selectedGenres.value
      }
  })
    .then((res) => {
      console.log(res)
      router.push({name:'main'})
    })
    .catch((err) => {
      console.log(err)
    })
}

const comp = computed(() => {
  return selectedGenres.value.length > 2 ? true : false
})

onMounted(() => {
  getMoviesInfo()
})

</script>

<style scoped>
  h2 {
    margin: 15px 0;
    color: rgb(212, 212, 212);
  }
.genre-container{
  position: fixed;
  top: 10%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 700px;
  height: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 350px 0px;
  border-radius: 10px;
  background-color: rgb(39, 39, 39);
  padding: 10px;
  border-radius: 10px;
}

.genres {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
}

.genre {
  margin: 5px 10px;
}

.genre-button {
  width: 150px;
  height: 48px;
  font-size: 19px;
  padding: 5px;
  background-color: rgb(212, 212, 212);
  border: 3px solid rgb(138, 138, 138);
  border-radius: 6px; 
  cursor: pointer;
}

.genre-button:hover {
  opacity: 50%;
  transition: opacity 0.2s;
}

.submit {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.submit-button {
  margin: 15px 0;
  display: block;
  /* width: 670px; */
  width: 325px;
  margin-top: 10px;
  padding: 9px 10px 8px;
  font-size: 20px;
  background-color:rgb(34, 34, 34);
  color: rgb(219, 219, 219);;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  border: 1px solid #383838;
  border-radius: 6px;  
  cursor: pointer;
  transition: background-color 0.5s;
}

.submit-button:hover {
  background-color: #414141;
}
</style>