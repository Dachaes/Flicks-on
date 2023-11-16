<template>
  <header>
    <div class="wrapper">
      <Headers />
    </div>
  </header>
  <hr>
  <RouterView />
  <hr>
  <Footers />
</template>

<script setup>
// import { RouterLink, RouterView } from 'vue-router'
import MainView from '@/views/MainView.vue'
import { RouterView } from 'vue-router';
import Headers from '@/components/Headers.vue'
import Footers from '@/components/Footers.vue'
</script>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

nav {
  display: flex;
  justify-content: center;
  background-color: #333;
  padding: 1rem 0;
}

nav a {
  color: #fff;
  text-decoration: none;
  margin: 0 1rem;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}
</style>
