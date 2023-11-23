import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userNickName = ref('')
  const userPk = ref(0)
  const userData = ref(null)
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
        const password = password1
        axios({
          method: 'post',
          url: `${API_URL}/accounts/login/`,
          data:{
            username,
            password,
          }
        })
      .then((res) => {
        token.value = res.data.key
        axios({
          method:'get',
          url: `${API_URL}/accounts/user/`,
          headers:{
            'Authorization': `Token ${token.value}`
          }
      })
      .then((res) => {
        userData.value = res.data
        userNickName.value = res.data.nickname
        userPk.value = res.data.pk
        router.push({name:'init', params:{user_pk: res.data.pk}})
      })
      })
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
        getUserDetail()
        console.log(res)
        token.value = res.data.key
        router.push({ name:'main' })
      })
      .catch(err => {
        alert('입력하신 정보가 올바르지 않습니다.')
      })
    }
    
    const logOut = function () {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
      })
      .then((res) => {
        userNickName.value = ''
        token.value = null
        userPk.value = 0
        userData.value = []
        // 임시
        router.push({ name:'login' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getUserDetail = function () {
    axios({
      method:'get',
      url: `${API_URL}/accounts/user/`,
      headers:{
        'Authorization': `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(res.data.usergenre_set)
        userData.value = res.data
        userNickName.value = res.data.nickname
        userPk.value = res.data.pk
      })
      .catch(err => console.log(err))
  }

  const updateUserDetail = function (payload) {
    const { email, nickName, firstName, lastName, age } = payload
    axios({
      method: 'patch',
      url: `${API_URL}/accounts/user/`,
      headers:{
        'Authorization': `Token ${token.value}`
      },
      data:{
        email: email,
        first_name:firstName,
        last_name:lastName,
        nickname:nickName,
        age: age,
      }
    })
      .then((res) => {
        router.push({name:'profile', params:{user_name:userPk.value}})
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const updateUserImage = function (image) {
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/addimage/${userPk.value}/`,
      data:{
        img:image
      }
    })
      .then((res) => {
        console.log('image@@@@@@@@@@@@@@@@@@@@@@@@@@')
        console.log(res)
      })
      .catch((err) => {
        console.log('image error @@@@@@@@@@@@@@@@@@@@@@@@@@')
        console.log(err)
      })
  }

  // const deleteUser = function () {
  //   axios({
  //     method: 'patch',
  //     url: `${API_URL}/accounts/user/`,
  //     headers:{
  //       'Authorization': `Token ${token.value}`
  //     },
  //     data:{
  //       is_acitve: 0,
  //     }
  //   })
  //     .then((res) => {
  //       console.log(res)
  //       logOut()
  //       router.push({name:'profile', params:{user_name:userPk.value}})
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }

  return { isLogin, API_URL, token, userNickName, userPk, userData, signUp, logIn, logOut, getUserDetail, updateUserDetail, updateUserImage }
}, {persist: true})
