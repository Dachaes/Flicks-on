<template>
  <div class="trailers" v-for="Url in youtubeEmbedUrl" :key="Url">
    <iframe class="trailer"
      width="560"
      height="315"
      :src="Url"
      frameborder="0"
      allow="fullscreen; accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, computed } from 'vue'

const props = defineProps({
    tmdbId: String
  })


const TMDB_API_TOKEN = ref(import.meta.env.VITE_TMDB_API_TOKEN)
const keys = ref(['', '', ''])
const youtubeEmbedUrl = ref(['', '', ''])
const options = {
  method: 'GET',
  url: `https://api.themoviedb.org/3/movie/${props.tmdbId}/videos`,
  params: {language: 'en-US'},
  headers: {
    accept: 'application/json',
    Authorization: `Bearer ${TMDB_API_TOKEN.value}`
  }
};

axios
  .request(options)
  .then(function (response) {
    console.log(response.data.results);
    keys.value[0] = response.data.results[0].key
    keys.value[1] = response.data.results[1].key
    keys.value[2] = response.data.results[2].key

    // const youtubeEmbedUrl = `https://www.youtube.com/embed/${url}`
    // const youtubeEmbedUrl = computed(() => `https://www.youtube.com/embed/${props.movieTrailer}`)
    youtubeEmbedUrl.value[0] = `https://www.youtube.com/embed/${keys.value[0]}`
    youtubeEmbedUrl.value[1] = `https://www.youtube.com/embed/${keys.value[1]}`
    youtubeEmbedUrl.value[2] = `https://www.youtube.com/embed/${keys.value[2]}`
  })
  .catch(function (error) {
    console.error(error);
  });

</script>

<style scoped>
.trailers {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: 20px 0;
}

.trailer {
  width: 300px;
  height: 170px;
  margin: 10px;
  border-radius: 5px;
}

@media (max-width: 768px) {
  .trailer {
    width: 200px;
    height: 112px;
  }
}
</style>