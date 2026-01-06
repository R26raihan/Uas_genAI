<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { FunnelIcon } from '@heroicons/vue/24/outline';
import RestaurantCard from '../components/restaurant/RestaurantCard.vue';
import api from '../services/api';
import type { Restaurant, RestaurantFilters } from '../types';

const restaurants = ref<Restaurant[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

const filters = ref<RestaurantFilters>({
  searchQuery: '',
  cuisine: '',
  location: '',
  priceRange: [],
  rating: undefined,
});

const showFilters = ref(false);

const cuisines = ['Semua', 'Indonesian', 'Balinese', 'Padang', 'Sundanese', 'Javanese'];
const locations = ['Semua', 'Jakarta Pusat', 'Jakarta Selatan', 'Jakarta Barat', 'Ubud, Bali', 'Kota Tua', 'Menteng', 'Kebayoran Baru', 'Surabaya'];
const priceRanges = [
  { label: '50rb - 100rb', value: 'budget' },
  { label: '100rb - 500rb', value: 'moderate' },
  { label: '500rb - 1jt+', value: 'fine-dining' },
];

onMounted(async () => {
  try {
    restaurants.value = await api.getRestaurants();
  } catch (err) {
    error.value = 'Gagal memuat data restoran. Pastikan backend berjalan.';
    console.error(err);
  } finally {
    loading.value = false;
  }
});

const filteredRestaurants = computed(() => {
  let results = [...restaurants.value];

  if (filters.value.searchQuery) {
    const query = filters.value.searchQuery.toLowerCase();
    results = results.filter(r =>
      r.name.toLowerCase().includes(query) ||
      r.description.toLowerCase().includes(query) ||
      r.cuisine.toLowerCase().includes(query)
    );
  }

  if (filters.value.cuisine && filters.value.cuisine !== 'Semua') {
    results = results.filter(r => r.cuisine === filters.value.cuisine);
  }

  if (filters.value.location && filters.value.location !== 'Semua') {
    results = results.filter(r => r.location === filters.value.location);
  }

  if (filters.value.priceRange && filters.value.priceRange.length > 0) {
    results = results.filter(r => filters.value.priceRange!.includes(r.priceRange));
  }

  if (filters.value.rating) {
    results = results.filter(r => r.rating >= filters.value.rating!);
  }

  return results;
});

const clearFilters = () => {
  filters.value = {
    searchQuery: '',
    cuisine: '',
    location: '',
    priceRange: [],
    rating: undefined,
  };
};
</script>

<template>
  <div class="min-h-screen bg-dark-50">
    <!-- Header -->
    <div class="bg-white border-b border-dark-100">
      <div class="container-custom py-8">
        <h1 class="text-4xl font-display font-bold text-dark-900 mb-4">
          Jelajahi Restoran
        </h1>
        <p class="text-lg text-dark-600">
          Temukan pengalaman bersantap sempurna Anda from {{ loading ? '...' : restaurants.length }} restoran luar biasa
        </p>
        <div v-if="error" class="mt-4 p-4 bg-red-100 text-red-700 rounded-lg">
            {{ error }}
        </div>
      </div>
    </div>

    <div class="container-custom py-8">
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Filters Sidebar -->
        <aside class="lg:w-80 flex-shrink-0">
          <div class="sticky top-20">
            <!-- Mobile Filter Toggle -->
            <button
              @click="showFilters = !showFilters"
              class="lg:hidden w-full btn-outline mb-4"
            >
              <FunnelIcon class="w-5 h-5" />
              {{ showFilters ? 'Sembunyikan Filter' : 'Tampilkan Filter' }}
            </button>

            <!-- Filters -->
            <div
              :class="{ 'hidden lg:block': !showFilters }"
              class="card space-y-6"
            >
              <div class="flex items-center justify-between">
                <h2 class="text-xl font-display font-bold text-dark-900">Filter</h2>
                <button
                  @click="clearFilters"
                  class="text-sm text-primary-600 hover:text-primary-700 font-medium"
                >
                  Hapus Semua
                </button>
              </div>

              <!-- Search -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Cari
                </label>
                <input
                  v-model="filters.searchQuery"
                  type="text"
                  placeholder="Restaurant name or cuisine..."
                  class="input"
                />
              </div>

              <!-- Cuisine -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Cuisine Type
                </label>
                <select v-model="filters.cuisine" class="input">
                  <option v-for="cuisine in cuisines" :key="cuisine" :value="cuisine === 'All' ? '' : cuisine">
                    {{ cuisine }}
                  </option>
                </select>
              </div>

              <!-- Location -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Lokasi
                </label>
                <select v-model="filters.location" class="input">
                  <option v-for="location in locations" :key="location" :value="location === 'Semua' ? '' : location">
                    {{ location }}
                  </option>
                </select>
              </div>

              <!-- Price Range -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-3">
                  Rentang Harga
                </label>
                <div class="space-y-2">
                  <label
                    v-for="range in priceRanges"
                    :key="range.value"
                    class="flex items-center gap-2 cursor-pointer"
                  >
                    <input
                      type="checkbox"
                      :value="range.value"
                      v-model="filters.priceRange"
                      class="w-4 h-4 text-primary-600 rounded focus:ring-primary-500"
                    />
                    <span class="text-sm text-dark-700">{{ range.label }}</span>
                  </label>
                </div>
              </div>

              <!-- Rating -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Rating Minimal
                </label>
                <select v-model.number="filters.rating" class="input">
                  <option :value="undefined">Semua Rating</option>
                  <option :value="4.5">4.5+ Bintang</option>
                  <option :value="4.0">4.0+ Bintang</option>
                  <option :value="3.5">3.5+ Bintang</option>
                </select>
              </div>
            </div>
          </div>
        </aside>

        <!-- Results -->
        <main class="flex-1">
          <div class="mb-6">
            <p class="text-dark-600">
              Menampilkan <span class="font-semibold text-dark-900">{{ filteredRestaurants.length }}</span> restoran
            </p>
          </div>

          <!-- Restaurant Grid -->
          <div v-if="filteredRestaurants.length > 0" class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
            <RestaurantCard
              v-for="restaurant in filteredRestaurants"
              :key="restaurant.id"
              :restaurant="restaurant"
            />
          </div>

          <!-- Empty State -->
          <div v-else class="text-center py-20">
            <div class="text-6xl mb-4">🔍</div>
            <h3 class="text-2xl font-display font-bold text-dark-900 mb-2">
              Restoran tidak ditemukan
            </h3>
            <p class="text-dark-600 mb-6">
              Coba sesuaikan filter atau kata kunci pencarian Anda
            </p>
            <button @click="clearFilters" class="btn-primary">
              Hapus Filter
            </button>
          </div>
        </main>
      </div>
    </div>
  </div>
</template>
