<template>
  <div class="footer">
    <div class="copyright">
      <p class="m-0">&copy; 삼성 청년 소프트웨어 아카데미 - 대전 2반 9조</p>
    </div>
    <div class="links">
      <img src="@/assets/github/github.png" alt="github" width="20">
      <a href="https://github.com/dachaes"> 전소현 </a>
      <a href="https://github.com/nastorond">박수형</a>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.footer {
  margin-top: 150px;
  width: 100%;
  height: 120px;
  background-color: #f5f5f5;
  padding: 20px;
}

.copyright {
  float: left;
  margin: 0px;
}

.links {
  margin-top: 60px;
  float: right;
}

.links img {
  margin-right: 10px;
}

.links a {
  color: #000;
  text-decoration: none;
  margin-right: 10px;
}
</style>