<template>
  <div class="comments-container">
    <div v-for="comment in movieStore.detailMovieComment" :key="comment.id">
      <div class="movie" v-if="!comment.deleting">
        <div v-if="comment.content">
          <p class="user-name">{{ comment.user_nickname }}</p>
          <img class="movie-poster" src="@/assets/user/anonymous_user.png" alt="user_profile">
        </div>
        <!-- <img src="@/assets/likes/heart2.png" width="33" alt="likes"> -->

        <div class="comment" v-if="!comment.editing">
          <p class="one-comment">{{ comment.content }}</p>
          <button @click="editSwitch(comment)">Edit</button>
        </div>
        <div class="comment" v-else>
          <form class="one-comment" @submit.prevent="commentEdit(comment.id, comment)">
            <input type="text" v-model="comment.content">
            <button type="submit">Accept</button>
          </form>
        </div>

        <button @click="deleteComment(comment, comment.id)">Delete</button>
      </div>
    </div>
  </div>

  
</template>

<script setup>
  import { useRouter, useRoute } from 'vue-router'
  import { useCommentStore } from '@/stores/comments'
  import { useMovieStore } from '@/stores/movies'

  const router = useRouter()
  const route = useRoute()
  const movieStore = useMovieStore()
  const commentStore = useCommentStore()

  const deleteComment = (comment, pk) => {
    commentStore.commentDelete(route.params.title, pk)
    // router.push({name: "movie_detail", params: {title: pk}})
    comment.deleting = !comment.deleting
  }

  const editSwitch = (comment) => {
    comment.editing = !comment.editing
  }

  const commentEdit = (pk, comment) => {
    const payLoad = {
      movie_pk: route.params.title,
      comment_pk: pk,
      content: comment.content,
    }
    commentStore.commentUpdate(payLoad)
    comment.editing = false
  }
  
  // const comments = ref(movieStore.detailMovieComment)

  // watch(comments, (newValue, oldValue) => {
  //   console.log(newValue)
  // }, { immediate: true })

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