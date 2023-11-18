<template>
  <div class="container">
    <MovieGroupSub />
    <MovieGroupSub />
    <MovieGroupSub />
    <MovieGroupSub />
  </div>
</template>

<script setup>
import MovieGroupSub from "@/components/MovieGroupSub.vue";

</script>

<style scoped>
.container {
  /* align-items: flex-start;
  display: flex;
  flex-direction: row; */
  /* gap: 40px; */
  /* position: relative; */
  display: flex;
  justify-content: space-around;
  margin-top: 30px;
  padding: 10px 0;
}
</style>