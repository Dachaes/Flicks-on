<template>
  <div>
    <Headers />
    <Banner />
    <form @submit.prevent="goSearch(query)">
      <input type="text" :value="query" @input="updateQuery">
      <input type="submit" value="Search">
    </form>
    <h2 class="recommendation-message">현재 상영작이에요!</h2>
    <MovieListNowPlaying />
    <h2 class="recommendation-message">유명한 작품이에요!</h2>
    <MovieListTopRated />
    <h2 class="recommendation-message">개봉 예정작이에요!</h2>
    <MovieListUpcomming />
    <footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Banner from '@/components/Banner.vue'
  import MovieListNowPlaying from '@/components/MovieListNowPlaying.vue'
  import MovieListTopRated from '@/components/MovieListTopRated.vue'
  import MovieListUpcomming from '@/components/MovieListUpcomming.vue'
  import Footers from '@/components/Footers.vue'

  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  const router = useRouter()

  const query = ref('')
  
  const updateQuery = function (event) {
    query.value = event.currentTarget.value
  }
  
  const goSearch = function (query) {
    router.push({name: 'search', params: { query: query } })
  }
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