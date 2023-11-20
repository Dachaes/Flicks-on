<template>
  <div class="movies-container">
    <div class="movies"
    v-for="movie in movieStore.similarMovie" :key="movie.id">
      <!-- <div v-show="movie.poster_path">
        <div v-show="movie.vote_average"> -->
          <img class="movie-poster" @click="goPage('movie_detail', tmdbId)"
          :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="movie_poster">
          <p class="m-0 p-0">{{ movie.title }}</p>
          <img src="@/assets/likes/heart2.png" width="17" alt="">{{ movie.vote_average }}
        <!-- </div>
      </div> -->
    </div>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router'
  import { useMovieStore } from '@/stores/movies'

  const props = defineProps({
    tmdbId: String
  })

  const router = useRouter()
  const movieStore = useMovieStore()
  movieStore.getSimilarMovie(props.tmdbId)
  console.log(props.tmdbId)
  const goPage = function (pageName, id) {
    router.push({name: pageName, params: {title: id}})
  }
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