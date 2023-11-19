<template>
  <div>
    <Headers />

    <MovieDetail />
    <MovieList />

    <CommentCreate />
    <!-- <CommentCreate 
      :moviePk="store.detailMovie.id"
    /> -->
    
    <CommentList />
    <!-- <ul class="comment-list">
      <CommentList
          v-for="comment in store.detailMovie.comment_set"
          :key="comment.id"
          class="comment-item"
          :comment="comment"
        />
    </ul> -->
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

  // import { onMounted } from 'vue'
  // import { useRoute } from 'vue-router'
  // import { useMovieStore } from '@/stores/movies'
  // const route = useRoute()
  // const store = useMovieStore()
  // onMounted(() => {
  //   store.getDetailMovie(route.params.pk)
  // })

</script>

<style scoped>

</style>