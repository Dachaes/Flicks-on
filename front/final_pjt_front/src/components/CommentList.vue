<template>
  <div class="comments-container">
    <div v-for="comment in movieStore.detailMovieComment">
      <div class="movie">
        <div v-if="comment.content">
          <!-- <p class="user-name">{{ comment.id }}</p> -->
          <p class="user-name">{{ comment.user_nickname }}</p>
    
          <img class="movie-poster" src="@/assets/user/anonymous_user.png" alt="user_profile">
        </div>
        <div class="comment">
          <img src="@/assets/likes/heart2.png" width="33" alt="likes">
          <!-- <p class="one-comment">{{ comment.content }}</p> -->
          <p class="one-comment">{{ comment.content }}</p>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup>
  import { useRouter, useRoute } from 'vue-router'
  import { useMovieStore } from '@/stores/movies'

  const router = useRouter()
  const route = useRoute()
  const movieStore = useMovieStore()

  // defineProps({
    // comment: Object
  // })
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

  .movie p {
    text-align: center;
  }

  .movie-poster {
    width: 100%;
    /* object-fit: cover; */
  }

  .user-name {
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