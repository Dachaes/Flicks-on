<template>
  <div>
    <Headers />
    <MovieDetail :tmdb-id="tmdb_id"/>
    
    <MovieDetailTrailer :tmdb-id="tmdb_id"/>
    <MovieListSimilar :tmdb-id="tmdb_id"/>

    <CommentCreate />
    
    <CommentList />

    <Footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import MovieDetail from '@/components/MovieDetail.vue'
  import MovieDetailTrailer from '@/components/MovieDetailTrailer.vue'
  import MovieListSimilar from '@/components/MovieListSimilar.vue'
  import CommentCreate from '@/components/CommentCreate.vue'
  import CommentList from '@/components/CommentList.vue'
  import Footers from '@/components/Footers.vue'

  import { ref } from 'vue'
  import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const router = useRouter()
  const tmdb_id = ref(route.params.title)
  console.log(tmdb_id.value)

  onBeforeRouteUpdate((to, from) => {
    tmdb_id.value = to.params.title
  })

</script>

<style scoped>

</style>