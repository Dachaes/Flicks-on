<template>
  <Headers />
  <div class="movies-container">
    <div class="movies"
    v-for="movie in movieStore.searchMovie" :key="movie.id">
      <div v-if="movie.poster_path === null">
        <img class="movie-poster" @click="goPage('movie_detail', movie.id)"
      src="@/assets/movie/movieAltImage.png" alt="movie_poster">
      </div>
      <div v-else>
        <img class="movie-poster" @click="goPage('movie_detail', movie.id)"
        :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="movie_poster">
      </div>
      <p class="m-0 p-0">{{ movie.title }}</p>
      <img src="@/assets/likes/heart2.png" width="17" alt="">{{ movie.vote_average }}
    </div>
  </div>
  <Footers />
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Footers from '@/components/Footers.vue'

  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useMovieStore } from '@/stores/movies'

  const route = useRoute()
  const router = useRouter()
  const query = ref(route.params.query)
  
  const movieStore = useMovieStore()
  movieStore.getSearchMovie(query.value)

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