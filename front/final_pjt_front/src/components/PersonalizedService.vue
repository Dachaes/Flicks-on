<template>
  <div class="recommendation-message">
    <h3 class="message">{{ userStore.userNickName }} 님을 위한 맞춤 추천이에요!</h3>
    <div class="detail-analysis">
      <h4 class="detail-message" @click="analysisUser">취향 분석</h4>
      <img width="25" height="25" src="https://img.icons8.com/metro/26/FFFFFF/long-arrow-right.png" alt="long-arrow-right"/>
    </div>
  </div>

  <div class="movies-container"  v-if="userRecommendList">
    <div class="movies" v-for="movie in userRecommendList" :key="movie.id">
      <div v-if="movie.poster_path === null">
        <img class="movie-poster" @click="goPage(movie.tmdb_id)"
      src="@/assets/movie/movieAltImage.png" alt="movie_poster">
      </div>
      <div v-else>
        <img class="movie-poster" @click="goPage(movie.tmdb_id)" :src="movie.poster_path" alt="movie_poster">
      </div>
      <p class="movie-title">{{ movie.title }}</p>
      <div class="movie-rating">
        <img class="movie-heart" src="@/assets/likes/heart2.png" width="17" alt="">
        <p class="movie-rate">{{ movie.movie_rate }}</p>
      </div>
    </div>
  </div>
  <div v-else>
    <p>로딩중</p>
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

  .recommendation-message {
    margin-top: 60px;
    margin-left: 3%;
    margin-right: auto;
    margin-bottom: -10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .detail-analysis {
    display: flex;
    align-items: center;
  }

  .detail-analysis img {
    margin: 0 10px 10px;

  }
  .movies-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px;
  }

  .movies {
    margin: 10px;
    padding: 10px;
    background-color: #1f1f1f;
    border-radius: 10px;
    text-align: center;
    width: 197px;
    height: 410px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }

  .movie-poster {
    width: 100%;
    height: 280px;
    object-fit: cover;
    cursor: pointer;
  }

  .movie-poster:hover {
    width: 100%;
    height: 280px;
    object-fit: cover;
    opacity: 0.5;
  }

  .movie-title {
    font-size: 18px;
    margin: 5px 0px 10px;
  }

  .movie-title:hover {
    font-size: 18px;
    margin: 5px 0px 10px;
    opacity: 0.5;
  }

  .movie-rating {  
    display: flex;
    position: absolute;
    align-items: center;
    justify-content: space-between;
    margin: 365px 0px 0px;
  }

  .movie-heart {
    width: 17px;
    height: 17px;
    margin: 6px 6px 17px;
  }

  .movie-rate {
    font-size: 16px;
    font-weight: bold;
    color: rgb(170, 170, 170);
  }
</style>