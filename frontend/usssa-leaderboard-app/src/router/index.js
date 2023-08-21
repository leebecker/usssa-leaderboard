import { createRouter, createWebHashHistory } from 'vue-router'
import { useAuthStore } from '@/stores';

var adminObfuscationSuffix = process.env.VUE_APP_LEADERBOARD_ADMIN_OBFUSCATION_SUFFIX;

const routes = [
  {
    path: '/',
    name: 'root',
    component: () => import('@/views/RootView.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginView.vue')
  },
  {
    path: '/:slug',
    name: 'leaderboard',
    component: () => import('@/views/LeaderBoardView.vue')
  },
  {
    path: `/admin-${adminObfuscationSuffix}`,
    name: 'admin',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('@/views/AdminRootView.vue')
  },
  {
    path: `/admin-${adminObfuscationSuffix}/:slug`,
    name: 'adminEvent',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('@/views/AdminEventView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

router.beforeEach(async (to) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const authRequired = to.path.startsWith("/admin")
  const auth = useAuthStore();

  if (authRequired && !auth.user) {
      auth.returnUrl = to.fullPath;
      return '/login';
  }
});

export default router
