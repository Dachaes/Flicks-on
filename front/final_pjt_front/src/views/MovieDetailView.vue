<template>
  <div>
    <Headers />
    <MovieDetail :tmdb-id="tmdb_id"/>

    <h2 class="recommendation-message">관련 영상</h2>
    <MovieDetailTrailer :tmdb-id="tmdb_id"/>
    
    <h2 class="recommendation-message">관련 영화</h2>
    <MovieListSimilar :tmdb-id="tmdb_id"/>
    
    <h2 class="recommendation-message">관련 리뷰</h2>
    <MovieDetailReview :tmdb-id="tmdb_id" />

    <h2 class="recommendation-message">한줄평</h2>
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
  import MovieDetailReview from '@/components/MovieDetailReview.vue'
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

.recommendation-message {
  margin-top: 70px;
  margin-right: auto;
  margin-bottom: 30px;
  padding-left: 20px;
  padding-bottom: 20px;
  border-bottom: 1px solid #333;
}
</style>