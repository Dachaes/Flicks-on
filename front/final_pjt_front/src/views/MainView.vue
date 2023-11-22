<template>
  <div>
    <Headers />
    <banner />
    <div class="container">
      <h2 class="recommendation-message">> 현재 상영작이에요!</h2>
      <MovieListNowPlaying />
      <h2 class="recommendation-message">> 유명한 작품이에요!</h2>
      <MovieListTopRated />
      <h2 class="recommendation-message">> 개봉 예정작이에요!</h2>
      <MovieListUpcomming />
    </div>
    <Footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Banner from '@/components/Banner.vue'
  import MovieListNowPlaying from '@/components/MovieListNowPlaying.vue'
  import MovieListTopRated from '@/components/MovieListTopRated.vue'
  import MovieListUpcomming from '@/components/MovieListUpcomming.vue'
  import Footers from '@/components/Footers.vue'
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.recommendation-message {
  margin-top: 60px;
  margin-left: 3%;
  margin-right: auto;
  margin-bottom: -10px;
}

.recommendation-message:hover {
  margin-top: 60px;
  margin-left: 3%;
  margin-right: auto;
  margin-bottom: -10px;
  opacity: 50%;
}
</style>