<template>
  <MatrixPage msg="Welcome to Your Vue.js App"/>
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body{
  margin: 0;
  padding: 0;
}
</style>
