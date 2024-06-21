<template>
  <div class="main_page">
    <p class="header">{{ name }}</p>
    <div class="main_container">
      <img :src="cardimage" alt="" class="">
      <img :src="cardimage" alt="" class="reverse">
    </div>
    <div class="significance">
      <div class="significance_container" @click="toggleContent('direct')">
        <div class="header_container">
          <p class="significance_header">Прямое значение</p>
          <img :class="{'rotated': visibleContent === 'direct'}" src="../../img/down.svg" alt="">
        </div>
        <div v-if="visibleContent === 'direct'" class="significance_content">
          <p class="subheader">{{this.info.Direct}}</p>
        </div>
      </div>
      <div class="significance_container" @click="toggleContent('reversed')">
        <div class="header_container">
          <p class="significance_header">Перевернутое значение</p>
          <img :class="{'rotated': visibleContent === 'reversed'}" src="../../img/down.svg" alt="">
        </div>
        <div v-if="visibleContent === 'reversed'" class="significance_content">
          <p class="subheader">{{this.info.Reversed}}</p>
        </div>
      </div>
      <div class="significance_container" @click="toggleContent('waite')">
        <div class="header_container">
          <p class="significance_header">Оригинальный текст Вейта</p>
          <img :class="{'rotated': visibleContent === 'waite'}" src="../../img/down.svg" alt="">
        </div>
        <div v-if="visibleContent === 'waite'" class="significance_content">
          <p class="subheader">{{this.info.Waite}}</p>
        </div>
      </div>
      <div class="significance_container" @click="toggleContent('metaphysical')">
        <div class="header_container">
          <p class="significance_header">Метафизическая интерпретация</p>
          <img :class="{'rotated': visibleContent === 'metaphysical'}" src="../../img/down.svg" alt="">
        </div>
        <div v-if="visibleContent === 'metaphysical'" class="significance_content">
          <p class="subheader">{{this.info.Metaphysical}}</p>
        </div>
      </div>
      <div class="significance_container" @click="toggleContent('imagery')">
        <div class="header_container">
          <p class="significance_header">Образный лад</p>
          <img :class="{'rotated': visibleContent === 'imagery'}" src="../../img/down.svg" alt="">
        </div>
        <div v-if="visibleContent === 'imagery'" class="significance_content">
          <p class="subheader">{{this.info.Imagery}}</p>
        </div>
      </div>
      <div class="significance_container" @click="toggleContent('symbolism')">
        <div class="header_container">
          <p class="significance_header">Символизм</p>
          <img :class="{'rotated': visibleContent === 'symbolism'}" src="../../img/down.svg" alt="">
        </div>
        <div v-if="visibleContent === 'symbolism'" class="significance_content">
          <p class="subheader">{{this.info.Symbolism}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      visibleContent: null,
      name: '',
      info: {},
    };
  },
  computed: {
    cardid() {
      return this.$route.params.number;
    },
    cardimage() {
      return require(`../../img/taro/${this.cardid}.jpg`);
    }
  },
  methods: {
    toggleContent(content) {
      if (this.visibleContent === content) {
        this.visibleContent = null;
      } else {
        this.visibleContent = content;
      }
    },
    async get_mention() {
      try {
        const response = await this.$axios.get('/cards_info/', {
          params: {
            card: this.cardid
          },
          withCredentials: true,
        });
        console.log(response);
        this.name = response.data.name
        this.info = response.data.info
      } catch (error) {
        this.error = error;
        console.error('Error fetching data:', error);
      }
    }
  },
  mounted() {
    this.get_mention();
  }
};
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
.subheader {
  font-family: Mulish Regular;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #d3d3d3;
}
.main_container img {
  width: 100%;
  border-radius: 5px;
}
.main_container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 1fr;
  gap: 20px;
}
.reverse {
  rotate: 180deg;
}
.significance {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 7px;
}
.header_container {
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
.significance_container {
  padding: 10px;
  background: rgba(164, 164, 164, 0.2);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}
.significance_content {
  padding-top: 10px;
  font-family: Mulish Regular;
  font-size: 14px;
  color: #FFFFFF;
}
img {
  transition: transform 0.3s ease;
}
img.rotated {
  transform: rotate(180deg);
}
</style>
