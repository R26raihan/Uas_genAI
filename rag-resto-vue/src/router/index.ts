import { createRouter, createWebHistory } from 'vue-router';
import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/HomePage.vue'),
    },
    {
        path: '/restaurants',
        name: 'Restaurants',
        component: () => import('../views/RestaurantsPage.vue'),
    },
    {
        path: '/restaurant/:id',
        name: 'RestaurantDetail',
        component: () => import('../views/RestaurantDetailPage.vue'),
        props: true,
    },
    {
        path: '/reservation/:restaurantId',
        name: 'Reservation',
        component: () => import('../views/ReservationPage.vue'),
        props: true,
    },
    {
        path: '/confirmation/:bookingId',
        name: 'Confirmation',
        component: () => import('../views/ConfirmationPage.vue'),
        props: true,
    },
    {
        path: '/ai-reservation',
        name: 'AIReservation',
        component: () => import('../views/AIReservationPage.vue'),
    },
    {
        path: '/my-reservations',
        name: 'UserReservations',
        component: () => import('../views/UserReservationsPage.vue'),
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition;
        } else {
            return { top: 0 };
        }
    },
});

export default router;
