import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    idCurrentProject: null
  },
  mutations: {
    SET_ID_CURRENT_PROJECT(state, id) {
      state.idCurrentProject = id
    }
  },
  actions: {
  },
  modules: {
  }
})
