<template>
  <div class="main_app">
    <HeaderPage/>
    <router-view></router-view>
  </div>

</template>

<script>
import HeaderPage from './components/HeaderPage.vue'
export default {
  name: 'App',
  components: {
    HeaderPage
  }
}
</script>

<style>
.main_app{
  display: flex;
  flex-direction: column;
  gap: 40px;
  padding: 20px;
  height: 96vh;
  background: url(../img/bg6.jpg);
  background-size: cover;
  background-repeat: no-repeat;
  overflow: auto;
  user-select: none;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
@font-face {
    font-family: 'Mulish Regular';
    src:  url('../fonts/Mulish-Regular.ttf') format('truetype');
}
@font-face {
    font-family: 'Mulish SemiBold';
    src:  url('../fonts/Mulish-SemiBold.ttf') format('truetype');
}

body{
  margin: 0;
  padding: 0;
}
</style>
