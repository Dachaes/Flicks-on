<template>
  <div class="movies-container">
    <div class="movies"
    v-for="movie in movieStore.similarMovie" :key="movie.id">
      <div v-if="movie.poster_path === null">
        <img class="movie-poster"
      src="@/assets/movie/movieAltImage.png" alt="movie_poster">
      </div>
      <div v-else>
        <img class="movie-poster"
        :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="movie_poster">
        <router-view :key="route.fullPath" />
      </div>
      <p class="m-0 p-0">{{ movie.title }}</p>
      <img src="@/assets/likes/heart2.png" width="17" alt="">{{ movie.vote_average }}
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, watch } from 'vue'
  import { useRouter } from 'vue-router'
  import { useMovieStore } from '@/stores/movies'

  import { useRoute } from 'vue-router'
  
  const props = defineProps({
    tmdbId: String
  })

  const route = useRoute()
  // const tmdb_id = ref(route.params.title)

  const router = useRouter()
  const movieStore = useMovieStore()
  movieStore.getSimilarMovie(props.tmdbId)

</script>

<style scoped>

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