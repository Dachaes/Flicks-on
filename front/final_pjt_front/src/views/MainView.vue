<template>
  <div>
    <Headers />
    <Banner />
    <MovieGroup />
    <MovieList />
    <MovieList />
    <footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Banner from '@/components/Banner.vue'
  import MovieGroup from '@/components/MovieGroup.vue'
  import MovieList from '@/components/MovieList.vue'
  import Footers from '@/components/Footers.vue'

  import { useRouter } from 'vue-router'

  const router = useRouter()

</script>

<style scoped>
  .btn-toolbar {
    flex-direction: row;
    justify-content: space-around;
  }
</style>