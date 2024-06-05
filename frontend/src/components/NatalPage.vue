<template>
  <div class="main_page">
    <p class="head_text">Введите дату рождения</p>
    <div class="main_head">
      <SelectPage
      :options="['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']"
      @input="option => selectedTimeZone = option"
      :placeholderdata="'Число'"
      />
      <SelectPage
      :options="['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']"
      @input="option => selectedTimeZone = option"
      :placeholderdata="'Месяц'"
      />
      <SelectPage
      :options="['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024']"
      @input="option => selectedTimeZone = option"
      :placeholderdata="'Год'"
      />  
    </div>
    <button class="calculation">Рассчитать</button>
  </div>
</template>

<script>
import SelectPage from './SelectPage.vue';
export default {
  components: { SelectPage },
  data() {
      return {
          
      }
  },

}
</script>

<style scoped>
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
  padding: 6px 10px;
}
.balance {
  font-family: Poppins;
  font-size: 20px;
  font-weight: 700;
  line-height: 42px;
  letter-spacing: 0.01em;
  text-align: left;
  color: #FFFFFF;
}
.ref {
  display: flex;
  justify-content: end;
  align-items: center;
}
.ref_balance {
  font-family: Poppins;
  font-size: 24px;
  font-weight: 700;
  line-height: 36px;
  text-align: left;
  color: #FFFFFF;
}
.main_page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.main_head{
  display: flex;
  gap: 20px;
}
.head_text{
  font-family: Poppins;
  font-size: 28px;
  font-weight: 700;
  line-height: 42px;
  letter-spacing: 0.01em;
  text-align: center;
  color: #FFFFFF;
}
p{
  margin: 0;
}
button {
  color: #FFFFFF;
  background:#6266EA;
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
  font-family: "TT Norms Medium";
}
.matrix_img{
  border-radius: 10px;
}
</style>