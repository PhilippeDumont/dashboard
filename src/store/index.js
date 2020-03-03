import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        currentProject: null,
        listProjects: [],
        expansionBarVisibility: true,
        msgSnackBar: "",
        snackBarToShow: false,
        colorSnackBar: ""
    },
    getters: {
        getListProjects: state => state.listProjects.sort(function(a, b) {
            return new Date(b.last_opening_date) - new Date(a.last_opening_date);
        }),
        getExpansionBarVisibility: state => state.expansionBarVisibility,
        getMsgSnackBar: state => state.msgSnackBar,
        getSnackBarToShow: state => state.snackBarToShow,
        getColorSnackBar: state => state.colorSnackBar
    },
    mutations: {
        /* Project */
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
        },
        SET_EXPANSION_BAR_VISIBILITY(state, visibility) {
            state.expansionBarVisibility = visibility
        },
        SET_MSG_SNACKBAR(state, msgSnackBar) {
            state.msgSnackBar = msgSnackBar
        },
        SET_COLOR_SNACKBAR(state, colorSnackBar) {
            state.colorSnackBar = colorSnackBar
        },
        SET_SNAKBAR_TO_SHOW(state, snackBarToShow) {
            state.snackBarToShow = snackBarToShow
        }

    },
    actions: {
        addProject({
            commit
        }, project) {
            commit('ADD_PROJECT', project)
        },
        deleteProject({
            commit
        }, project) {
            commit('DELETE_PROJECT', project)
        },
        setCurrentProject({
            commit
        }, project) {
            commit('SET_CURRENT_PROJECT', project)
        },
        setListProjects({
            commit
        }, list) {
            commit('SET_LIST_PROJECTS', list)
        },
        setExpansionBarVisibility({
            commit
        }, visibility) {
            commit('SET_EXPANSION_BAR_VISIBILITY', visibility)
        },
        setMsgSnackBar({
            commit
        }, msgSnackBar) {
            commit('SET_MSG_SNACKBAR', msgSnackBar)
        },
        setSnackBarToShow({
            commit
        }, snackBarToShow) {
            commit('SET_SNAKBAR_TO_SHOW', snackBarToShow)
        },
        setColorSnackBar({
            commit
        }, colorSnackBar) {
            commit('SET_COLOR_SNACKBAR', colorSnackBar)
        }
    },
    modules: {}
})