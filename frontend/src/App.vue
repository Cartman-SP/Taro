<template>
  <div class="main_app">
    <MatrixPage/>
  </div>

</template>

<script>
import MatrixPage from './components/MatrixPage.vue'
export default {
  name: 'App',
  components: {
    MatrixPage
  }
}
</script>

<style>
.main_app{
  padding: 20px;
  max-width: 600px;
  height: 100vh;
  background: url(../img/bg1.jpg);
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
