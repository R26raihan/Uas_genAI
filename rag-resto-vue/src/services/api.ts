import axios from 'axios';
import type { Restaurant, Reservation } from '../types';

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/v1',
    headers: {
        'Content-Type': 'application/json',
    },
});

export default {
    async getRestaurants(): Promise<Restaurant[]> {
        const response = await apiClient.get<Restaurant[]>('/restaurants/');
        return response.data;
    },

    async getRestaurant(id: string): Promise<Restaurant> {
        const response = await apiClient.get<Restaurant>(`/restaurants/${id}`);
        return response.data;
    },

    async createReservation(data: Partial<Reservation>): Promise<Reservation> {
        const response = await apiClient.post<Reservation>('/reservations/', data);
        return response.data;
    },

    async getReservation(id: string): Promise<Reservation> {
        const response = await apiClient.get<Reservation>(`/reservations/${id}`);
        return response.data;
    },

    async getReservations(filters?: { restaurantId?: string; customerEmail?: string; customerPhone?: string }): Promise<Reservation[]> {
        const response = await apiClient.get<Reservation[]>('/reservations/', { params: filters });
        return response.data;
    },

    async chat(message: string): Promise<{ response: string }> {
        const response = await apiClient.post<{ response: string }>('/chat/', { message });
        return response.data;
    },
};
