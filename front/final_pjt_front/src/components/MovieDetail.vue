<template>
  <div class="container">
    <img class="movie-poster" src="@/assets/movie/parasite.png" alt="poster">
    
    <div class="movie-info">
      <div class="movie-title">
        
      </div>
      <div class="movie-detail">
      
      </div>

    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
  .container {
    display: flex;
    background-color: aqua;
    margin-top: 10px;
  }
  
  .movie-poster {
    border: 1px solid black;
    width: 30%;
  }

  .movie-info {
    display: flex;
    justify-content: row;
  }
  .movie-title {
    border: 1px solid black;
    
  }

  .movie-detail {
    border: 1px solid black;

  }
</style>