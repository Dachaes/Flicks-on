<template>
  <h2 class="recommendation-message">이건 어때요?</h2>

  <div class="movies-container">
    <div class="movies"
    v-for="movie in movieStore.movieList" :key="movie.id">
      <img class="movie-poster" @click="goPage('movie_detail', movie.tmdb_id)"
      :src="`${movie.poster_path}`" alt="movie_poster">
      <p class="m-0 p-0">{{ movie.title }}</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
  </div>
  <!-- <p>{{ movieStore.movieList }}</p> -->
</template>

<script setup>
  // import MovieDetailView from '@/views/MovieDetailView.vue'

  import { useRouter } from 'vue-router'
  import { useMovieStore } from '@/stores/movies'

  const router = useRouter()
  const movieStore = useMovieStore()
  movieStore.getMovieList()

  const goPage = function (pageName, id) {
    router.push({name: pageName, params: {title: id}})
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
  .movies {
    width: 20%;
  }
  .movie-poster {
    width: 85%;
  }


</style>