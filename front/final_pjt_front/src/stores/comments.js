import axios from 'axios'
import { defineStore } from 'pinia'
import { useUserStore } from './users'
import { ref } from 'vue'

export const useCommentStore = defineStore('comment', () => {
  const userStore = useUserStore()
  const movieList = ref(null)
  const API_URL = 'http://127.0.0.1:8000'
  const commentCreate = function (pk, content) {
    console.log(pk)
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/detail/${pk}/comment/`,
      data: {
        content,
        pk: userStore.userPk
      }
    })
  }

  const commentUpdate = function (movie_pk, comment_pk, content) {
    axios({
      method: 'put',
      url: `${API_URL}/api/v1/detail/${movie_pk}/comment/${comment_pk}`,
      data: {
        pk: userStore.userPk,
        movie: movie_pk,
        contnent: content,
      }
    })
  }

  const commentDelete = function (movie_pk, comment_pk) {
    axios({
      method: 'delete',
      url: `${API_URL}/api/v1/detail/${movie_pk}/comment/${comment_pk}`,
      data: {
        pk: userStore.userPk,
        movie: movie_pk,
        contnent: content,
      }
    })
  }
  return { commentCreate, commentUpdate, commentDelete }
})
