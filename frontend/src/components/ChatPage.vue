<template>
  <div class="main_page">
    <div class="start" v-if="selectedCards === 0">
      <p class="chat_text">Чат начат</p>
      <div class="choice">
        <p class="choice_text">Пожалуйста, выберите тип расклада:</p>
      </div>
      <div class="cards_container">
        <div class="cards" @click="selectCards(1)">
          <div class="card">
            <p class="card_number">1</p>
          </div>
          <p class="number">1 карта</p>
        </div>
        <div class="cards" @click="selectCards(3)">
          <div class="wrapper">
            <div class="card">
              <p class="card_number">1</p>
            </div>
            <div class="card">
              <p class="card_number">2</p>
            </div>
            <div class="card">
              <p class="card_number">3</p>
            </div>
          </div>
          <p class="number">3 карты</p>
        </div>
        <div class="cards_1" @click="selectCards(6)">
          <div class="wrapper">
            <div class="card">
              <p class="card_number">1</p>
            </div>
            <div class="card">
              <p class="card_number">2</p>
            </div>
            <div class="card">
              <p class="card_number">3</p>
            </div>
            <div class="card">
              <p class="card_number">4</p>
            </div>
            <div class="card">
              <p class="card_number">5</p>
            </div>
            <div class="card">
              <p class="card_number">6</p>
            </div>
          </div>
          <p class="number">6 карт</p>
        </div>
      </div>
    </div>

    <div v-else>
      <p class="chat_text">Чат начат</p>
      <div class="hello hello1">
        <p class="hello_text">Приветствую тебя. Я жду твой вопрос, чтобы использовать мою удивительную способность видеть за завесой времени.</p>
      </div>
      <div class="hello hello2">
        <p class="hello_text">Пожалуйста, расскажи мне о твоем вопросе, и мы вместе попытаемся раскроить его с помощью карт.</p>
      </div>
      <input v-if="!submittedQuestion" type="text" placeholder="Введите свой вопрос к Таро сюда" class="question_input" v-model="userQuestion" @keyup.enter="submitQuestion">
      <button v-if="submittedQuestion && !showAnswer" class="answer_button" :class="{ purple: allCardsFlipped }" @click="revealAnswer">Узнать ответ</button>
      <button v-else-if="submittedQuestion && showAnswer" class="home_button" @click="this.$router.push('/')">Домой</button>
      <div class="question" v-if="submittedQuestion">
        <p class="question_text">{{ submittedQuestion }}</p>
      </div>
      <div class="img_container" v-if="submittedQuestion" :style="{ height: imgContainerHeight }">
        <div v-for="(card, index) in cards" :key="index" class="flip-card-container" @click="flipCard(index)">
          <div class="flip-card" :class="{ flipped: card.flipped }">
            <div class="flip-card-front" v-if="!card.flipped">
              <img :src="require('../../img/Rubashka.jpg')" alt="Карты" />
            </div>
            <div class="flip-card-back" v-else>
              <img :src="card.src" alt="Карты" />
            </div>
          </div>
        </div>
      </div>
      <div class="answer" v-if="showAnswer">
        <p class="answer_text">ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ ГПТ</p>
      </div>
    </div>
  </div>
</template>

      
<!--       <div class="recognize">
  <p class="recognize_text">Переверни карты и узнай ответ!</p>
</div> -->


<script>
export default {
  data() {
    return {
      selectedCards: 0,
      cards: [],
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
      userQuestion: '',
      submittedQuestion: '',
      showAnswer: false,
      imgContainerHeight: '',
    }
  },
  computed: {
    allCardsFlipped() {
      return this.cards.length > 0 && this.cards.every(card => card.flipped);
    }
  },
  methods: {
    selectCards(number) {
      const defaultCardImage = { src: '', flipped: false };
      this.selectedCards = number;
      this.cards = Array.from({ length: number }, () => ({ ...defaultCardImage }));
      this.availableImages = [...this.tarotImages];
    },
    flipCard(index) {
      if (this.availableImages.length === 0 || this.cards[index].flipped) return;

      const randomIndex = Math.floor(Math.random() * this.availableImages.length);
      const randomImage = this.availableImages[randomIndex];
      
      this.availableImages.splice(randomIndex, 1);

      this.cards[index].src = randomImage;
      this.cards[index].flipped = true;
    },
    submitQuestion() {
      this.submittedQuestion = this.userQuestion;
      this.userQuestion = '';
    },
    revealAnswer() {
      if(this.allCardsFlipped) {
    this.showAnswer = true;
      } 
    },
  }
}
</script>

<style scoped>
.main_page{
  display: flex;
  flex-direction: column-reverse;
  height: 70%;
  overflow: auto;
}
.chat_text{
  font-family: Mulish Regular;
  font-size: 18px;
  line-height: 42px;
  letter-spacing: 0.01em;
  text-align: center;
  color: #FFFFFF;
  margin-bottom: 10px;
}
.choice{
  width: 70%;
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.4 );
  padding: 15px;
  margin-bottom: 20px;
  opacity: 0; /* Начальное состояние - элемент невидим */
  animation: fadeIn 1s ease forwards;
}
.choice_text{
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
p{
  margin: 0;
}
.cards_container{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  gap: 20px;
  opacity: 0; /* Начальное состояние - элемент невидим */
  animation: fadeIn 2s ease 0.3s forwards;
}
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.cards_container > * {
  animation-delay: 1s; /* Измените задержку по вашему желанию */
}
.cards{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: end;
  gap: 20px;
  width: 95%;
  height: auto;
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.3 );
}
.cards_1{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: end;
  gap: 5px;
  width: 95%;
  height: auto;
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.3 );
  padding-top: 10px;
}
.card{
  background: -webkit-linear-gradient(280deg, #6c0094,#f759ea);                                                                   
  padding: 5px;
  border-radius: 3px;                 
}
.card_number{
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.01em;
  text-align: center;
  color: #FFFFFF;
}
.number{
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.01em;
  text-align: center;
  color: #FFFFFF;
  margin-bottom: 10px;
}
.wrapper{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 7px;
  width: 80%;
}
.hello{
  width: 70%;
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.4 );
  padding: 15px;
  margin-bottom: 5px;
}
.hello1{
  opacity: 0;
  animation: fadeIn 1s ease forwards;
}
.hello2{
  opacity: 0;
  animation: fadeIn 2s ease 0.3s forwards;
}
.hello_text{
  max-width: 260px;
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.question_input {
  width: 83%;
  position: fixed;
  bottom: 30px;
  left: 5%;
  padding: 14px;
  border-radius: 8px;
  background: #191b1b url('../../img/right.svg') no-repeat right 5px center;;
  border: none;
  outline: none;
  color: #FFFFFF;
}

.question_input::placeholder {
  font-family: "Mulish Regular";
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  letter-spacing: 0em;
  color: #d2d8deab;
}

.question_input:focus {
  color: #FFFFFF;
}
.answer_button {
  position: fixed;
  bottom: 30px;
  left: 5%;
  font-family: Mulish Regular;
  font-size: 18px;
  line-height: 22px;
  letter-spacing: 0.01em;
  text-align: center;
  width: 90%;
  color: #FFFFFF;
  background: rgba( 60, 57, 65, 0.5 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 6px );
  -webkit-backdrop-filter: blur( 6px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  border: none;
  border-radius: 12px;
  display: block;
  cursor: pointer;
  padding: 10px 12px;
}
.question{
  width: 70%;
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.4 );
  padding: 15px;
  margin-bottom: 15px;
  float: right;
  opacity: 0;
  animation: fadeIn 2s ease 0.3s forwards;
}
.question_text{
  max-width: 260px;
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.img_container{
  width: 100%;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 1fr;
  gap: 5px;
  margin-bottom: 15px;
  opacity: 0;
  animation: fadeIn 3s ease 0.6s forwards;
}
.rubashka{
  width: 100%;
  border-radius: 5px;
  object-fit: cover;
}
.recognize{
  width: 70%;
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.4 );
  padding: 15px;
  margin-bottom: 5px;
}
.recognize_text{
  max-width: 260px;
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.flip-card-container {
  height: 100%;
  perspective: 1000px;
}

.flip-card {
  height: 100%;
  width: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1.5s;
}

.flip-card.flipped {
  height: 100%;
  transform: rotateY(180deg);
}

.flip-card img {
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 5px;
}

.flip-card-back {
  height: 100%;
  transform: rotateY(180deg);
}
.answer_button.purple {
  background: rgba( 180, 94, 209, 0.5 );
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 6px );
  -webkit-backdrop-filter: blur( 6px );
  border-radius: 10px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
}
.answer{
  width: 70%;
  box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
  backdrop-filter: blur( 3px );
  border-radius: 12px;
  border: 1px solid rgba( 255, 255, 255, 0.18 );
  background: rgba( 180, 94, 209, 0.4 );
  padding: 15px;
  margin-bottom: 20px;
  opacity: 0;
  animation: fadeIn 1s ease forwards;
}
.answer_text{
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 18px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.home_button{
  position: fixed;
  bottom: 30px;
  left: 20%;
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