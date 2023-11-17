<template>
  <h2 class="mt-3">작성한 한줄평</h2>
  <div class="comments-container">
    <div class="movie">
      <img @click="goPage('movie_detail')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="m-0 p-0">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="comment">
      <img src="@/assets/likes/heart2.png" width="33" alt="likes">
      <div class="one-comment">  </div>
    </div>
  </div>

</template>

<script setup>
  import { useRouter } from 'vue-router'
  const router = useRouter()

  const goPage = function (pageName) {
    router.push({name: pageName, params: {title: 'parasite'}})
  }
</script>

<style scoped>
  .comments-container {
    display: flex;
    align-items: center;
    margin-top: 15px;
  }

  .movie-poster {
    height: 300px;
  }
  .comment {
    display: flex;
    margin-left: 50px;
    flex-direction: column;
  }

  .one-comment {
    margin-top: 10px;
    height: 200px;
    width: 750px;
    border: 1px solid rgb(130, 128, 128);
  }
</style>