<template>
  <div>
    <Headers />
    <Banner />
    <div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
      <div v-for="button in 5">
        <button type="button" class="btn btn-secondary" @click="goPage('genre')">Romance</button>
      </div>
    </div>
    <MovieList />
    <MovieList />
    <footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import Banner from '@/components/Banner.vue'
  // import GenreView from '@/views/GenreView.vue'
  import MovieList from '@/components/MovieList.vue'
  import Footers from '@/components/Footers.vue'

  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goPage = function (pageName) {
    router.push({name: pageName, params: {genre: 'romance'}})
  }

</script>

<style scoped>
  .btn-toolbar {
    flex-direction: row;
    justify-content: space-around;
  }

  .btn {
    padding: 5px 20px;
  }
</style>