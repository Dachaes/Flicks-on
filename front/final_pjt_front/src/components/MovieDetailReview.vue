<template>
  <button @click="useApi('센과 치히로의 행방불명')">스포일러가 포함되어 있을 수 있어요!</button>
  <div v-for="review in reviews" :key="review.title">
    <p class=title v-html="review.title"></p>
    <img class="thumbnail" :src="review.thumbnail" alt="" @click="openModal(review.url)">
  </div>
  <div v-if="showModal" class="modal">
    <div class="reviews">
        <span class="close" @click="closeModal">&times;</span>
        <iframe class="review"
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
  // APP_KEY = 
//   Kakao.init('${APP_KEY}'); // 사용하려는 앱의 JavaScript 키 입력
  const isVisible = ref(false)
  const REST_API_KEY = ref(import.meta.env.VITE_KAKAO_REST_API_KEY)
  
  const useApi = function (title) {
    isVisible.value = !isVisible.value
    console.log(isVisible.value)

    if (isVisible) {
      axios({
        method:'get',
        url: `https://dapi.kakao.com/v2/search/blog`,
        headers: {
          'Authorization': `KakaoAK ${REST_API_KEY.value}`,
        },
        params: {
          'query': title + ' 평론가 리뷰',
          'size': 6
        }
      })
        .then (res => {
          // console.log(res)
          reviews.value = res.data.documents
          console.log(reviews.value)

        })
        .catch (err => {
          // console.log(err)
        })
    }
    else if (!isVisible) {
      reviews.value = null
      console.log(reviews.value)
    }
  }

  const url = ref('')
  const showModal = ref(false)

  const openModal = (openUrl) => {
    showModal.value = true
    url.value = openUrl
    console.log(url.value)
  }

  const closeModal = () => {
    showModal.value = false
  }
</script>

<style scoped>
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
z-index: 1;
}

.revies {
position: relative;
}

.close {
position: absolute;
top: 30px;
right: 30px;
cursor: pointer;
color: rgb(30, 30, 30);
font-size: 24px;
}

.thumbnail {
  width: 150px;
  height: auto;
  }
</style>