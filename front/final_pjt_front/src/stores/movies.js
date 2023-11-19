import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const usePostStore = defineStore('post', () => {
  // const postList = ref([])
  // const getPostList = function () {
  //   axios({
  //     method: 'get',
  //     url: 'http://127.0.0.1:8000/api/v1/posts/'
  //   })
  //   .then(res => postList.value = res.data)
  //   .catch(err => console.log(err))
  // }
  const detailMovie = ref([])
  const getDetailMovie = function (pk) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/detail/${pk}`
    })
    .then(res => detailMovie.value = res.data)
    .catch(err => console.log(err))
  }

  // const createPost = function ({category, title, content}) {
  //   axios({
  //     method: 'post',
  //     url: 'http://127.0.0.1:8000/api/v1/posts/',
  //     data: {
  //       category,
  //       title,
  //       content
  //     }
  //   })
  // }
  return { postList, getPostList, detailPost, getDetailPost, createPost }
})
