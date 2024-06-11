<template>
  <div class="main">
    <div class="header">
      <div class="header_container">
        <img src="../../img/logo.svg" alt="">
        <p class="header_text">Nickname</p>
      </div>
      <div class="balance_container" @click="toggleModal">
        <p class="balance">Тарифы</p>
      </div>
    </div>
    <div class="ref">
      <div class="ref_left">
        <p class="ref_text">Пригласить друзей</p>
      </div>
      <p class="ref_balance">N дней</p>
    </div>
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
  }
}
</script>

<style scoped>
.main {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header_container {
  display: flex;
  align-items: center;
  gap: 8px;
}
.header_text {
  font-family: Mulish Regular;
  font-size: 28px;
  line-height: 42px;
  text-align: left;
  color: #FFFFFF;
}
.balance_container {
  background: rgba( 23, 33, 43, 0.25 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 4px );
  -webkit-backdrop-filter: blur( 4px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 16px;
  display: flex;
  align-items: center;
  padding: 8px 10px;
}
.balance {
  font-family: Mulish Regular;
  font-size: 20px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
p {
  margin: 0;
}
.ref_left {
  background: rgba( 255, 255, 255, 0.8 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 5.5px );
  -webkit-backdrop-filter: blur( 5.5px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 25px;
  display: flex;
  align-items: center;
  padding: 6px 10px;
}
.ref {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.ref_text {
  font-family: Mulish Regular;
  text-align: left;
  color: #000;
}
.ref_balance {
  font-family: Mulish Regular;
  font-size: 24px;
  text-align: left;
  color: #FFFFFF;
}
img {
  border-radius: 25px;
  width: 65px;
  height: 65px;
}
</style>
