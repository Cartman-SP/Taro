<template>
  <div class="main_page">
    <p class="header">Значение карт</p>
    <div class="header_nav_container">
      <div 
        v-for="(nav, index) in headerNavs" 
        :key="index" 
        :class="['header_nav', { active: selectedNav === index }]" 
        @click="selectNav(index)"
      >
        <img v-if="index === 0" src="../../img/crown.svg" alt="crown">
        <img v-if="index === 1" src="../../img/staff.svg" alt="staff">
        <img v-if="index === 2" src="../../img/pentacle.svg" alt="pentacle">
        <img v-if="index === 3" src="../../img/kubok.svg" alt="kubok">
        <img v-if="index === 4" src="../../img/sword.svg" alt="sword">
      </div>
    </div>
    <div class="main_container">
      <div v-if="selectedNav === 0" class="selectedNav">
        <p class="head">Старшие арканы</p>
        <div class="card_container">
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/77.jpg" alt="">
            <p class="card_text">Дурак</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/8.jpg" alt="">
            <p class="card_text">Маг</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/9.jpg" alt="">
            <p class="card_text">Верховная жрица</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/70.jpg" alt="">
            <p class="card_text">Императрица</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/18.jpg" alt="">
            <p class="card_text">Император</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/59.jpg" alt="">
            <p class="card_text">Иерофант</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/24.jpg" alt="">
            <p class="card_text">Влюбленные</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/29.jpg" alt="">
            <p class="card_text">Колесница</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/34.jpg" alt="">
            <p class="card_text">Сила</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/75.jpg" alt="">
            <p class="card_text">Отшельник</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/78.jpg" alt="">
            <p class="card_text">Колесо Фортуны</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/45.jpg" alt="">
            <p class="card_text">Правосудие</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/48.jpg" alt="">
            <p class="card_text">Повешанный</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/49.jpg" alt="">
            <p class="card_text">Смерть</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/52.jpg" alt="">
            <p class="card_text">Умеренность</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/1.jpg" alt="">
            <p class="card_text">Дьявол</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/54.jpg" alt="">
            <p class="card_text">Башня</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/69.jpg" alt="">
            <p class="card_text">Звезда</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/63.jpg" alt="">
            <p class="card_text">Луна</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/53.jpg" alt="">
            <p class="card_text">Солнце</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/56.jpg" alt="">
            <p class="card_text">Суд</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/55.jpg" alt="">
            <p class="card_text">Мир</p>
          </div>
        </div>
      </div>
      <div v-if="selectedNav === 1" class="selectedNav">
        <p class="head">Жезлы</p>
        <div class="card_container">
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/66.jpg" alt="">
            <p class="card_text">Туз Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/10.jpg" alt="">
            <p class="card_text">Двойка жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/14.jpg" alt="">
            <p class="card_text">Тройка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/17.jpg" alt="">
            <p class="card_text">Четвёрка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/22.jpg" alt="">
            <p class="card_text">Пятёрка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/25.jpg" alt="">
            <p class="card_text">Шестёрка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/30.jpg" alt="">
            <p class="card_text">Семёрка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/65.jpg" alt="">
            <p class="card_text">Восьмёрка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/38.jpg" alt="">
            <p class="card_text">Девятка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/42.jpg" alt="">
            <p class="card_text">Десятка Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/47.jpg" alt="">
            <p class="card_text">Паж Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/74.jpg" alt="">
            <p class="card_text">Рыцарь Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/50.jpg" alt="">
            <p class="card_text">Дама Жезлов</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/60.jpg" alt="">
            <p class="card_text">Король Жезлов</p>
          </div>
        </div>
      </div>
      <div v-if="selectedNav === 2" class="selectedNav">
        <p class="head">Пентакли</p>
        <div class="card_container">
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/61.jpg" alt="">
            <p class="card_text">Туз Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/13.jpg" alt="">
            <p class="card_text">Двойка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/67.jpg" alt="">
            <p class="card_text">Тройка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/68.jpg" alt="">
            <p class="card_text">Четвёрка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/71.jpg" alt="">
            <p class="card_text">Пятёрка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/27.jpg" alt="">
            <p class="card_text">Шестёрка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/33.jpg" alt="">
            <p class="card_text">Семёрка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/37.jpg" alt="">
            <p class="card_text">Восьмёрка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/41.jpg" alt="">
            <p class="card_text">Девятка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/2.jpg" alt="">
            <p class="card_text">Десятка Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/76.jpg" alt="">
            <p class="card_text">Паж Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/4.jpg" alt="">
            <p class="card_text">Рыцарь Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/51.jpg" alt="">
            <p class="card_text">Дама Пентаклей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/58.jpg" alt="">
            <p class="card_text">Король Пентаклей</p>
          </div>
        </div>
      </div>
      <div v-if="selectedNav === 3" class="selectedNav">
        <p class="head">Кубки</p>
        <div class="card_container">
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/64.jpg" alt="">
            <p class="card_text">Туз Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/11.jpg" alt="">
            <p class="card_text">Двойка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/15.jpg" alt="">
            <p class="card_text">Тройка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/19.jpg" alt="">
            <p class="card_text">Четвёрка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/21.jpg" alt="">
            <p class="card_text">Пятёрка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/26.jpg" alt="">
            <p class="card_text">Шестёрка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/31.jpg" alt="">
            <p class="card_text">Семерка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/35.jpg" alt="">
            <p class="card_text">Восьмёрка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/39.jpg" alt="">
            <p class="card_text">Девятка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/43.jpg" alt="">
            <p class="card_text">Десятка Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/46.jpg" alt="">
            <p class="card_text">Паж Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/73.jpg" alt="">
            <p class="card_text">Рыцарь Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/72.jpg" alt="">
            <p class="card_text">Дама Кубков</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/57.jpg" alt="">
            <p class="card_text">Король Кубков</p>
          </div>
        </div>
      </div>
      <div v-if="selectedNav === 4" class="selectedNav">
        <p class="head">Мечи</p>
        <div class="card_container">
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/62.jpg" alt="">
            <p class="card_text">Туз Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/12.jpg" alt="">
            <p class="card_text">Двойка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/16.jpg" alt="">
            <p class="card_text">Тройка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/20.jpg" alt="">
            <p class="card_text">Четвёрка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/23.jpg" alt="">
            <p class="card_text">Пятёрка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/28.jpg" alt="">
            <p class="card_text">Шестёрка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/32.jpg" alt="">
            <p class="card_text">Семерка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/36.jpg" alt="">
            <p class="card_text">Восьмёрка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/40.jpg" alt="">
            <p class="card_text">Девятка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/44.jpg" alt="">
            <p class="card_text">Десятка Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/6.jpg" alt="">
            <p class="card_text">Паж Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/5.jpg" alt="">
            <p class="card_text">Рыцарь Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/7.jpg" alt="">
            <p class="card_text">Дама Мечей</p>
          </div>
          <div class="card" @click="navigateToCard">
            <img :class="{ subscribed: issubbed }" src="../../img/taro/3.jpg" alt="">
            <p class="card_text">Король Мечей</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedNav: 0,
      headerNavs: [0, 1, 2, 3, 4]
    };
  },
  methods: {
    selectNav(index) {
      this.selectedNav = index;
    },
    navigateToCard() {
      if (this.issubbed) {
        this.$router.push('/card/significance');
      } else {
        this.$router.push('/card/banned');
      }
    }
  },
  computed:{
    issubbed(){
      return  Math.ceil((new Date(this.$store.state.data.sub_date) - new Date()) / (1000 * 3600 * 24)) > 0
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
}
.header {
  font-family: Mulish Regular;
  font-size: 24px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.head {
  font-family: Mulish Regular;
  font-size: 18px;
  line-height: 18px;
  letter-spacing: 0.01em;
  color: #FFFFFF;
  text-align: center;
}
.header_nav_container {
  display: flex;
  gap: 15px;
}
.card_container{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  gap: 20px;
}
.card_text{
  font-family: Mulish Regular;
  font-size: 12px;
  line-height: 18px;
  letter-spacing: 0.01em;
  color: #FFFFFF;
  text-align: center;  
}
.header_nav {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 65px;
  height: 65px;
  background: rgba(127, 127, 127, 0.35);
  border-radius: 18px;
  cursor: pointer;
  outline: none;
}
.header_nav:focus {
  outline: none;
}
.header_nav.active {
  background: rgba(180, 94, 209, 0.8);
}
.main_container {
  width: 100%;
  padding: 20px;
  padding-top: 0;
  border-radius: 18px;
  text-align: center;
}
.header_nav img {
  width: 45px;
  height: 45px;
}
.card img{
  width: 100%;
  height: 90%;
  border-radius: 5px;
  filter: grayscale(100%);
}
.selectedNav{
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.card img.subscribed {
  filter: none;
}
</style>
