import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../components/MainPage.vue'
import ChatPage from '../components/ChatPage.vue'
import MatrixPage from '../components/MatrixPage.vue'
import DayCardPage from '../components/DayCardPage.vue'
import GoroscopePage from '../components/GoroscopePage.vue'

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/matrix',
    name: 'MatrixPage',
    component: MatrixPage
  },
  {
    path: '/day',
    name: 'DayCardPage',
    component: DayCardPage
  },
  {
    path: '/goroscope/:sign',
    name: 'GoroscopePage',
    component: GoroscopePage
  },
  {
    path: '/chat',
    name: 'ChatPage',
    component: ChatPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
