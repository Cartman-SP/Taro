<template>
  <div class="main_page">
    <div class="header">
      <div class="header_container">
        <img src="../../img/logo.svg" alt="">
        <p class="header_text">Nickname</p>
      </div>
      <div class="balance_container">
        <p class="balance">Пополнить</p>
      </div>
    </div>
    <div class="ref">
      <div class="ref_left">
        <p class="ref_text">Пригласить друзей</p>
      </div>
      <p class="ref_balance">200 руб</p>
    </div>
    <div class="cards">
      <div class="card_container">
        <div class="taro">
          <p class="taro_text">Карты<br> <span class="span_taro">ТАРО</span></p>
          <img src="../../img/navigate_next.svg" alt="" class="navigate_img">
        </div>
        <div class="natal">
          <p class="natal_text">Натальная<br> <span class="span_natal">карта</span></p>
          <img src="../../img/navigate_next.svg" alt="" class="navigate_img">
        </div>
      </div>
      <div class="matrix">
        <p class="matrix_text">Матрица<br>судьбы</p>
        <div class="circle">
          <img src="../../img/next.svg" alt="">
        </div>
      </div>  
    </div>
    <div class="goroskop">
      <p class="goroskop_text">Гороскоп<br>по знакам зодиака</p>
    </div>
    <div class="slider">
      <div class="slider_card">
        <img src="../../img/Oven.svg" alt="" class="img_slider">
        <p class="slider_text">Овен</p>
      </div>
      <div class="slider_card">
        <img src="../../img/telec.svg" alt="" class="img_slider">
        <p class="slider_text">Телец</p>
      </div>
      <div class="slider_card">
        <img src="../../img/bliz.svg" alt="" class="img_slider">
        <p class="slider_text">Близнецы</p>
      </div>
      <div class="slider_card">
        <img src="../../img/rak.svg" alt="" class="img_slider">
        <p class="slider_text">Рак</p>
      </div>
      <div class="slider_card">
        <img src="../../img/lion.svg" alt="" class="img_slider">
        <p class="slider_text">Лев</p>
      </div>
      <div class="slider_card">
        <img src="../../img/deva.svg" alt="" class="img_slider">
        <p class="slider_text">Дева</p>
      </div>
      <div class="slider_card">
        <img src="../../img/vesi.svg" alt="" class="img_slider">
        <p class="slider_text">Весы</p>
      </div>
      <div class="slider_card">
        <img src="../../img/scorpion.svg" alt="" class="img_slider">
        <p class="slider_text">Скорпион</p>
      </div>
      <div class="slider_card">
        <img src="../../img/strelec.svg" alt="" class="img_slider">
        <p class="slider_text">Стрелец</p>
      </div>
      <div class="slider_card">
        <img src="../../img/kozerog.svg" alt="" class="img_slider">
        <p class="slider_text">Козерог</p>
      </div>
      <div class="slider_card">
        <img src="../../img/fish.svg" alt="" class="img_slider">
        <p class="slider_text">Рыбы</p>
      </div>
      <div class="slider_card">
        <img src="../../img/vodolei.svg" alt="" class="img_slider">
        <p class="slider_text">Водолей</p>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  mounted() {
    const slider = this.$el.querySelector('.slider');
    let isDown = false;
    let startX;
    let scrollLeft;

    slider.addEventListener('mousedown', (e) => {
      isDown = true;
      slider.classList.add('active');
      startX = e.pageX - slider.offsetLeft;
      scrollLeft = slider.scrollLeft;
    });

    slider.addEventListener('mouseleave', () => {
      isDown = false;
      slider.classList.remove('active');
    });

    slider.addEventListener('mouseup', () => {
      isDown = false;
      slider.classList.remove('active');
    });

    slider.addEventListener('mousemove', (e) => {
      if (!isDown) return;
      e.preventDefault();
      const x = e.pageX - slider.offsetLeft;
      const walk = (x - startX) * 3; // Adjust scroll speed
      slider.scrollLeft = scrollLeft - walk;
    });
  }
}
</script>

<style scoped>
.main_page {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
  max-width: 600px;
  height: 1000px;
  background: radial-gradient(163.29% 100% at 50.04% 0%, #010110 0%, #14062E 31.08%, #422989 55.63%, #A951D2 78.65%, #DF84E1 91.15%, #FCA5FE 100%);
}
.header {
  display: flex;
  justify-content: space-between;
}
.header_container {
  display: flex;
  align-items: center;
  gap: 8px;
}
.header_text {
  font-family: Poppins;
  font-size: 28px;
  font-weight: 700;
  line-height: 42px;
  text-align: left;
  color: #FFFFFF;
}
.balance_container {
  background: #17212B;
  border-radius: 25px;
  display: flex;
  align-items: center;
  padding: 8px 12px;
}
.balance {
  font-family: Poppins;
  font-size: 24px;
  font-weight: 700;
  line-height: 42px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
p {
  margin: 0 ;
}
.ref_left {
  background: linear-gradient(338.31deg, #21D1FF 12.39%, #993CFE 70.15%);
  border-radius: 25px;
  display: flex;
  align-items: center;
  padding: 8px 12px;
}
.ref {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.ref_text {
  font-family: Poppins;
  font-size: 20px;
  font-weight: 700;
  line-height: 36px;
  text-align: left;
  color: #FFFFFF;
}
.ref_balance {
  font-family: Poppins;
  font-size: 24px;
  font-weight: 700;
  line-height: 36px;
  text-align: left;
  color: #FFFFFF;
}
.cards {
  display: flex;
  gap: 30px;
}
.card_container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 50%;
}
.taro {
  position: relative;
  background: #FFFFFF;
  border-radius: 25px;
  height: auto;
  padding: 35px 20px;
}
.taro_text {
  font-family: Poppins;
  font-size: 40px;
  font-weight: 700;
  line-height: 32px;
  text-align: left;
  color: #17212B;
}
.span_taro {
  font-family: Poppins;
  font-size: 20px;
  font-weight: 700;
  line-height: 14px;
  text-align: left;
  color: #17212B;
}
.natal {
  position: relative;
  background: #17212B;
  border-radius: 25px;
  padding: 35px 20px;
}
.natal_text {
  font-family: Poppins;
  font-size: 28px;
  font-weight: 700;
  line-height: 32px;
  text-align: left;
  color: #FFFFFF;
}
.span_natal {
  font-family: Poppins;
  font-size: 20px;
  font-weight: 700;
  line-height: 14px;
  text-align: left;
  color: #FFFFFF;
}
.matrix {
  background: #B45ED1;
  border-radius: 25px;
  width: 100%;
  padding: 15px 20px;
  position: relative;
}
.matrix_text {
  color: rgba(255, 255, 255, 1);
  font-family: Poppins;
  font-size: 28px;
  font-weight: 600;
  line-height: 36px;
  text-align: left;
}
.circle {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 175px;
  width: 80px;
  height: 80px;
  background: #FFFFFF;
  border-radius: 150px;
}
.navigate_img {
  width: 32px;
  height: 32px;
  position: absolute;
  top: 60px;
  right: 0;
}
.goroskop_text {
  font-family: Poppins;
  font-size: 32px;
  font-weight: 700;
  line-height: 48px;
  text-align: left;
  color: #FFFFFF;
}
.slider {
  display: flex;
  gap: 30px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}
.slider_card {
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  border-image-source: linear-gradient(180deg, #21D1FF 0%, #993CFE 100%);
  background: rgba( 0, 0, 0, 0.65 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 8px );
  -webkit-backdrop-filter: blur( 8px );
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 15px;
  scroll-snap-align: start;
  min-width: 135px;
}
.slider_text {
  font-family: Poppins;
  font-size: 20px;
  font-weight: 400;
  line-height: 30px;
  text-align: left;
  color: #FFFFFF;
}
.img_slider {
  width: 120px;
  height: 100px;
}
</style>

