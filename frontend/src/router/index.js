import { createRouter, createWebHistory } from 'vue-router'
import MainPage from '../components/MainPage.vue'
import ChatPage from '../components/ChatPage.vue'
import MatrixPage from '../components/MatrixPage.vue'
import DayCardPage from '../components/DayCardPage.vue'
import GoroscopePage from '../components/GoroscopePage.vue'
import YesNo from '../components/YesNo.vue'
import CardPage from '../components/CardPage.vue'


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
  {
    path: '/yesno',
    name: 'YesNo',
    component: YesNo
  },
  {
    path: '/card',
    name: 'CardPage',
    component: CardPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
