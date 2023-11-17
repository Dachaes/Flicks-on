<template>
  <div>
    <Headers />
    <h1>프로필 뷰</h1>
    <ProfileDetail />
    <PersonalizedService />
    <CommentList />
    <Footers />
  </div>
</template>

<script setup>
  import Headers from '@/components/Headers.vue'
  import ProfileDetail from '@/components/ProfileDetail.vue'
  import PersonalizedService from '@/components/PersonalizedService.vue'
  import CommentList from '@/components/CommentList.vue'
  import Footers from '@/components/Footers.vue'
</script>

<style scoped>

</style>