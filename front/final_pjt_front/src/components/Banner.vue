<template>
  <div id="carouselExampleCaptions" class="carousel slide">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
      <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
    </div>

    <div id="carouselExample" class="carousel slide banner-container">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img @click="goPage(157336)" src="@/assets/banner/img1.jpg" class="d-block" alt="exImg1">
        </div>
        <div class="carousel-item">
          <img @click="goPage(872585)" src="@/assets/banner/img4.jpg" class="d-block w-150" alt="exImg2">
        </div>
        <div class="carousel-item">
          <img @click="goPage(129)" src="@/assets/banner/img5.jpg" class="d-block w-150" alt="exImg3">
        </div>
      </div>

      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>

      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>

  </div>
 </template>

 
<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goPage = function (id) {
  router.push({name:'movie_detail', params:{title:id}})
}


</script>

<style scoped>
  .banner-container {
    position: relative;
    margin: 20px 10px;
    height: 400px;
    min-height: 400px; 
  }
  .d-block {
    object-fit: cover;
    width: 100%;
    min-height: 400px;
    height: 400px;
  }
</style>