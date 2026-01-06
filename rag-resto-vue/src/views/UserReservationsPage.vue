<script setup lang="ts">
import { ref } from 'vue';
import { MagnifyingGlassIcon, CalendarIcon, UserGroupIcon, ClockIcon } from '@heroicons/vue/24/outline';
import api from '../services/api';
import type { Reservation } from '../types';

const searchForm = ref({
  customerEmail: '',
  customerPhone: '',
});

const reservations = ref<Reservation[]>([]);
const loading = ref(false);
const hasSearched = ref(false);
const error = ref<string | null>(null);

const searchReservations = async () => {
  if (!searchForm.value.customerEmail || !searchForm.value.customerPhone) {
    error.value = 'Mohon isi email dan nomor telepon.';
    return;
  }

  loading.value = true;
  error.value = null;
  reservations.value = [];
  hasSearched.value = false;

  try {
    const data = await api.getReservations({
      customerEmail: searchForm.value.customerEmail,
      customerPhone: searchForm.value.customerPhone,
    });
    reservations.value = data;
    hasSearched.value = true;
  } catch (err) {
    console.error(err);
    error.value = 'Gagal mencari reservasi. Silakan coba lagi.';
  } finally {
    loading.value = false;
  }
};

const formatDate = (date: string) => {
  return new Date(date).toLocaleDateString('id-ID', {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  });
};
</script>

<template>
  <div class="min-h-screen bg-dark-50 py-12">
    <div class="container-custom max-w-4xl">
      <div class="text-center mb-10">
        <h1 class="text-4xl font-display font-bold text-dark-900 mb-4">Cek Pesanan Anda</h1>
        <p class="text-lg text-dark-600">
          Lihat riwayat dan status reservasi Anda dengan memasukkan email dan nomor telepon.
        </p>
      </div>

      <!-- Search Form -->
      <div class="card mb-10 max-w-2xl mx-auto">
        <form @submit.prevent="searchReservations" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-dark-700 mb-2">Email</label>
              <input
                v-model="searchForm.customerEmail"
                type="email"
                placeholder="nama@email.com"
                class="input"
                required
              />
            </div>
            <div>
              <label class="block text-sm font-semibold text-dark-700 mb-2">Nomor Telepon</label>
              <input
                v-model="searchForm.customerPhone"
                type="tel"
                placeholder="08123456789"
                class="input"
                required
              />
            </div>
          </div>
          <button type="submit" class="btn-primary w-full" :disabled="loading">
            <span v-if="loading" class="flex items-center justify-center gap-2">
              <span class="w-4 h-4 border-2 border-primary-50 border-t-transparent rounded-full animate-spin"></span>
              Mencari...
            </span>
            <span v-else class="flex items-center justify-center gap-2">
              <MagnifyingGlassIcon class="w-5 h-5" />
              Cari Reservasi
            </span>
          </button>
          <p v-if="error" class="text-red-600 text-sm text-center">{{ error }}</p>
        </form>
      </div>

      <!-- Results -->
      <div v-if="hasSearched" class="space-y-6 animate-fade-in-up">
        <div v-if="reservations.length === 0" class="text-center py-12 bg-white rounded-xl shadow-sm border border-dark-100">
          <div class="text-4xl mb-4">📭</div>
          <h3 class="text-xl font-bold text-dark-900 mb-2">Tidak Ada Reservasi Ditemukan</h3>
          <p class="text-dark-600">Kami tidak menemukan reservasi dengan data tersebut.</p>
        </div>

        <div v-else class="grid gap-6">
          <h2 class="text-2xl font-bold text-dark-900 mb-4">Daftar Reservasi Anda ({{ reservations.length }})</h2>
          
          <div v-for="res in reservations" :key="res.id" class="card hover:shadow-lg transition-shadow border-l-4" 
               :class="res.status === 'confirmed' ? 'border-l-green-500' : 'border-l-yellow-500'">
             <router-link :to="`/confirmation/${res.id}`" class="block">
              <div class="flex flex-col md:flex-row justify-between md:items-center gap-4">
                <div>
                  <div class="flex items-center gap-2 text-sm text-dark-500 mb-1">
                    <span class="px-2 py-0.5 rounded text-xs font-semibold uppercase tracking-wider"
                      :class="res.status === 'confirmed' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'">
                      {{ res.status }}
                    </span>
                    <span>#{{ res.id }}</span>
                  </div>
                  <h3 class="text-xl font-bold text-dark-900 mb-1">{{ res.restaurantName }}</h3>
                  <div class="flex flex-wrap gap-4 text-sm text-dark-600">
                    <span class="flex items-center gap-1">
                      <CalendarIcon class="w-4 h-4" />
                      {{ formatDate(res.date) }}
                    </span>
                    <span class="flex items-center gap-1">
                      <ClockIcon class="w-4 h-4" />
                      {{ res.time }}
                    </span>
                    <span class="flex items-center gap-1">
                      <UserGroupIcon class="w-4 h-4" />
                      {{ res.guests }} Orang
                    </span>
                  </div>
                </div>
                
                <div class="flex gap-3">
                   <!-- Actions could go here -->
                </div>
              </div>
             </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
