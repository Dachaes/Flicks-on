<template>
  <div class="comment-container">
    <div class="comment-user">
      <p class="user-name">{{ userStore.userNickName }}</p>
    <img class="user-img" @click="goProfile()" src="https://img.icons8.com/external-bearicons-glyph-bearicons/64/FFFFFF/external-User-essential-collection-bearicons-glyph-bearicons.png" alt="external-User-essential-collection-bearicons-glyph-bearicons"/>
    </div>
    <div class="comment-content">
      <form>
        <input class="content" type="text" :value="content" @input="updateComment" placeholder="해당 영화의 한 줄 평가를 해주세요!">
        <img @click="createComment" class="accept" src="https://img.icons8.com/pulsar-line/96/FFFFFF/plus-2-math.png" alt="plus-2-math"/>
      </form>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useUserStore } from '@/stores/users'
  import { useCommentStore } from '@/stores/comments.js'
  import { useMovieStore } from '@/stores/movies'
  import { useRouter, useRoute } from 'vue-router'

  const userStore =useUserStore()
  const movieStore = useMovieStore()
  const commentStore = useCommentStore()
  const router = useRouter()
  const route = useRoute()
  const content = ref('')

  const updateComment = function (event) {
    content.value = event.currentTarget.value
  }

  const createComment = function () {
    commentStore.commentCreate(route.params.title, content.value)
  
    // console.log(route.params.title)
    // router.push({name:'movies', params:{title:route.params.title}})
    movieStore.getDetailMovie(route.params.title)
    content.value = ''
  }
</script>

<style scoped>
  .comment-container {
  display: flex;
  flex-direction: row;
  background-color: #1e1e1e;
  border: 1px solid #333;
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 50px;
}

.comment-user {
  margin: auto;
  padding-bottom: 18px;
  display: flex;
  align-items: center;
  flex-direction: column;
  margin: auto;
}

.user-name {
  font-weight: bold;
}

.user-name:hover {
  font-weight: bold;
  opacity: 50%;
}

.user-img {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  cursor: pointer;
}

.user-img:hover {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  opacity: 50%;
}

.comment-content {
  margin: 20px 0;

  flex: 0.9;
  /* margin-left: auto; */
  flex-direction: row;
}

.content {
  width: 88%;
  height: 100px;
  padding: 15px;
  border-radius: 8px;
  border: 1px solid #ccc;
  margin-right: 20px;
  margin-bottom: 6px;
}

.content:hover {
  width: 88%;
  height: 100px;
  padding: 15px;
  border-radius: 8px;
  border: 1px solid #ccc;
  margin-right: 20px;
  margin-bottom: 6px;
  opacity: 90%;
}

.accept {
  width: 45px;
  border-radius: 4px;
  cursor: pointer;
}
.accept:hover {
  width: 45px;
  border-radius: 4px;
  cursor: pointer;
  opacity: 50%;
}

</style>