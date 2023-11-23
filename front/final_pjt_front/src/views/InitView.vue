<template>
  <div class="genre-container">
    <h2>선호하는 장르를 선택해주세요!</h2>
    <div class="genres">
    <div class="genre" v-for="genre in genres" :key="genre.id">
      <button class="genre-button" @click="selectGenres(genre)">{{ genre.name }}</button>
      <div v-if="genre.showModal" class="modal">
        <div class="genre-score">
          <span class="close" @click="closeModal(genre)">&times;</span>
          <h3>{{ genre.name }} 장르를 얼마나 좋아하세요?</h3>
          <input class="genre-score-input" type="number" @keyup.enter="closeModal(genre, genre.name)" v-model="genre.score">
          {{ genre['name'].score }}
        </div>
      </div>
    </div>
  </div>
  <div class="submit" v-if="cnt > 2">
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
const selectedGenres = ref({
  'Action': 0, 'Adventure': 0, 'Animation': 0, 'Comedy': 0,
  'Crime': 0, 'Documentary': 0, 'Drama': 0, 'Family': 0,
  'Fantasy': 0, 'History': 0, 'Horror': 0, 'Music': 0,
  'Mystery': 0, 'Romance': 0, 'Science Fiction': 0, 'TV Movie': 0,
  'Thriller': 0, 'War': 0, 'Western': 0
})
const cnt = ref(0)

const getMoviesInfo = function () {
    axios({
      method: 'get',
      url: `${userStore.API_URL}/api/v1/init/${userStore.userPk}/`,
    })
      .then((res) => {
        genres.value = res.data
        genres.value.forEach((genre) => {
          genre.isSelected = false
          genre.showModal = false
          genre.score = 0
        })
      })
      .catch((err) => {
        console.log(err)
      })
  }

const selectGenres = function (genre) {
  genre.showModal = !genre.showModal
}

const closeModal = function (genre, name) {
  genre.showModal = !genre.showModal
  selectedGenres.value[name] = genre.score
  console.log(selectedGenres.value)
  cnt.value++
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

// const comp = computed(() => {
//   return selectedGenres.value.length > 2 ? true : false
// })

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
.genre-score{
  text-align: center;
  color: black;
}
.submit-button:hover {
  background-color: #414141;
}
.modal {
display: flex;
align-items: center;
justify-content: center;
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgb(237, 237, 237, 0.92);
z-index: 1;
}
.close {
position: absolute;
top: 30px;
right: 30px;
cursor: pointer;
color: rgb(30, 30, 30);
font-size: 24px;
}
.genre-score-input{
  text-align: center;
}
</style>