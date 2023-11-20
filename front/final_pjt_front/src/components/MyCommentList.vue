<template>
  <h2 class="mt-3">작성한 한줄평</h2>
  <div class="comments-container">
    <div class="movie">
      <img @click="goPage('movie_detail')" class="movie-poster" src="@/assets/movie/parasite.png" alt="movie_poster">
      <p class="movie-title">기생충</p>
      <img src="@/assets/likes/heart2.png" width="17" alt=""> 5.3
    </div>
    <div class="comment">
      <img src="@/assets/likes/heart2.png" width="33" alt="likes">
      <p class="one-comment">재밌어요!</p>
    </div>
    <div>
      <button>수정</button>
      <button>삭제</button>
    </div>
  </div>

</template>

<script setup>
  import { useCommentStore } from '@/stores/comments'
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

  .movie {
    width: 20%;
  }

  .movie-poster {
    width: 100%;
    /* object-fit: cover; */
  }

  .movie-title {
    margin-top: 2px;
    margin-bottom: 5px;
  }

  .comment {
    display: flex;
    flex-direction: column;
    width: 80%;
    margin-left: 10px;
  }

  .one-comment {
    margin-top: 10px;
    margin-right: 100px;
  }
</style>