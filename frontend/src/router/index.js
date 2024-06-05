import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../components/MainPage.vue'
import ChatPage from '../components/ChatPage.vue'
import MatrixPage from '../components/MatrixPage.vue'
import NatalPage from '../components/NatalPage.vue'
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
    path: '/natal',
    name: 'NatalPage',
    component: NatalPage
  },
  {
    path: '/goroscope',
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