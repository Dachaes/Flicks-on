<template>
    <div class="comment-container" v-for="comment in movieStore.detailMovieComment" :key="comment.id">
    
      <div class="comment-user" v-if="!comment.deleting">
        <div v-if="comment.content">
          <p class="user-name">{{ comment.user_nickname }}</p>

          <img v-if="comment.user === userStore.userPk" class="user-img" @click="goProfile(userStore.userPk)" src="https://img.icons8.com/external-bearicons-glyph-bearicons/64/FFFFFF/external-User-essential-collection-bearicons-glyph-bearicons.png" alt="external-User-essential-collection-bearicons-glyph-bearicons"/>
          <img v-else class="other-user-img" src="https://img.icons8.com/external-bearicons-glyph-bearicons/64/FFFFFF/external-User-essential-collection-bearicons-glyph-bearicons.png" alt="external-User-essential-collection-bearicons-glyph-bearicons"/>
        
        </div>
      </div>
        
      <div class="comment-content" v-if="comment.user_id === userStore.userPk">
        <div v-if="!comment.editing" class="content-container">
          <p class="content">{{ comment.content }}</p>
          <div class="icon">
            <img class="edit" @click="editSwitch(comment)" src="https://img.icons8.com/glyph-neue/64/FFFFFF/edit--v1.png" alt="edit--v1"/>
            <img class="delete" @click="deleteComment(comment, comment.id)" src="https://img.icons8.com/sf-regular-filled/48/FFFFFF/trash.png" alt="trash"/>
          </div>
        </div>

        <div v-else>
            <input class="content" type="text" v-model="comment.content">
            <img class="accept" @click="commentEdit(comment.id, comment)" src="https://img.icons8.com/glyph-neue/64/FFFFFF/checkmark.png" alt="checkmark"/>
        </div>

        <p class="date">{{ comment.created_at }}</p>
      </div>

      <div class="comment-content" v-else>
        <p class="content">{{ comment.content }}</p>
        <p class="date">{{ comment.created_at }}</p>
      </div>

    </div>
  
</template>

<script setup>
  import { computed } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useUserStore } from '@/stores/users'
  import { useCommentStore } from '@/stores/comments'
  import { useMovieStore } from '@/stores/movies'

  const router = useRouter()
  const route = useRoute()
  const movieStore = useMovieStore()
  const commentStore = useCommentStore()
  const userStore = useUserStore()

  const deleteComment = (comment, pk) => {
    commentStore.commentDelete(route.params.title, pk)
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
  
  const goProfile = function (id) {
    router.push({name: 'profile', params: {user_name: id}})
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
  margin-bottom: 15px;
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
  text-align: center;
}

.user-name:hover {
  font-weight: bold;
  text-align: center;
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

.other-user-img {
  width: 70px;
  height: 70px;
  border-radius: 50%;
  cursor: pointer;
  opacity: 40%;
}
.comment-content {
  margin: 20px 0;
  flex: 0.9;
  flex-direction: row;
  padding-bottom: -10px;
}

.content-container {
  display: flex;
  align-items: center;
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

.icon {
  display: flex;
  flex-direction: column;
}

.comment-content img {
  width: 30px;
  cursor: pointer;
  margin: 5px 0;
}
.comment-content img :hover {
  width: 30px;
  cursor: pointer;
  margin: 5px 0;
  opacity: 50%;
}

.date {
  text-align: right;
  padding-right: 13%;
  margin: 0px;
}

.edit:hover, .delete:hover, .accept:hover {
  width: 30px;
  cursor: pointer;
  margin: 5px 0;
  opacity: 50%;
}
</style>