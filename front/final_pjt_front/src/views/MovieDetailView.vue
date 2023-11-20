<template>
  <div>
    <Headers />

    <MovieDetail :tmdb-id="tmdb_id"/>

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

  import { ref } from 'vue'
  import { useRoute } from 'vue-router'

  const route = useRoute()
  const tmdb_id = ref(route.params.title)

  // import { onMounted } from 'vue'
  // import { useMovieStore } from '@/stores/movies'
  // const route = useRoute()
  // const store = useMovieStore()
  // onMounted(() => {
  //   store.getDetailMovie(route.params.pk)
  // })

</script>

<style scoped>

</style>