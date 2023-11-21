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

  const route = useRoute()
  const tmdb_id = ref(route.params.title)

  const router = useRouter()
  const movieStore = useMovieStore()
  movieStore.getSimilarMovie(tmdb_id)


  // @click="goPage('movie_detail', movie.id)"




  // console.log(props.tmdbId)
  // 코드 1.
  // const goPage = function (pageName, id) {
  //   router.push({name: pageName, params: {title: id}})
  //   router.go(0)
  // }

  // 코드 2.
  // const goPage = function (pageName, id) {
  //   // 네비게이션 가드에서 디버깅을 위해 훅을 추가
  //   router.beforeEach((to, from, next) => {
  //     console.log('Before route update', { to, from });
  //     next();
  //   });
  //   router.push({ name: pageName, params: { title: id } });
  // }

  // 코드 3.
  // const goPage = function (pageName, id, forceReload = false) {
  //   if (forceReload) {
  //     window.location.href = `#/${pageName}/${id}`
  //   } else {
  //     router.push({name: pageName, params: {title: id}})
  //   }
  // }

  // 코드 4.
  // const goPage = function (pageName, id) {
  //   router.go({name: pageName, params: {title: id}, replace: true})
  // }

  // 코드 5.
  // const goPage = function (pageName, id) {
  //   router.replace({name: pageName, params: {title: id}})
  // }

  // 코드 6.
  // const goPage = function (pageName, id) {
  //   router.replace({name: pageName, params: {title: id}})
  //   window.location.reload()
  // }

  // 코드 7
  // const goPage = function (pageName, id) {
  //   router.push({name: pageName, params: {title: id}, replace: true})
  // }

  // 코드 8
  // const goPage = function (pageName, id) {
  //   router.replace({name: pageName, params: {newId: id}})
  // }

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