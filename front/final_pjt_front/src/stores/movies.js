import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useMovieStore = defineStore('post', () => {
  const movieList = ref([])
  const getMovieList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/movies/'
    })
    .then(res => movieList.value = res.data)
    .catch(err => console.log(err))
  }


  const detailMovie = ref([])
  const detailMovieComment = ref([])
  const getDetailMovie = function (pk) {
    const TMDB_API_TOKEN = ref(import.meta.env.VITE_TMDB_API_TOKEN)
    
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/detail/${pk}`
    })
    .then(res => {
      detailMovieComment.value = res.data.comment_set
      console.log(detailMovieComment.value)
    })
    .catch(err => console.log(err))

    const options = {
      method: 'GET',
      url: `https://api.themoviedb.org/3/movie/${pk}`,
      params: {language: 'ko-KR'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_API_TOKEN.value}`
      }
    }
    axios
    .request(options)
    .then(function (response) {
      detailMovie.value = response.data
      let tmp = detailMovie.value.poster_path
      detailMovie.value.poster_path = 'https://image.tmdb.org/t/p/w500/' + tmp
    })
    .catch(function (error) {
      console.error(error)
    })
  }

  return { movieList, detailMovieComment, getMovieList, detailMovie, getDetailMovie}
})
