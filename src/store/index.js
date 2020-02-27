import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentProject: null,
    listProjects: []
  },
  getters: {
    getListProjects: state => state.listProjects
  },
  mutations: {
    ADD_PROJECT(state, newProject) {
      state.listProjects.push(newProject)
    },
    SET_CURRENT_PROJECT(state, currentProject) {
      state.currentProject = currentProject
    },
    SET_LIST_PROJECTS(state, list) {
      state.listProjects = list
    }
  },
  actions: {
    addProject({ commit }, project) {
      commit('ADD_PROJECT', project)
    }
  },
  modules: {
  }
})
