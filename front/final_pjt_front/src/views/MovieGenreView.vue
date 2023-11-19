<template>
  <Headers />
  <div class="movies-container" >
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
  </div>
  <div class="movies-container" >
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="movie">
      <img @click="goPage('movie_detail', 'parasite')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
  </div>
  <Footers />
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Footers from '@/components/Footers.vue'

  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goPage = function (pageName, title) {
    router.push({name: pageName, params: {title: title}})
  }

</script>

<style scoped>
  .recommendation-message{
    margin: 65px 0px 30px;
  }
  .movies-container {
    display: flex;
    justify-content: space-around;
    margin-top: 30px;
    padding: 10px 0;
  }
  .movie {
    width: 20%;
  }
  .movie-poster {
    width: 85%;
  }
</style>