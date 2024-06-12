<template>
  <div class="main_page">
    <div class="img_container" v-if="showOnlyOneCardIndex === null">
      <div v-for="(card, index) in cards" :key="index" class="flip-card-container" @click="flipCard(index)">
        <div class="flip-card" :class="{ flipped: card.flipped && showOnlyOneCardIndex === index }">
          <div class="flip-card-front">
            <img :src="require('../../img/Rubashka.jpg')" alt="" class="rubashka"/>
          </div>
          <div class="flip-card-back" v-if="card.flipped && showOnlyOneCardIndex === index">
            <img :src="card.src" alt="" class="tarot-card"/>
          </div>
        </div>
      </div>
    </div>
    <div class="centered-card" v-else>
      <div class="flip-card-container" @click="flipCard(showOnlyOneCardIndex)">
        <div class="flip-card flipped">
          <div class="flip-card-back">
            <img :src="cards[showOnlyOneCardIndex].src" alt="" class="tarot-card"/>
          </div>
        </div>
      </div>

      <div class="significance">
        <p class="significance_text">Пожалуйста, выберите типыфвыфввфывфывфывыф фывфывраскладавв:ddddddddывфывраскладавв:dddddddddddddddddddddывфывраскладавв:ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd</p>
      </div>
      
      <button class="home_button" @click="this.$router.push('/')">Домой</button>

    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cards: Array.from({ length: 9 }, () => ({ flipped: false, src: '' })),
      tarotImages: [
        require('../../img/taro/1.jpg'),
        require('../../img/taro/2.jpg'),
        require('../../img/taro/3.jpg'),
        require('../../img/taro/4.jpg'),
        require('../../img/taro/5.jpg'),
        require('../../img/taro/6.jpg'),
        require('../../img/taro/7.jpg'),
        require('../../img/taro/8.jpg'),
        require('../../img/taro/9.jpg'),
        require('../../img/taro/10.jpg'),
        require('../../img/taro/11.jpg'),
        require('../../img/taro/12.jpg'),
        require('../../img/taro/13.jpg'),
        require('../../img/taro/14.jpg'),
        require('../../img/taro/15.jpg'),
        require('../../img/taro/16.jpg'),
        require('../../img/taro/17.jpg'),
        require('../../img/taro/18.jpg'),
        require('../../img/taro/19.jpg'),
        require('../../img/taro/20.jpg'),
        require('../../img/taro/21.jpg'),
        require('../../img/taro/22.jpg'),
        require('../../img/taro/23.jpg'),
        require('../../img/taro/24.jpg'),
        require('../../img/taro/25.jpg'),
        require('../../img/taro/26.jpg'),
        require('../../img/taro/27.jpg'),
        require('../../img/taro/28.jpg'),
        require('../../img/taro/29.jpg'),
        require('../../img/taro/30.jpg'),
        require('../../img/taro/31.jpg'),
        require('../../img/taro/32.jpg'),
        require('../../img/taro/33.jpg'),
        require('../../img/taro/34.jpg'),
        require('../../img/taro/35.jpg'),
        require('../../img/taro/36.jpg'),
        require('../../img/taro/37.jpg'),
        require('../../img/taro/38.jpg'),
        require('../../img/taro/39.jpg'),
        require('../../img/taro/40.jpg'),
        require('../../img/taro/41.jpg'),
        require('../../img/taro/42.jpg'),
        require('../../img/taro/43.jpg'),
        require('../../img/taro/44.jpg'),
        require('../../img/taro/45.jpg'),
        require('../../img/taro/46.jpg'),
        require('../../img/taro/47.jpg'),
        require('../../img/taro/48.jpg'),
        require('../../img/taro/49.jpg'),
        require('../../img/taro/50.jpg'),
        require('../../img/taro/51.jpg'),
        require('../../img/taro/52.jpg'),
        require('../../img/taro/53.jpg'),
        require('../../img/taro/54.jpg'),
        require('../../img/taro/55.jpg'),
        require('../../img/taro/56.jpg'),
        require('../../img/taro/57.jpg'),
        require('../../img/taro/58.jpg'),
        require('../../img/taro/59.jpg'),
        require('../../img/taro/60.jpg'),
        require('../../img/taro/61.jpg'),
        require('../../img/taro/62.jpg'),
        require('../../img/taro/63.jpg'),
        require('../../img/taro/64.jpg'),
        require('../../img/taro/65.jpg'),
        require('../../img/taro/66.jpg'),
        require('../../img/taro/67.jpg'),
        require('../../img/taro/68.jpg'),
        require('../../img/taro/69.jpg'),
        require('../../img/taro/70.jpg'),
        require('../../img/taro/71.jpg'),
        require('../../img/taro/72.jpg'),
        require('../../img/taro/73.jpg'),
        require('../../img/taro/74.jpg'),
        require('../../img/taro/75.jpg'),
        require('../../img/taro/76.jpg'),
        require('../../img/taro/77.jpg'),
        require('../../img/taro/78.jpg')
      ],
      availableImages: [],
      showOnlyOneCardIndex: null // Индекс карточки, которую нужно показать
    }
  },
  methods: {
    flipCard(index) {
      // Устанавливаем индекс карточки, которую нужно показать
      this.showOnlyOneCardIndex = index;

      // Проверяем, не перевернута ли уже карточка
      if (!this.cards[index].flipped) {
        // Сначала перевернем все карточки в изначальное положение
        this.cards.forEach((card) => {
          card.flipped = false;
        });
        // Затем выберем случайное изображение из списка tarotImages
        const randomIndex = Math.floor(Math.random() * this.tarotImages.length);
        this.cards[index].src = this.tarotImages[randomIndex];
        // И затем перевернем выбранную карточку
        this.cards[index].flipped = true;
      }
    }
  }
}
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.main_page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.img_container {
  width: 100%;
  height: 600px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  gap: 15px;
  margin-bottom: 15px;
  opacity: 0;
  animation: fadeIn 2.5s ease forwards;
}
.rubashka {
  width: 100%;
  border-radius: 5px;
  object-fit: cover;
}
p {
  margin: 0;
}
button {
  color: #FFFFFF;
  background: #6266EA;
  border: none;
  cursor: pointer;
  display: flex;
  height: 36px;
  padding: 10px 14px;
  justify-content: center;
  align-items: center;
  gap: 5px;
  border-radius: 3px;
  transition: all .2s ease;
  font-family: "Mulish Regular";
}
.matrix_img {
  border-radius: 10px;
}
.flip-card-container {
  perspective: 1000px;
}

.flip-card {
  width: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1.5s;
}

.flip-card.flipped {
  transform: rotateY(180deg);
  height: 100%;
}

.flip-card-front {
  position: absolute;
  top: 0;
  left: 0;
}

.flip-card-back {
  height: 100%;
  transform: rotateY(180deg);
}

.centered-card {
  display: flex;
  flex-direction: column;
  gap: 20px;
  justify-content: center;
  align-items: center;
  animation: fadeIn 2.5s ease;
}
.img_container.fade-out {
  animation: fadeOut 2.5s ease forwards;
}
.tarot-card {
  width: 80%;
  height: auto;
  max-width: 300px;
  border-radius: 5px;
}
.significance{
  width: 80%;
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.4 );
  padding: 15px;
  opacity: 0;
  animation: fadeIn 1s ease forwards;
  word-wrap: break-word;
}
.significance_text{
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 18px;
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
