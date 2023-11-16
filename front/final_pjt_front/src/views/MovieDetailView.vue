<template>
  <div>
    <h1>무비 디테일 뷰</h1>
    <h3>한줄평</h3>
    <h4>작성</h4>
    <CommentCreate />
    <h4>조회</h4>
    <CommentList />
  </div>
</template>

<script setup>
  import CommentCreate from '@/components/CommentCreate.vue'
  import CommentList from '@/components/CommentList.vue'
</script>

<style scoped>

</style>