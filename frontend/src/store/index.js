import { createStore } from 'vuex'

export default createStore({
  state: {
    data:{}
  },
  getters: {
  },
  mutations: {
    ADD_TO_DATA: (state, items) => {
      state.data = items
    },
  },
  actions: {
  },
  modules: {
  }
})
