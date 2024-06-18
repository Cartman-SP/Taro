<template>
    <div v-if="isVisible" class="modal-overlay" @click="closeModal">
      <div class="modal" @click.stop>
        <div class="modal-header">
          <button class="close-button" @click="closeModal">&times;</button>
        </div>
        <div class="modal-body">
          <div class="tariff">
<!--             <p class="tariff-title">Недельный:</p>
            <p class="tariff-price">100 рублей</p> -->
            <button class="tariff_btn">Недельный 350р</button>
          </div>
          <div class="tariff">
            <button class="tariff_btn">Месячный 350р</button>
          </div>
          <div class="tariff">
            <button class="tariff_btn">Годовой 350р</button>
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
  .tariff_btn {
    color: #FFFFFF;
    background: rgba(180, 94, 209, 0.65);
    border: none;
    cursor: pointer;
    display: flex;
    height: 36px;
    padding: 10px 14px;
    justify-content: center;
    align-items: center;
    gap: 5px;
    border-radius: 10px;
    transition: all .2s ease;
    font-family: Mulish Semibold;
    width: 100%;
  }

  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal {
    background: rgba( 117, 117, 117, 0.5 );
    box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
    backdrop-filter: blur( 9.5px );
    -webkit-backdrop-filter: blur( 9.5px );
    border-radius: 10px;
    border: 1px solid rgba( 255, 255, 255, 0.18 );
    padding: 20px;
    border-radius: 10px;
    max-width: 80%;
    width: 400px;
  }
  
  .modal-header {
    display: flex;
    justify-content: end;
    align-items: center;
  }
  
  .close-button {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: #FFFFFF;
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
  </style>
  