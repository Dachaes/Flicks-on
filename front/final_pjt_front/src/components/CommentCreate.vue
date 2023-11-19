<template>
  <h2 class="mt-3">한줄평</h2>
  <div class="comments-container">
    <div class="movie">
      <p class="user-name">User</p>
      <img class="movie-poster" src="@/assets/user/anonymous_user.png" alt="user_profile">
    </div>
    <div class="comment">
      <form @submit.prevent="createComment">
        <input type="text" v-model="comment">
        <p>{{ comment }}</p>
        <input type="submit" value="등록">
      </form>
    </div>
  </div>

</template>

<script setup>
  import { useRouter } from 'vue-router'
  const router = useRouter()
  const comment = ref('')

  const createComment = function (event) {
    comment.value = event.currentTarget.value
  }
</script>

<style scoped>
  .comments-container {
    display: flex;
    align-items: center;
    margin-top: 15px;
    border-top: 1px solid rgb(139, 139, 139);
    border-bottom: 1px solid rgb(139, 139, 139);
    padding: 10px 0 20px;
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