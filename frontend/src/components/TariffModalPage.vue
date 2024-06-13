<template>
    <div v-if="isVisible" class="modal-overlay" @click="closeModal">
      <div class="modal" @click.stop>
        <div class="modal-header">
          <h2>Тарифы</h2>
          <button class="close-button" @click="closeModal">&times;</button>
        </div>
        <div class="modal-body">
          <div class="tariff">
            <p class="tariff-title">Недельный:</p>
            <p class="tariff-price">100 рублей</p>
          </div>
          <div class="tariff">
            <p class="tariff-title">Месячный:</p>
            <p class="tariff-price">350 рублей</p>
          </div>
          <div class="tariff">
            <p class="tariff-title">Годовой:</p>
            <p class="tariff-price">3500 рублей</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isVisible: {
        type: Boolean,
        required: true
      }
    },
    methods: {
      closeModal() {
        this.$emit('close');
      }
    }
  }
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal {
    background: #fff;
    padding: 20px;
    border-radius: 10px;
    max-width: 80%;
    width: 400px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .close-button {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
  }
  
  .modal-body {
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-top: 20px;
  }
  
  .tariff {
    display: flex;
    gap: 20px;
  }
  
  .tariff-title {
    font-size: 18px;
    font-weight: bold;
    font-family: Mulish Regular;
  }
  
  .tariff-price {
    font-family: Mulish Regular;
    font-size: 16px;
  }
  p{
    margin: 0;
  }
  h2{
    font-family: Mulish Regular;
  }
  </style>
  