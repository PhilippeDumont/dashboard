import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentProject: null,
    listProjects:[],
    expansionBarVisibility: true
  },
  getters: {
    getListProjects(state, getters) {
      return (sortType, search) => {
          let sortedData = null
          switch (sortType) {
            case "alpha-asc":
              sortedData = getters.getListProjectsSortedByAlphabet
              break
            case "alpha-desc":
              sortedData = getters.getListProjectsSortedByAntiAlphabet
              break
            case "date-open":
              sortedData = getters.getListProjectsSortedByDate
              break
            default:
              sortedData = getters.getListProjectsSortedByDate
          }
          return sortedData.filter(projet => projet.name.toUpperCase().includes(search.toUpperCase()))
      }
    },
    getListProjectsSortedByAlphabet: state => state.listProjects.sort((a, b) => (a.name.toUpperCase() > b.name.toUpperCase()) ? 1 : -1),
    
    getListProjectsSortedByAntiAlphabet: state => state.listProjects.sort((a, b) => (a.name.toUpperCase() < b.name.toUpperCase()) ? 1 : -1),

    getListProjectsSortedByDate: (state) => state.listProjects.sort(function (a, b) {
      return new Date(b.last_opening_date) - new Date(a.last_opening_date);
    }),

    getExpansionBarVisibility: state => state.expansionBarVisibility
  },
  mutations: {
    /* Project */
    ADD_PROJECT(state, newProject) {
      state.listProjects.push(newProject)
      state.listProjects.sort((a, b) => (a.name.toUpperCase() > b.name.toUpperCase()) ? 1 : -1)
    },
    DELETE_PROJECT(state, project) {
      state.listProjects.splice(state.listProjects.indexOf(project), 1)
    },
    SET_CURRENT_PROJECT(state, newCurrentProject) {
      let indexProject = state.listProjects.indexOf(newCurrentProject)
      state.listProjects[indexProject].setLastopeningDate(Date.now())
      state.currentProject = state.listProjects[indexProject]
    },
    SET_LIST_PROJECTS(state, list) {
      state.listProjects = list
    },
    SET_EXPANSION_BAR_VISIBILITY(state, visibility) {
      state.expansionBarVisibility = visibility
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
    },
    setExpansionBarVisibility({ commit }, visibility) {
      commit('SET_EXPANSION_BAR_VISIBILITY', visibility)
    }
  },
  modules: {}
})
