// Restaurant related types
export interface MenuItem {
    id: string;
    name: string;
    description: string;
    price: number;
    image: string;
    category: string;
    isBestSeller: boolean;
}

export interface Restaurant {
    id: string;
    name: string;
    description: string;
    cuisine: string;
    location: string;
    address: string;
    phone: string;
    email: string;
    priceRange: 'budget' | 'moderate' | 'fine-dining' | 'expensive' | 'cheap';
    rating: number;
    reviewCount: number;
    images: string[];
    openingHours: {
        [key: string]: { open: string; close: string };
    };
    features: string[];
    capacity: number;
    menu?: MenuItem[];
    isOpen?: boolean;
}

// Reservation related types
export interface Reservation {
    id?: string;
    restaurantId: string;
    restaurantName?: string;
    date: string;
    time: string;
    guests: number;
    customerName: string;
    customerEmail: string;
    customerPhone: string;
    specialRequests?: string;
    status?: 'pending' | 'confirmed' | 'cancelled';
    createdAt?: string;
}

export interface TimeSlot {
    time: string;
    available: boolean;
    capacity: number;
}

// User related types (for future authentication)
export interface User {
    id: string;
    name: string;
    email: string;
    phone: string;
    avatar?: string;
}

// Filter types
export interface RestaurantFilters {
    cuisine?: string;
    location?: string;
    priceRange?: string[];
    rating?: number;
    searchQuery?: string;
}

// API Response types
export interface ApiResponse<T> {
    success: boolean;
    data?: T;
    message?: string;
    error?: string;
}
