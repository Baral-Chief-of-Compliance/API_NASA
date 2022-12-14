import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PhotoDayView from '../views/PhotoDayView.vue'
import FindPhotoView from '../views/FindPhotoView.vue'
import ArchiveView from '../views/ArchiveView.vue'
import PhotoView from '../views/PhotoView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'photo_of_the_day',
      component: PhotoDayView
    },
    {
      path: '/find_a_photo',
      name: 'find_a_photo',
      component: FindPhotoView
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      // component: () => import('../views/AboutView.vue')
    },
    {
      path: '/archive',
      name: 'archive',
      component: ArchiveView
    },

    {
      path:'/photo/:year-:month-:day',
      name: 'photo',
      component: PhotoView
    }
  ]
})

export default router
