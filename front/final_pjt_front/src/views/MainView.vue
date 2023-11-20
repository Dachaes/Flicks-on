<template>
  <div>
    <Headers />
    <Banner />
    <h2 class="recommendation-message">현재 상영작이에요!</h2>
    <MovieListNowPlaying />
    <h2 class="recommendation-message">유명한 작품이에요!</h2>
    <MovieListTopRated />
    <h2 class="recommendation-message">장르별로 골라 봐요!</h2>
    <MovieGroup />
    <h2 class="recommendation-message">시대별로 골라 봐요!</h2>
    <MovieGroup />
    <footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Banner from '@/components/Banner.vue'
  import MovieGroup from '@/components/MovieGroup.vue'
  import MovieListNowPlaying from '@/components/MovieListNowPlaying.vue'
  import MovieListTopRated from '@/components/MovieListTopRated.vue'
  import Footers from '@/components/Footers.vue'

  // import { ref, onBeforeMount, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  // import { useMovieStore } from '@/stores/movies'

  const router = useRouter()

  // 1.
  // const movieStore = useMovieStore()
  // movieStore.getNowPlayingMovie()
  // const nowPlayingMovieList = movieStore.nowPlayingMovie
  // console.log(nowPlayingMovieList)

  // 2.
  // const movieStore = useMovieStore()
  // const nowPlayingMovieList = ref([])
  // onBeforeMount(async () => {
  //   await movieStore.getNowPlayingMovie()
  //    nowPlayingMovieList.value = await movieStore.nowPlayingMovie
  // })

  // 3.
  // const movieStore = useMovieStore()
  // const nowPlayingMovieList = ref([])
  // const isDataLoaded = ref(false)
  // onMounted(async () => {
  //   try {
  //     // 상영작 데이터 로딩
  //     await movieStore.getNowPlayingMovie()
  //     nowPlayingMovieList.value = movieStore.nowPlayingMovie

  //     // 다른 비동기 작업이 있다면 여기에 추가 가능
  //     // 예: await movieStore.getFamousMovies()

  //     // 데이터 로딩 완료
  //     isDataLoaded.value = true
  //   } catch (error) {
  //     console.error('Error fetching movie list:', error)
  //   }
  // })
</script>

<style scoped>
  .recommendation-message{
    margin: 65px 0px 30px;
  }
  .btn-toolbar {
    flex-direction: row;
    justify-content: space-around;
  }
</style>