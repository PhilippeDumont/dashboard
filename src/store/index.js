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
      state.listProjects.sort((a, b) => (a.name.toUpperCase() > b.name.toUpperCase()) ? 1 : -1)
    },
    DELETE_PROJECT(state, project) {
      state.listProjects.splice(state.listProjects.indexOf(project), 1)
      console.log(state.listProjects)
    },
    SET_CURRENT_PROJECT(state, currentProject) {
      state.currentProject = currentProject
    },
    SET_LIST_PROJECTS(state, list) {
      state.listProjects = list
      state.listProjects.sort((a, b) => (a.name.toUpperCase() > b.name.toUpperCase()) ? 1 : -1)
    }
  },
  actions: {
    addProject({ commit }, project) {
      commit('ADD_PROJECT', project)
    },
    deleteProject({ commit }, project) {
      commit('DELETE_PROJECT', project)
    },
    setCurrentProject({ commit }, project) {
      commit('SET_CURRENT_PROJECT', project)
    },
    setListProjects({ commit }, list) {
      commit('SET_LIST_PROJECTS', list)
    }
  },
  modules: {
  }
})
