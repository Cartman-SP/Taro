<template>
  <div class="main_page">
    <p class="header">Гороскоп {{ sign }} на сегодня</p>
    <div class="subheader_container">
      <p class="subheader">{{ new Date().toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' }) }} - {{ new Date(Date.now() + 24 * 60 * 60 * 1000).toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' }) }}</p>
    </div>
    <div class="main">
      <p class="main_text">{{ data }}</p>
    </div>
    <button class="home_button" @click="goHome">Домой</button>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRoute } from 'vue-router';

export default {
  name: 'GoroscopePage',
  data(){
    return{
      data: '',
      sign:'',
      ensign: '',
    }
  },
  mounted() {
  const route = useRoute();
  this.ensign = ref(route.params.sign);
  this.initializeData(this.ensign);
},
methods: {
  async initializeData() {
    try {
      await this.getHoro();
    } catch (error) {
      console.error('Error initializing data:', error);
    }
  },
  async getSign(sign) {
    const zodiacSigns = {
      aries: 'Овен',
      taurus: 'Телец',
      gemini: 'Близнецы',
      cancer: 'Рак',
      leo: 'Лев',
      virgo: 'Дева',
      libra: 'Весы',
      scorpio: 'Скорпион',
      sagittarius: 'Стрелец',
      capricorn: 'Козерог',
      aquarius: 'Водолей',
      pisces: 'Рыбы'
    };
    this.sign = zodiacSigns[sign.value];
  },
  async getHoro() {
    try {
      const response = await this.$axios.get('/get_goroscope_info/', {
        params: {
          sign: this.ensign,
        },
        withCredentials: true,
      });
      console.log(response)
      this.data = response.data.data.text;
      
    } catch (error) {
      this.error = error;
      console.error('Error fetching data:', error);
    }
  },
  goHome() {
    this.$router.push('/');
  }
}

}
</script>



<style scoped>
.main_page{
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
}
.header{
  font-family: Mulish Semibold;
  font-size: 36px;
  line-height: 42px;
  letter-spacing: 0.01em;
  text-align: center;
  color: #FFFFFF;
  max-width: 300px;
}
.subheader{
  font-family: Mulish Semibold;
  font-size: 14px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: center;
  color: #FFFFFF;
  max-width: 300px;
}
p{
  margin: 0;
}
.main{
  width: 95%;
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.4 );
  padding: 15px;
  word-wrap: break-word;
}
.main_text{
  font-family: Mulish Regular;
  font-size: 16px;
  line-height: 28px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.home_button{
  font-family: Mulish Regular;
  font-size: 18px;
  line-height: 22px;
  letter-spacing: 0.01em;
  text-align: center;
  width: 60%;
  color: #FFFFFF;
  background: rgba( 180, 94, 209, 0.5 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 6px );
  -webkit-backdrop-filter: blur( 6px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  padding: 8px 10px;
}
</style>