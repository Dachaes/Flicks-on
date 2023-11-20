import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userName = ref('')
  const userPk = ref(0)
  const isLogin = computed(() => {
    return token.value === null ? false : true
  })

  const signUp = function (payload) {
    const { username, nickname, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data:{
        username,
        nickname,
        password1,
        password2,
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data:{
        username,
        password,
      }
    })
      .then((res) => {
        console.log(res)
        token.value = res.data.key
        // console.log(this)
        
        axios({
          method:'get',
          url: `${API_URL}/accounts/user/`,
          headers:{
            'Authorization': `Token ${token.value}`
          }
        })
        .then((res) => {
          userName.value = res.data.nickname
          userPk.value = res.data.pk
          console.log(res)
          console.log(res.data)
          console.log(res.data.pk)
          })
          .catch((err) => console.log(err))
        // 임시로 main으로 전송
        // 추후 수정
        router.push({ name:'main' })
      })
      .catch((err) => {
          console.log(err)
        })
    }
    
    const logOut = function () {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
      .then((res) => {
        userName.value = ''
        token.value = null
        userName.value = ''
        userPk.value = 0
        // 임시
        router.push({ name:'login' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { isLogin, API_URL, token, userName, userPk, signUp, logIn, logOut }
}, {persist: true})
