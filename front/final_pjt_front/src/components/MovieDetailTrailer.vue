<template>
  <div v-if="notExist">
    <div class="trailers" >
      <iframe v-for="Url in youtubeEmbedUrl" :key="Url" class="trailer"
        width="560"
        height="315"
        :src="Url"
        frameborder="0"
        allow="fullscreen; accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
  </div>
  <div v-else>

  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { onBeforeRouteUpdate } from 'vue-router'

const props = defineProps({
    tmdbId: String
  })

const notExist = ref(true)


const TMDB_API_TOKEN = ref(import.meta.env.VITE_TMDB_API_TOKEN)
const keys = ref([])
const youtubeEmbedUrl = ref([])

const getMovieTrailler = () => {
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
      keys.value[3] = response.data.results[3].key
  
      // const youtubeEmbedUrl = `https://www.youtube.com/embed/${url}`
      // const youtubeEmbedUrl = computed(() => `https://www.youtube.com/embed/${props.movieTrailer}`)
      youtubeEmbedUrl.value[0] = `https://www.youtube.com/embed/${keys.value[0]}`
      youtubeEmbedUrl.value[1] = `https://www.youtube.com/embed/${keys.value[1]}`
      youtubeEmbedUrl.value[2] = `https://www.youtube.com/embed/${keys.value[2]}`
      youtubeEmbedUrl.value[3] = `https://www.youtube.com/embed/${keys.value[3]}`
    })
    .catch(function (error) {
      console.error(error);
    });
}

  onMounted(() => {
  getMovieTrailler()
})

onBeforeRouteUpdate((to, from) => {
  props.tmdbId = to.params.title
  getMovieTrailler()
})

</script>

<style scoped>
.trailers {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

@media (min-width: 576px) {
  .trailer {
    width: 500px;
    height: 300px;
    border: 1px solid #ccc;
  }
}

@media (min-width: 768px) {
  .trailer {
    width: 350px;
    height: 210px;
    border: 1px solid #ccc;
  }
}

@media (min-width: 992px) {
  .trailer {
    width: 440px;
    height: 260px;
    border: 1px solid #ccc;
  }
}


@media (min-width: 1200px) {
  .trailer {
    width: 520px;
    height: 300px;
    border: 1px solid #ccc;
  }
}
</style>