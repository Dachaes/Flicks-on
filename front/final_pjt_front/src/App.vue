<template>
  <header class="wrapper">
    <div>
      <RouterView />
    </div>
  </header>
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
  .wrapper {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

</style>
