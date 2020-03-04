// import * as types from '../mutation-types'
// import Vue from 'vue'

const state = {
    all: [],
    pending: false,
    error: false
}

const getters = {
    getProjects: state => state.all
}

export default {
    state,
    getters
}