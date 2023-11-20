import axios from 'axios'
import { defineStore } from 'pinia'
import { useUserStore } from './users'

export const useCommentStore = defineStore('comment', () => {
  const userStore = useUserStore()
  const API_URL = 'http://127.0.0.1:8000'
  const commentCreate = function (pk, content) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/detail/${pk}/comment/`,
      data: {
        content,
        pk: userStore.userPk
      }
    })
  }
  return { commentCreate }
})
