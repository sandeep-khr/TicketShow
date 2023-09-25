import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminHome from '../views/AdminHome.vue'
import Signup from '../views/Signup.vue'
import Login from '../views/Login.vue'
import { useAuthStore } from '../stores/index';
import AddTheater from '../components/AddTheater.vue';
import AddShow from '../components/AddShow.vue';
import ShowDetails from '../views/ShowDetails.vue';
import Search from '../views/Search.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/admin',
      name: 'Admin',
      component: AdminHome,
      meta: { requiresAdmin: true }
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    
    {
      path: '/admin/theater/add',
      component: AddTheater,
      meta: { requiresAdmin: true }, 
    },
    {
      path: '/admin/show/add/:id',
      component: AddShow,
      meta: { requiresAdmin: true }, 
    },
    {
      path: '/show/:id',
      component: ShowDetails,
      name: 'ShowDetails',
      // props: true,
      meta: { requiresAuth: true }, 
    },
    {
      path: '/show/search',
      name: 'search',
      component: Search,
      meta: { requiresAuth: true }, 
    },
    {
      path: '/bookings',
      name: 'bookings',
      component: () => import('../views/Tickets.vue'),
      meta: { requiresAuth: true }, 
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('../views/NotFound.vue')
    },
    
  ]
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const isLoggedIn = authStore.isLoggedIn;
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);
  const requiresAdmin = to.matched.some((record) => record.meta.requiresAdmin);

  if (requiresAuth && !isLoggedIn) {
    // If the route requires authentication and the user is not logged in, redirect to the login page
    next('/login');
  } else if (requiresAdmin && !isLoggedIn) {
    // If the route requires being a guest (not authenticated) and the user is logged in, redirect to the home page
    next('/login');
  } else if (requiresAdmin &&  !authStore.user.is_admin) {
    // If the route requires being a guest (not authenticated) and the user is logged in, redirect to the home page
    next('/signup');
  } else {
    next(); // Allow the navigation to proceed
  }
});

export default router
