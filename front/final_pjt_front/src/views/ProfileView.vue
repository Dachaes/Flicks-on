<template>
  <div>
    <Headers />
    <ProfileDetail />
    <PersonalizedService />
    <Footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import ProfileDetail from '@/components/ProfileDetail.vue'
  import PersonalizedService from '@/components/PersonalizedService.vue'
  import Footers from '@/components/Footers.vue'
  import { useUserStore } from '../stores/users'
  import { onMounted } from 'vue'

  const userStore = useUserStore()

  onMounted(() => {
    userStore.getUserDetail()
  })

</script>

<style scoped>

</style>