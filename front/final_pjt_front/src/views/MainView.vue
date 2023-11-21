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