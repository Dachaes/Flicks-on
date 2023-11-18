<template>
  <div class="card">
    <div class="container">
      <div class="image-container">
        <img class="image" alt="Image" src="@/assets/movie/parasite.png" />
        <img class="image" alt="Image" src="@/assets/movie/parasite.png" />
      </div>
      <div class="image-container">
        <img class="image" alt="Image" src="@/assets/movie/parasite.png" />
        <img class="image" alt="Image" src="@/assets/movie/parasite.png" />
      </div>
      <!-- <div class="fade-out-bottom">
      </div> -->
    </div>
    <div class="div">
      <div class="heading">Adventure</div>
      <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
        <path d="M438.6 278.6c12.5-12.5 12.5-32.8 0-45.3l-160-160c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3L338.8 224 32 224c-17.7 0-32 14.3-32 32s14.3 32 32 32l306.7 0L233.4 393.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0l160-160z"/>
      </svg>
    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
.card {
  align-items: flex-start;
  border: 1px solid rgb(168, 168, 168);
  border-radius: 10px;
  padding: 5px;
  margin: 10px;
  width: 25%;
}

.container {
  align-items: flex-start;
  align-self: stretch;
  display: flex;
  flex-direction: column;
  gap: 5px;
  overflow: hidden;
  position: relative;
  width: 100%;
  margin: 0px;
  padding: 5px;
}

.image-container {
  align-items: flex-start;
  align-self: stretch;
  display: flex;
  flex: 1;
  flex-grow: 1;
  gap: 5px;
  position: relative;
  width: 100%;
}

.image {
  width: 50%;
  align-self: stretch;
  flex: 1;
  flex-grow: 1;
  object-fit: contain;
  position: relative;

}

.fade-out-bottom {
  background: linear-gradient(180deg, rgba(26, 26, 26, 0) 0%, rgb(26, 26, 26) 100%);
  height: 210px;
  left: -9px;
  position: absolute;
  top: -23px;
  width: 193px;
}

.div {
  align-items: center;
  align-self: stretch;
  display: flex;
  flex: 0 0 auto;
  position: relative;
  width: 100%;
}

.heading {
  color: var(--absolutewhite);
  flex: 1;
  font-family: "Manrope-SemiBold", Helvetica;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0;
  line-height: 24px;
  margin-top: -1px;
  position: relative;
}

.icon {
  height: 24px;
  position: relative;
  width: 24px;
}
</style>
