import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Login from '@/views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/client',
      name: 'client',
      component: () => import('../views/Clients/ClientsFilter.vue')
    },
    {
      path: '/client/choice',
      name: 'clientchoice',
      component: () => import('../views/Clients/ClientChoice.vue')
    },
    {
      path: '/client/data',
      name: 'clientdata',
      component: () => import('../views/Clients/ClientData.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
  ],
})

export default router
