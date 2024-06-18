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
      <div v-if="selectedNav === 0">
        
      </div>
      <div v-if="selectedNav === 1">Контент для второй вкладки</div>
      <div v-if="selectedNav === 2">Контент для третьей вкладки</div>
      <div v-if="selectedNav === 3">Контент для четвертой вкладки</div>
      <div v-if="selectedNav === 4">Контент для пятой вкладки</div>
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
    }
  }
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
.header_nav_container {
  display: flex;
  gap: 15px;
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
  border-radius: 18px;
  text-align: center;
}
.header_nav img {
  width: 45px;
  height: 45px;
}
</style>
