const state = {
    all: [],
    current: null,
    pending: false,
    error: false
}

const getters = {

    getProjectPending: state => state.pending,
    getProjectsError: state => state.error,

    getCurrentProject: state => state.current,

    getAllProjects(state, getters) {
        return (sortType = null, search = "") => {
            let sortedData = null
            switch (sortType) {
                case "alpha-asc":
                    sortedData = getters.getAllProjectsSortedByAlphabet
                    break
                case "alpha-desc":
                    sortedData = getters.getAllProjectsSortedByAntiAlphabet
                    break
                case "date-open":
                    sortedData = getters.getAllProjectsSortedByDate
                    break
                default:
                    sortedData = state.listProjects
            }
            return sortedData.filter(projet => projet.name.toUpperCase().includes(search.toUpperCase()))
        }
    },

    getAllProjectsSortedByAlphabet: state => state.all.sort((a, b) => (a.name.toUpperCase() > b.name.toUpperCase()) ? 1 : -1),

    getAllProjectsSortedByAntiAlphabet: state => state.all.sort((a, b) => (a.name.toUpperCase() < b.name.toUpperCase()) ? 1 : -1),

    getAllProjectsSortedByDate: (state) => state.all.sort(function(a, b) {
        return new Date(b.last_opening_date) - new Date(a.last_opening_date);
    }),
}

const actions = {
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
    setNameProject({ commit }, value) {
        commit('SET_NAME_PROJECT', value)
    }
}

const mutations = {

    ADD_PROJECT(state, newProject) {
        state.all.push(newProject)
        state.all.sort((a, b) => (a.name.toUpperCase() > b.name.toUpperCase()) ? 1 : -1)
    },
    DELETE_PROJECT(state, project) {
        if (project == state.current) {
            state.current = null
        }
        state.all.splice(state.all.indexOf(project), 1)
    },
    SET_CURRENT_PROJECT(state, newCurrentProject) {
        let indexProject = state.all.indexOf(newCurrentProject)
        state.all[indexProject].setLastopeningDate(Date.now())
        state.current = state.all[indexProject]
    },
    SET_LIST_PROJECTS(state, list) {
        state.all = list
    },
    SET_NAME_PROJECT(state, value) {
        let indexProject = state.all.indexOf(value.project)
        state.all[indexProject].setName(value.nameToRename)
    }

}

export default {
    state,
    getters,
    actions,
    mutations
}