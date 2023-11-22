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
      </div>
      <p class="movie-title">{{ movie.title }}</p>
      <div class="movie-rating">
        <img class="movie-heart" src="@/assets/likes/heart2.png" width="17" alt="">
        <p class="movie-rate">{{ movie.vote_average }}</p>
      </div>
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
    font-weight: bold;
    margin: 5px 0px 10px;
  }

  .movie-title:hover {
    font-size: 18px;
    font-weight: bold;
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