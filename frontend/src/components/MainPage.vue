<template>
  <div class="main_page">
    <div class="cards">
      <div class="card_container">
        <div class="taro" @click="this.$router.push('/chat')">
          <p class="taro_text">Таро<br> <span class="span_taro">чат</span></p>
          <img src="../../img/navigate_next.svg" alt="" class="navigate_img">
        </div>
        <div class="natal" @click="this.$router.push('/natal')">
          <p class="natal_text">Карта<br> <span class="span_natal">дня</span></p>
          <img src="../../img/navigate_next.svg" alt="" class="navigate_img">
        </div>
      </div>
      <div class="matrix" @click="this.$router.push('/matrix')">
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
      <div class="slider_card" @click="this.$router.push('/goroscope')">
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
}
p {
  margin: 0 ;
}
.cards {
  display: flex;
  gap: 20px;
}
.card_container {
  display: flex;
  flex-direction: column;
  gap: 15px;
  width: 50%;
}
.taro {
  position: relative;
  background: rgba( 180, 94, 209, 0.65 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  -webkit-backdrop-filter: blur( 3px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 25px;
  height: auto;
  padding: 35px 20px;
}
.taro_text {
  font-family: Mulish Regular;
  font-size: 40px;
  line-height: 32px;
  text-align: left;
  color: #FFFFFF;
}
.span_taro {
  font-family: Mulish Regular;
  font-size: 20px;
  line-height: 14px;
  text-align: left;
  color: #FFFFFF;
}
.natal {
  position: relative;
  background: rgba( 180, 94, 209, 0.65 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  -webkit-backdrop-filter: blur( 3px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 25px;
  padding: 35px 20px;
}
.natal_text {
  font-family: Mulish Regular;
  font-size: 28px;
  line-height: 32px;
  text-align: left;
  color: #FFFFFF;
}
.span_natal {
  font-family: Mulish Regular;
  font-size: 24px;
  line-height: 14px;
  text-align: left;
  color: #FFFFFF;
}
.matrix {
  background: rgba( 180, 94, 209, 0.65 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  -webkit-backdrop-filter: blur( 3px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 25px;
  width: 40%;
  padding: 15px 20px;
  position: relative;
}
.matrix_text {
  color: rgba(255, 255, 255, 1);
  font-family: Mulish Regular;
  font-size: 28px;
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
  font-family: Mulish Regular;
  font-size: 32px;
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
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 8px );
  -webkit-backdrop-filter: blur( 8px );
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border-radius: 15px;
  scroll-snap-align: start;
  min-width: 135px;
}
.slider_text {
  font-family: Mulish Regular;
  font-size: 20px;
  line-height: 30px;
  text-align: left;
  color: #FFFFFF;
}
.img_slider {
  width: 120px;
  height: 100px;
}
</style>

