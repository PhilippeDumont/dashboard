const state = {
    expansionBarVisibility: true,

    msgSnackBar: "",
    snackBarToShow: false,
    colorSnackBar: ""
}

const getters = {
    getExpansionBarVisibility: state => state.expansionBarVisibility,

    getMsgSnackBar: state => state.msgSnackBar,
    getSnackBarToShow: state => state.snackBarToShow,
    getColorSnackBar: state => state.colorSnackBar
}

const actions = {
    setExpansionBarVisibility({ commit }, visibility) {
        commit('SET_EXPANSION_BAR_VISIBILITY', visibility)
    },
    setMsgSnackBar({ commit }, msgSnackBar) {
        commit('SET_MSG_SNACKBAR', msgSnackBar)
    },
    setSnackBarToShow({ commit }, snackBarToShow) {
        commit('SET_SNAKBAR_TO_SHOW', snackBarToShow)
    },
    setColorSnackBar({ commit }, colorSnackBar) {
        commit('SET_COLOR_SNACKBAR', colorSnackBar)
    }
}

const mutations = {
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
}

export default {
    state,
    getters,
    actions,
    mutations
}