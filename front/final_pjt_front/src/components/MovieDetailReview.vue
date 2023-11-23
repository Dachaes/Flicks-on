<template>
  <div class="spoiler" v-if="!isVisible">
    <label @click="useApi(movieStore.detailMovie.title)">스포일러가 포함되어 있을 수 있어요!</label>
    <img @click="useApi(movieStore.detailMovie.title)" src="https://img.icons8.com/external-regular-kawalan-studio/24/FFFFFF/external-down-arrow-arrows-regular-kawalan-studio-6.png" alt="external-down-arrow-arrows-regular-kawalan-studio-6"/>
  </div>
  <div class="spoiler" v-else>
    <label @click="useApi(movieStore.detailMovie.title)">그만 볼래요!</label>
    <img @click="useApi(movieStore.detailMovie.title)" src="https://img.icons8.com/external-regular-kawalan-studio/24/FFFFFF/external-up-arrow-arrows-regular-kawalan-studio-2.png" alt="external-up-arrow-arrows-regular-kawalan-studio-2"/>
  </div>

  <div class="reviews">
    <div class="review" v-for="review in reviews" :key="review.title">
      <p class=review-title v-html="review.title" @click="openModal(review.url)" ></p>
      <img v-if="review.thumbnail" class="review-thumbnail" :src="review.thumbnail" alt="thumbnail" @click="openModal(review.url)">
      <img v-else class="review-thumbnail" 
      src="@/assets/movie/movieAltImage.png" alt="movie_poster">
    </div>
  </div>

  <div v-if="showModal" class="modal">
    <div class="review-modal">
        <span class="close" @click="closeModal">&times;</span>
        <iframe class="review-content"
        :src="url"
        width="1500" height="800"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </div>
</template>

<script setup>
  import {ref} from 'vue'
  import axios from 'axios'
  const reviews = ref([])
  const isVisible = ref(false)
  const REST_API_KEY = ref(import.meta.env.VITE_KAKAO_REST_API_KEY)
  
  const useApi = function (title) {
    isVisible.value = !isVisible.value

    if (isVisible.value) {
      axios({
        method:'get',
        url: `https://dapi.kakao.com/v2/search/blog`,
        headers: {
          'Authorization': `KakaoAK ${REST_API_KEY.value}`,
        },
        params: {
          'query': '영화' + title + ' 평론가 리뷰',
          'size': 6
        }
      })
        .then (res => {
          // console.log(res)
          reviews.value = res.data.documents
          // console.log(reviews.value)
        })
        .catch (err => {
          console.log(err)
        })
    }
    else {
      reviews.value = []
      // console.log(reviews.value)
    }
  }

  const url = ref('')
  const showModal = ref(false)

  const openModal = (openUrl) => {
    showModal.value = true
    url.value = openUrl
    // console.log(url.value)
  }

  const closeModal = () => {
    showModal.value = false
  }


  import { useMovieStore } from '@/stores/movies'
  const movieStore = useMovieStore()

</script>

<style scoped>

  .spoiler {
    display: flex;
    align-items: center;
    padding: 20px 30px 10px;
    color: rgb(255, 164, 164);
    margin-bottom: 10px;
    transition: opacity 0.5s;
    cursor: pointer;
  }

  .spoiler:hover {
    opacity: 0.5;
  }

  .spoiler label {
    font-size: 18px;
  }

  .spoiler img {
    width: 20px;
    height: 20px;
    margin-left: 10px;
    margin-bottom: 3px;
  }
  .reviews {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    gap: 1px;
  }
  .review {
    display: flex;
    /* flex-wrap: wrap; */
    flex-direction: column;
    margin-bottom: 10px;
    width: 31%;
    background-color: #1e1e1e;
    border: 1px solid #333;
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 15px;
  }
  .review-title {
    height: 30px;
    font-size: 17px;
    transition: opacity 0.5s;
    cursor: pointer;
  }
  
  .review-title:hover {
    opacity: 0.5;
  }
  
  .review-thumbnail {
    border: 1px solid #333;
    border-radius: 50px;
    margin-left: auto;
    width: 150px;
    height: 150px;
    transition: opacity 0.5s;
    cursor: pointer;
  }

  .review-thumbnail:hover {
    opacity: 0.5;
  }

  .modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgb(237, 237, 237, 0.92);
  z-index: 1000;
  }

  .review-modal {
    display: flex;
    flex-direction: column;
    margin: 10px;
    border-radius: 5px;
  }

  .review-modal p {
    font-size: 14px;
    font-weight: bold;
    margin-bottom: 5px;
  }

  .close {
  position: absolute;
  top: 30px;
  right: 30px;
  cursor: pointer;
  color: rgb(30, 30, 30);
  font-size: 24px;
  }

</style>