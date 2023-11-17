<template>
  <div>
    <Headers />
    <Banner />
    <hr>
    <button @click="goPage('genre')">장르 뷰</button>
    <MovieList />
    <MovieList />
    <footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Banner from '@/components/Banner.vue'
  // import GenreView from '@/views/GenreView.vue'
  import MovieList from '@/components/MovieList.vue'
  import Footers from '@/components/Footers.vue'

  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goPage = function (pageName) {
    router.push({name: pageName, params: {genre: 'romance'}})
  }

</script>

<style scoped>

</style>