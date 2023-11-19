import axios from 'axios'
import { defineStore } from 'pinia'

export const useCommentStore = defineStore('comment', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const commentCreate = function (pk, content) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/detail/${pk}/comment/`,
      data: {
        content
      }
    })
  }
  return { commentCreate }
})
