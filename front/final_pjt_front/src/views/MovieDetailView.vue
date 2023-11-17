<template>
  <div>
    <Headers />
    <h1>무비 디테일 뷰</h1>
    <h3>한줄평</h3>
    <h4>작성</h4>
    <MovieDetail />
    <CommentCreate />
    <h4>조회</h4>
    <CommentList />
    <Footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import MovieDetail from '@/components/MovieDetail.vue'
  import CommentCreate from '@/components/CommentCreate.vue'
  import CommentList from '@/components/CommentList.vue'
  import Footers from '@/components/Footers.vue'
</script>

<style scoped>

</style>