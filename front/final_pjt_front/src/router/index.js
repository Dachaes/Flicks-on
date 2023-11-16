import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import GenreView from '@/views/GenreView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/movies/:genre',
      name: 'genre',
      component: GenreView
    },
    {
      path: '/movies/:title',
      name: 'movie_detail',
      component: MovieDetailView
    },
    {
      path: '/profile/:user_name',
      name: 'profile',
      component: ProfileView
    },
  ]
})

// router.beforeEach((to, from) => {
//   const store = useUserStore()
//   if (to.name === 'main' && !store.isLogin) {
//     return { name: 'login' }
//   }
// })

export default router
