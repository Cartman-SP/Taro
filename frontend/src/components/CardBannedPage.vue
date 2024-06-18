<template>
  <div class="main_page">
    <p class="header">Дьявол</p>
    <div class="main_container">
      <img src="../../img/taro/1.jpg" alt="" class="">
      <img src="../../img/taro/1.jpg" alt="" class="reverse">
    </div>
    <div class="significance_container">
      <div class="header_container" @click="toggleModal">
        <p class="significance_header">Прямое значение</p>
        <img src="../../img/lock.svg" alt="">
      </div>
      <div class="header_container" @click="toggleModal">
        <p class="significance_header">Перевернутое значение</p>
        <img src="../../img/lock.svg" alt="">
      </div>
      <div class="header_container" @click="toggleModal">
        <p class="significance_header">Оригинальный текст Вейта</p>
        <img src="../../img/lock.svg" alt="">
      </div>
      <div class="header_container" @click="toggleModal">
        <p class="significance_header">Метафизическая интерпретация</p>
        <img src="../../img/lock.svg" alt="">
      </div>
      <div class="header_container" @click="toggleModal">
        <p class="significance_header">Образный лад</p>
        <img src="../../img/lock.svg" alt="">
      </div>
      <div class="header_container" @click="toggleModal">
        <p class="significance_header">Символизм</p>
        <img src="../../img/lock.svg" alt="">
      </div>
    </div>
    <button @click="toggleModal">Открыть все значения</button>
    <TariffModalPage :isVisible="isModalVisible" @close="toggleModal"/>
  </div>
</template>

<script>
import TariffModalPage from './TariffModalPage.vue';
export default {
  components: {
    TariffModalPage
  },
  data() {
    return {
      isModalVisible: false
    };
  },
  methods: {
    toggleModal() {
      this.isModalVisible = !this.isModalVisible;
    }
  },

}
</script>

<style scoped>
.main_page {
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
  z-index: 100;
}
.header {
  font-family: Mulish Regular;
  font-size: 24px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.main_container img{
  width: 100%;
  border-radius: 5px;
  filter: grayscale(100%);
}
.main_container{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
  gap: 20px;
}
.reverse{
  rotate: 180deg;
}
button{
  font-family: Mulish Regular;
  font-size: 18px;
  line-height: 22px;
  letter-spacing: 0.01em;
  text-align: center;
  width: 80%;
  color: #FFFFFF;
  background: rgba( 180, 94, 209, 0.5 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 6px );
  -webkit-backdrop-filter: blur( 6px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  padding: 8px 10px;
}
.significance_container {
  width: 100%;
  gap: 7px;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}
.header_container {
  padding: 10px;
  background: rgba(164, 164, 164, 0.2);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  border-radius: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.significance_header {
  font-family: Mulish Regular;
  font-size: 16px;
  line-height: 18px;
  letter-spacing: 0.05em;
  text-align: left;
  color: #FFFFFF;
}
</style>