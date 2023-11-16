<template>
  <div>
    <h1>무비 리스트 컴포넌트</h1>
  </div>
  <button @click="goPage('movie_detail')">영화 디테일 페이지 이동</button>
</template>

<script setup>
  // import MovieDetailView from '@/views/MovieDetailView.vue'

  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goPage = function (pageName) {
    router.push({name: pageName, params: {title: 'parasite'}})
  }
</script>

<style scoped>

</style>