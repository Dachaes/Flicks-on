<template>
  <div class="personalized-container">
    <h3>{{ userStore.userNickName }} 님의 취향</h3>
    <div class="analysis">
      <h4 @click="analysisUser">취향 분석</h4>
      <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
        <path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/>
      </svg>
    </div>
  </div>
  <div class="likes">
    <div v-if="userRecommendList">
      <span v-for="movie in userRecommendList">
        <img @click="goPage(movie.tmdb_id)" :src="movie.poster_path" alt="" width="60">
        <strong>{{ movie.title }}</strong>
      </span>
    </div>
    <div v-else>
      <p>로딩중</p>
    </div>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '../stores/users';
import axios from 'axios'
import { ref, onMounted } from 'vue';

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const userRecommendList = ref(null)
  

const analysisUser = () => {
  return alert('아직 준비중이에요')
}

const getRecommendMovie = () => {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/api/v1/movies/recommend/${userStore.userPk}/`,
    data:{
      user_genre: userStore.userData.usergenre_set[0]
    }
  })
    .then((res) => {
      const uniqueMovies = removeDuplicates(res.data);
      userRecommendList.value = uniqueMovies.slice(0, 20);
    })
    .catch(err => console.log(err))
}

// Helper function to remove duplicates from an array of objects
const removeDuplicates = (array) => {
  const uniqueArray = array.filter((item, index, self) =>
    index === self.findIndex(obj => JSON.stringify(obj) === JSON.stringify(item))
  );
  return uniqueArray;
};

const goPage = (movieId) => {
  router.push({name:'movie_detail', params:{title:movieId}})
}

onMounted(() => {
  getRecommendMovie(route.params.user_name)
})

</script>

<style scoped>
  .personalized-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .analysis {
    display: flex;
    align-items: center;

  }
  .analysis svg {
    margin: 13px;
  }
  .likes {
    height: 500px;
    border-bottom: 1px solid rgb(143, 142, 142);
  }
</style>