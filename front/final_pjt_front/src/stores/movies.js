import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useMovieStore = defineStore('post', () => {
  const TMDB_API_TOKEN = ref(import.meta.env.VITE_TMDB_API_TOKEN)
  

  const movieList = ref([])
  const getMovieList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/movies/'
    })
    .then(res => movieList.value = res.data)
    .catch(err => console.log(err))
  }



  const searchMovie = ref([])
  const getSearchMovie = function (q) {
    const options = {
      method: 'GET',
      url: 'https://api.themoviedb.org/3/search/movie',
      params: {query: `${q}`, include_adult: 'false', language: 'ko-KR', page: '1'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_API_TOKEN.value}`
      }
    };
    
    axios
      .request(options)
      .then(function (response) {
        searchMovie.value = response.data.results
        searchMovie.value.forEach((movie, index) => {
          if (movie.vote_average === 0) {
            movie.vote_average = '--'
          } else {
            movie.vote_average = Math.round(movie.vote_average * 10) / 10
          }
        })
        // console.log(response.data)
      })
      .catch(function (error) {
        console.error(error);
      });
  }

  

  const nowPlayingMovie = ref([])
  const getNowPlayingMovie = function () {
    const options = {
      method: 'GET',
      url: 'https://api.themoviedb.org/3/movie/now_playing',
      params: {language: 'ko-KR', page: '1'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_API_TOKEN.value}`
      }
    };
    
    axios
      .request(options)
      .then(function (response) {
        nowPlayingMovie.value = response.data.results
        nowPlayingMovie.value.forEach((movie, index) => {
          if (movie.vote_average === 0) {
            movie.vote_average = '--'
          } else {
            movie.vote_average = Math.round(movie.vote_average * 10) / 10
          }
        })
      })
      .catch(function (error) {
        console.error(error);
      });
  }



  const topRatedMovie = ref([])
  const getTopRatedMovie = function () {
    const options = {
      method: 'GET',
      url: 'https://api.themoviedb.org/3/movie/top_rated',
      params: {language: 'ko-KR', page: '1'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_API_TOKEN.value}`
      }
    };

    axios
      .request(options)
      .then(function (response) {
        console.log(response.data)
        topRatedMovie.value = response.data.results
        topRatedMovie.value.forEach((movie, index) => {
          if (movie.vote_average === 0) {
            movie.vote_average = '--'
          } else {
            movie.vote_average = Math.round(movie.vote_average * 10) / 10
          }
        })
      })
      .catch(function (error) {
        console.error(error)
      });
  }




  const upcomingMovie = ref([])
  const getUpcomingMovie = function () {  
    const options = {
      method: 'GET',
      url: 'https://api.themoviedb.org/3/movie/upcoming',
      params: {language: 'ko-KR', page: '1'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_API_TOKEN.value}`
      }
    };
    
    axios
      .request(options)
      .then(function (response) {
        // console.log(response.data)
        upcomingMovie.value = response.data.results
        upcomingMovie.value.forEach((movie, index) => {
          if (movie.vote_average === 0) {
            movie.vote_average = '--'
          } else {
            movie.vote_average = Math.round(movie.vote_average * 10) / 10
          }
        })
      })
      .catch(function (error) {
        console.error(error)
      });
  }





  const similarMovie = ref([])
  const getSimilarMovie = function (pk) {
    const options = {
      method: 'GET',
      url: `https://api.themoviedb.org/3/movie/${pk}/similar`,
      params: {language: 'ko-KR', page: '1'},
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_API_TOKEN.value}`
      }
    };
    
    axios
      .request(options)
      .then(function (response) {
        similarMovie.value = response.data.results
        similarMovie.value.forEach((movie, index) => {
          if (movie.vote_average === 0) {
            movie.vote_average = '--'
          } else {
            movie.vote_average = Math.round(movie.vote_average * 10) / 10
          }
        })
      })
      .catch(function (error) {
        console.error(error)
      })
  }



  const detailMovie = ref([])
  const detailMovieComment = ref([])
  const getDetailMovie = function (pk) {
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
      if (detailMovie.value.vote_average === 0) {
        detailMovie.value.vote_average = '--'
      } else {
        detailMovie.value.vote_average = Math.round(detailMovie.value.vote_average * 10) / 10
      }
    })
    .catch(function (error) {
      console.error(error)
    })
  }

  return { movieList, getMovieList, searchMovie, getSearchMovie,
    detailMovieComment, getMovieList, nowPlayingMovie, getNowPlayingMovie,
    topRatedMovie, getTopRatedMovie, upcomingMovie, getUpcomingMovie, similarMovie, getSimilarMovie,
    detailMovie, getDetailMovie}
})
