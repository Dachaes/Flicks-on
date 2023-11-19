<template>
  <div>
    <Headers />

    <MovieDetail />
    <MovieList />

    <CommentCreate />

    <CommentList />
    <Footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import MovieDetail from '@/components/MovieDetail.vue'
  import MovieList from '@/components/MovieList.vue'
  import CommentCreate from '@/components/CommentCreate.vue'
  import CommentList from '@/components/CommentList.vue'
  import Footers from '@/components/Footers.vue'

</script>

<style scoped>

</style>