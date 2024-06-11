<template>
  <div class="main_page">
    <p class="header">Гороскоп Овна на сегодня</p>
    <div class="subheader_container">
      <p class="subheader">21 МАРТА - 20 АПРЕЛЯ</p>
    </div>
    <div class="main">
      <p class="main_text">Сегодня Овнам просто необходимо наслаждаться жизнью – сейчас она дарит вам самые лучшие моменты. Прочувствуйте их. Отлично в этот день заниматься творчеством – это расслабит и поможет поверить в себя, что здорово отразится и на работе. Гороскоп на сегодня для знака Овна советует «забить» на рутину – находите альтернативные варианты, новые решения.</p>
    </div>
    <button class="home_button" @click="this.$router.push('/')">Домой</button>
  </div>
</template>

<script>
export default {

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