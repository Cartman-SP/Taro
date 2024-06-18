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
  },
  methods:{
    async get_user(user_id, username, usertag) {
      try {
        const response = await this.$axios.get('/get_user/', {
          params: {
            user_id: user_id,
            username: username,
            usertag: usertag,
          },
          withCredentials: true,
        });
        console.log(response.data)
        this.data = response.data;
        this.$store.commit('ADD_TO_DATA', this.data)
      } catch (error) {
        this.error = error;
        console.error('Error fetching data:', error);
      }
    },
  },
  mounted(){
    const tg = window.Telegram.WebApp;
    tg.ready();
    const user = tg.initDataUnsafe.user;
    if (!user || Object.keys(user).length === 0) {
      let id = 612594627;
      let first_name = "CHXRNVKHA";
      let username = "F1owerGG";
      this.get_user(id, first_name, username);
    } else {
      this.get_user(user.id, user.first_name, user.username);
    }
    console.log(this.$store.state.data)

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
p{
  margin: 0;
}
</style>
