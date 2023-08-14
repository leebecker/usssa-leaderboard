import { createRouter, createWebHashHistory } from 'vue-router'

var adminObfuscationSuffix = process.env.VUE_APP_LEADERBOARD_ADMIN_OBFUSCATION_SUFFIX;

const routes = [
  {
    path: '/',
    name: 'root',
    component: () => import('../views/RootView.vue')
  },
  {
    path: '/:slug',
    name: 'leaderboard',
    component: () => import('../views/LeaderBoardView.vue')
  },
  {
    path: `/admin-${adminObfuscationSuffix}`,
    name: 'admin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/AdminRootView.vue')
  },
  {
    path: `/admin-${adminObfuscationSuffix}/:slug`,
    name: 'adminEvent',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/AdminEventView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
