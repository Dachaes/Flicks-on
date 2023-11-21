<template>
  <div class="container">
    <div class="movie">
      <img class="movie-poster" :src="movieStore.detailMovie.poster_path" alt="poster">
      <img src="@/assets/likes/heart2.png" width="33" alt="likes"> {{ movieStore.detailMovie.vote_average }}점
    </div>
    <div class="movie-info">
      <div class="movie-title" v-if="movieStore.detailMovie.production_countries">
        <p>{{ movieStore.detailMovie.title }}</p>
        <p>{{ movieStore.detailMovie.original_title }}, <span data-start="0" data-end="5">{{ movieStore.detailMovie.release_date }}</span></p>
        <p>{{ movieStore.detailMovie.runtime }}분 / {{ movieStore.detailMovie.production_countries[0].name }}</p>
        <span v-for="genre in movieStore.detailMovie.genres" :key="genre.id">
          -{{ genre.name }}
        </span>
      </div>
      <div class="movie-detail">
        <p>{{ movieStore.detailMovie.overview }}</p>
      </div>

    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useMovieStore } from '@/stores/movies'
  
  const props = defineProps({
    tmdbId: String
  })

  const movieStore = useMovieStore()
  // console.log(movieStore.detailMovie)
  
  // const title = ref(movieStore.detailMovie.title)
  // const original_title = ref(movieStore.detailMovie.original_title)
  // const year = ref(movieStore.detailMovie.release_date)
  // year.value = year.value.slice(0, 4)
  onMounted(() => {
    movieStore.getDetailMovie(props.tmdbId)
  })

</script>

<style scoped>
  .container {
    display: flex;
    /* flex-direction: row; */

    margin-top: 10px;
  }
  
  .movie {
    width: 100%;
    display: flex;
    flex-direction: column;
  }
  .movie-poster {
    width: 100%;
  }

  .movie-info {
    margin-left: 50px;
  }
  .movie-title {
    border: 1px solid black;
    text-align: right;
  }

  .movie-title p {
    margin-bottom: 2px;
  }
  .movie-detail {
    border: 1px solid black;
  }
</style>