import Vue from 'vue'
import Vuex from 'vuex'

import project from './modules/project'
import component from './modules/component'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
      component,
      project
    }
})
