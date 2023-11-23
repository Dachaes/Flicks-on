<template>
  <div class="recommendation-message">
    <h3 class="message">{{ userStore.userNickName }} 님을 위한 맞춤 추천이에요!</h3>
    <div class="detail-analysis">
      <h4 class="detail-message" @click="analysisUser">취향 분석</h4>
      <img width="25" height="25" src="https://img.icons8.com/metro/26/FFFFFF/long-arrow-right.png" alt="long-arrow-right"/>
    </div>
  </div>

  <div class="movies-container"  v-if="userRecommendList">
    <div class="movies" v-for="movie in userRecommendList" :key="movie.id">
      <div v-if="movie.poster_path === null">
        <img class="movie-poster" @click="goPage(movie.tmdb_id)"
      src="@/assets/movie/movieAltImage.png" alt="movie_poster">
      </div>
      <div v-else>
        <img class="movie-poster" @click="goPage(movie.tmdb_id)" :src="movie.poster_path" alt="movie_poster">
      </div>
      <p class="movie-title">{{ movie.title }}</p>
      <div class="movie-rating">
        <img class="movie-heart" src="@/assets/likes/heart2.png" width="17" alt="">
        <p class="movie-rate">{{ movie.movie_rate }}</p>
      </div>
    </div>
  </div>
  <div v-else>
    <div class="windows8">
      <div class="wBall" id="wBall_1">
        <div class="wInnerBall"></div>
      </div>
      <div class="wBall" id="wBall_2">
        <div class="wInnerBall"></div>
      </div>
      <div class="wBall" id="wBall_3">
        <div class="wInnerBall"></div>
      </div>
      <div class="wBall" id="wBall_4">
        <div class="wInnerBall"></div>
      </div>
      <div class="wBall" id="wBall_5">
        <div class="wInnerBall"></div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useUserStore } from '../stores/users';
import axios from 'axios'
import { ref, onMounted } from 'vue';

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const userRecommendList = ref(null)
  
const analysisUser = () => {
  return alert('아직 준비중이에요! 🥰')
}

const getRecommendMovie = () => {
  axios({
    method: 'post',
    url: `${userStore.API_URL}/api/v1/movies/recommend/${userStore.userPk}/`,
    data:{
      user_genre: userStore.userData.usergenre_set
    }
  })
    .then((res) => {
      const uniqueMovies = removeDuplicates(res.data);
      userRecommendList.value = uniqueMovies.slice(0, 20);
    })
    .catch(err => console.log(err))
}

// Helper function to remove duplicates from an array of objects
const removeDuplicates = (array) => {
  const uniqueArray = array.filter((item, index, self) =>
    index === self.findIndex(obj => JSON.stringify(obj) === JSON.stringify(item))
  );
  return uniqueArray;
};

const goPage = (movieId) => {
  router.push({name:'movie_detail', params:{title:movieId}})
}

onMounted(() => {
  getRecommendMovie()
  console.log(userStore.userData.usergenre_set)
})

</script>

<style scoped>
  .recommendation-message {
    margin-top: 60px;
    margin-left: 3%;
    margin-right: auto;
    margin-bottom: -10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .detail-analysis {
    display: flex;
    align-items: center;
	cursor: pointer;
  }
  .detail-analysis:hover {
    display: flex;
    align-items: center;
	cursor: pointer;
	opacity: 50%;
  }

  .detail-analysis img {
    margin: 0 10px 10px;

  }
  .movies-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px;
  }

  .movies {
    margin: 10px;
    padding: 10px;
    background-color: #1f1f1f;
    border-radius: 10px;
    text-align: center;
    width: 197px;
    height: 410px;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
  }

  .movie-poster {
    width: 100%;
    height: 280px;
    object-fit: cover;
    cursor: pointer;
  }

  .movie-poster:hover {
    width: 100%;
    height: 280px;
    object-fit: cover;
    opacity: 0.5;
  }

  .movie-title {
    font-size: 18px;
    margin: 5px 0px 10px;
  }

  .movie-title:hover {
    font-size: 18px;
    margin: 5px 0px 10px;
    opacity: 0.5;
  }

  .movie-rating {  
    display: flex;
    position: absolute;
    align-items: center;
    justify-content: space-between;
    margin: 365px 0px 0px;
  }

  .movie-heart {
    width: 17px;
    height: 17px;
    margin: 6px 6px 25px;
  }

  .movie-rate {
    font-size: 16px;
    font-weight: bold;
    color: rgb(170, 170, 170);
  }

  .windows8 {
	position: relative;
	width: 48px;
	height:48px;
	margin:auto;
  margin-top: 100px;
}

.windows8 .wBall {
	position: absolute;
	width: 46px;
	height: 46px;
	opacity: 0;
	transform: rotate(225deg);
		-o-transform: rotate(225deg);
		-ms-transform: rotate(225deg);
		-webkit-transform: rotate(225deg);
		-moz-transform: rotate(225deg);
	animation: orbit 4.8425s infinite;
		-o-animation: orbit 4.8425s infinite;
		-ms-animation: orbit 4.8425s infinite;
		-webkit-animation: orbit 4.8425s infinite;
		-moz-animation: orbit 4.8425s infinite;
}

.windows8 .wBall .wInnerBall{
	position: absolute;
	width: 6px;
	height: 6px;
	background: rgb(204,204,204);
	left:0px;
	top:0px;
	border-radius: 6px;
}

.windows8 #wBall_1 {
	animation-delay: 1.056s;
		-o-animation-delay: 1.056s;
		-ms-animation-delay: 1.056s;
		-webkit-animation-delay: 1.056s;
		-moz-animation-delay: 1.056s;
}

.windows8 #wBall_2 {
	animation-delay: 0.203s;
		-o-animation-delay: 0.203s;
		-ms-animation-delay: 0.203s;
		-webkit-animation-delay: 0.203s;
		-moz-animation-delay: 0.203s;
}

.windows8 #wBall_3 {
	animation-delay: 0.4265s;
		-o-animation-delay: 0.4265s;
		-ms-animation-delay: 0.4265s;
		-webkit-animation-delay: 0.4265s;
		-moz-animation-delay: 0.4265s;
}

.windows8 #wBall_4 {
	animation-delay: 0.6295s;
		-o-animation-delay: 0.6295s;
		-ms-animation-delay: 0.6295s;
		-webkit-animation-delay: 0.6295s;
		-moz-animation-delay: 0.6295s;
}

.windows8 #wBall_5 {
	animation-delay: 0.843s;
		-o-animation-delay: 0.843s;
		-ms-animation-delay: 0.843s;
		-webkit-animation-delay: 0.843s;
		-moz-animation-delay: 0.843s;
}



@keyframes orbit {
	0% {
		opacity: 1;
		z-index:99;
		transform: rotate(180deg);
		animation-timing-function: ease-out;
	}

	7% {
		opacity: 1;
		transform: rotate(300deg);
		animation-timing-function: linear;
		origin:0%;
	}

	30% {
		opacity: 1;
		transform:rotate(410deg);
		animation-timing-function: ease-in-out;
		origin:7%;
	}

	39% {
		opacity: 1;
		transform: rotate(645deg);
		animation-timing-function: linear;
		origin:30%;
	}

	70% {
		opacity: 1;
		transform: rotate(770deg);
		animation-timing-function: ease-out;
		origin:39%;
	}

	75% {
		opacity: 1;
		transform: rotate(900deg);
		animation-timing-function: ease-out;
		origin:70%;
	}

	76% {
	opacity: 0;
		transform:rotate(900deg);
	}

	100% {
	opacity: 0;
		transform: rotate(900deg);
	}
}

@-o-keyframes orbit {
	0% {
		opacity: 1;
		z-index:99;
		-o-transform: rotate(180deg);
		-o-animation-timing-function: ease-out;
	}

	7% {
		opacity: 1;
		-o-transform: rotate(300deg);
		-o-animation-timing-function: linear;
		-o-origin:0%;
	}

	30% {
		opacity: 1;
		-o-transform:rotate(410deg);
		-o-animation-timing-function: ease-in-out;
		-o-origin:7%;
	}

	39% {
		opacity: 1;
		-o-transform: rotate(645deg);
		-o-animation-timing-function: linear;
		-o-origin:30%;
	}

	70% {
		opacity: 1;
		-o-transform: rotate(770deg);
		-o-animation-timing-function: ease-out;
		-o-origin:39%;
	}

	75% {
		opacity: 1;
		-o-transform: rotate(900deg);
		-o-animation-timing-function: ease-out;
		-o-origin:70%;
	}

	76% {
	opacity: 0;
		-o-transform:rotate(900deg);
	}

	100% {
	opacity: 0;
		-o-transform: rotate(900deg);
	}
}

@-ms-keyframes orbit {
	0% {
		opacity: 1;
		z-index:99;
		-ms-transform: rotate(180deg);
		-ms-animation-timing-function: ease-out;
	}

	7% {
		opacity: 1;
		-ms-transform: rotate(300deg);
		-ms-animation-timing-function: linear;
		-ms-origin:0%;
	}

	30% {
		opacity: 1;
		-ms-transform:rotate(410deg);
		-ms-animation-timing-function: ease-in-out;
		-ms-origin:7%;
	}

	39% {
		opacity: 1;
		-ms-transform: rotate(645deg);
		-ms-animation-timing-function: linear;
		-ms-origin:30%;
	}

	70% {
		opacity: 1;
		-ms-transform: rotate(770deg);
		-ms-animation-timing-function: ease-out;
		-ms-origin:39%;
	}

	75% {
		opacity: 1;
		-ms-transform: rotate(900deg);
		-ms-animation-timing-function: ease-out;
		-ms-origin:70%;
	}

	76% {
	opacity: 0;
		-ms-transform:rotate(900deg);
	}

	100% {
	opacity: 0;
		-ms-transform: rotate(900deg);
	}
}

@-webkit-keyframes orbit {
	0% {
		opacity: 1;
		z-index:99;
		-webkit-transform: rotate(180deg);
		-webkit-animation-timing-function: ease-out;
	}

	7% {
		opacity: 1;
		-webkit-transform: rotate(300deg);
		-webkit-animation-timing-function: linear;
		-webkit-origin:0%;
	}

	30% {
		opacity: 1;
		-webkit-transform:rotate(410deg);
		-webkit-animation-timing-function: ease-in-out;
		-webkit-origin:7%;
	}

	39% {
		opacity: 1;
		-webkit-transform: rotate(645deg);
		-webkit-animation-timing-function: linear;
		-webkit-origin:30%;
	}

	70% {
		opacity: 1;
		-webkit-transform: rotate(770deg);
		-webkit-animation-timing-function: ease-out;
		-webkit-origin:39%;
	}

	75% {
		opacity: 1;
		-webkit-transform: rotate(900deg);
		-webkit-animation-timing-function: ease-out;
		-webkit-origin:70%;
	}

	76% {
	opacity: 0;
		-webkit-transform:rotate(900deg);
	}

	100% {
	opacity: 0;
		-webkit-transform: rotate(900deg);
	}
}

@-moz-keyframes orbit {
	0% {
		opacity: 1;
		z-index:99;
		-moz-transform: rotate(180deg);
		-moz-animation-timing-function: ease-out;
	}

	7% {
		opacity: 1;
		-moz-transform: rotate(300deg);
		-moz-animation-timing-function: linear;
		-moz-origin:0%;
	}

	30% {
		opacity: 1;
		-moz-transform:rotate(410deg);
		-moz-animation-timing-function: ease-in-out;
		-moz-origin:7%;
	}

	39% {
		opacity: 1;
		-moz-transform: rotate(645deg);
		-moz-animation-timing-function: linear;
		-moz-origin:30%;
	}

	70% {
		opacity: 1;
		-moz-transform: rotate(770deg);
		-moz-animation-timing-function: ease-out;
		-moz-origin:39%;
	}

	75% {
		opacity: 1;
		-moz-transform: rotate(900deg);
		-moz-animation-timing-function: ease-out;
		-moz-origin:70%;
	}

	76% {
	opacity: 0;
		-moz-transform:rotate(900deg);
	}

	100% {
	opacity: 0;
		-moz-transform: rotate(900deg);
	}
}
</style>