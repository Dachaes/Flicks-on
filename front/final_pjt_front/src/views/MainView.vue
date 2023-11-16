<template>
  <div>
    <h1>메인 뷰</h1>
    <Banner />
    <hr>
    <button @click="goPage('genre')">장르 뷰</button>
    <MovieList />
    <MovieList />
  </div>
</template>

<script setup>
  import Banner from '@/components/Banner.vue'
  // import GenreView from '@/views/GenreView.vue'
  import MovieList from '@/components/MovieList.vue'

  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goPage = function (pageName) {
    router.push({name: pageName, params: {genre: 2}})
  }

</script>

<style scoped>

</style>