import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Home',
    name: 'Home',
    component: Home
  },
  {
    path: '/Level1',
    name: 'Level1',
    component: () => import('../views/Level1.vue')
  },
  {
    path: '/Level2',
    name: 'Level2',
    component: () => import('../views/Level2.vue')
  },
  {
    path: '/Level3',
    name: 'Level1',
    component: () => import('../views/Level3.vue')
  },
  {
    path: '/Level4',
    name: 'Level4',
    component: () => import('../views/Level4.vue')
  },
  {
    path: '/Edit',
    name: 'Edit',
    component: () => import('../views/Edit.vue')
  },
  {
    path: '/Settings',
    name: 'Settings',
    component: () => import('../views/Settings.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
