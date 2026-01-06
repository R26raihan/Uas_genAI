<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { RouterLink } from 'vue-router';
import { CheckCircleIcon, CalendarIcon, EnvelopeIcon } from '@heroicons/vue/24/solid';
import api from '../services/api';
import type { Reservation } from '../types';

interface Props {
  bookingId: string;
}

const props = defineProps<Props>();
const bookingDetails = ref<Reservation | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
    try {
        bookingDetails.value = await api.getReservation(props.bookingId);
    } catch (err) {
        console.error(err);
        error.value = "Gagal memuat detail reservasi.";
    } finally {
        loading.value = false;
    }
});

const formattedDate = computed(() => {
    if (!bookingDetails.value) return '';
    return new Date(bookingDetails.value.date).toLocaleDateString('id-ID', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });
});
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-50 via-white to-accent-50 py-12">
    <div class="container-custom max-w-3xl">
      <!-- Loading -->
      <div v-if="loading" class="text-center py-20">
          <div class="text-xl text-dark-600 animate-pulse">Memuat detail reservasi...</div>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="text-center py-20 text-red-600">
          <p>{{ error }}</p>
          <RouterLink to="/" class="btn-primary mt-4 inline-block">Kembali ke Beranda</RouterLink>
      </div>

      <div v-else-if="bookingDetails" class="card text-center space-y-8 animate-scale-in">
        <!-- Success Icon -->
        <div class="inline-flex items-center justify-center w-24 h-24 rounded-full bg-secondary-100">
          <CheckCircleIcon class="w-16 h-16 text-secondary-600" />
        </div>

        <!-- Heading -->
        <div>
          <h1 class="text-4xl font-display font-bold text-dark-900 mb-3">
            Reservasi Berhasil!
          </h1>
          <p class="text-lg text-dark-600">
            Meja Anda telah berhasil dipesan
          </p>
        </div>

        <!-- Booking Details -->
        <div class="bg-dark-50 rounded-xl p-8 text-left space-y-6">
          <div class="flex items-center justify-between pb-4 border-b border-dark-200">
            <span class="text-sm text-dark-600">ID Reservasi</span>
            <span class="font-mono font-semibold text-dark-900">{{ bookingDetails.id }}</span>
          </div>

          <div class="space-y-4">
            <div class="flex items-start gap-4">
              <div class="w-12 h-12 rounded-lg gradient-primary flex items-center justify-center flex-shrink-0">
                <span class="text-2xl">🍽️</span>
              </div>
              <div>
                <p class="text-sm text-dark-600">Restoran</p>
                <p class="text-xl font-display font-bold text-dark-900">{{ bookingDetails.restaurantName }}</p>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="flex items-start gap-3">
                <CalendarIcon class="w-5 h-5 text-primary-600 flex-shrink-0 mt-0.5" />
                <div>
                  <p class="text-sm text-dark-600">Tanggal & Waktu</p>
                  <p class="font-semibold text-dark-900">{{ formattedDate }}</p>
                  <p class="font-semibold text-dark-900">{{ bookingDetails.time }}</p>
                </div>
              </div>

              <div class="flex items-start gap-3">
                <svg class="w-5 h-5 text-primary-600 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
                <div>
                  <p class="text-sm text-dark-600">Jumlah Tamu</p>
                  <p class="font-semibold text-dark-900">{{ bookingDetails.guests }} Tamu</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Confirmation Email Notice -->
        <div class="bg-primary-50 rounded-xl p-6 flex items-start gap-4">
          <EnvelopeIcon class="w-6 h-6 text-primary-600 flex-shrink-0 mt-0.5" />
          <div class="text-left">
            <p class="font-semibold text-primary-900 mb-1">Email Konfirmasi Terkirim</p>
            <p class="text-sm text-primary-800">
              Kami telah mengirimkan email konfirmasi ke <strong>{{ bookingDetails.customerEmail }}</strong> dengan rincian reservasi Anda.
            </p>
          </div>
        </div>

        <!-- Important Notes -->
        <div class="bg-yellow-50 border border-yellow-200 rounded-xl p-6 text-left">
          <h3 class="font-display font-bold text-yellow-900 mb-3">Catatan Penting</h3>
          <ul class="space-y-2 text-sm text-yellow-800">
            <li class="flex items-start gap-2">
              <span class="text-yellow-600 mt-0.5">•</span>
              <span>Harap tiba 10 menit sebelum waktu reservasi Anda</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-yellow-600 mt-0.5">•</span>
              <span>Jika Anda perlu membatalkan atau mengubah reservasi, silakan hubungi restoran setidaknya 24 jam sebelumnya</span>
            </li>
            <li class="flex items-start gap-2">
              <span class="text-yellow-600 mt-0.5">•</span>
              <span>Bawa identitas diri yang valid dan konfirmasi booking Anda</span>
            </li>
          </ul>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 pt-4">
          <RouterLink to="/restaurants" class="btn-primary flex-1">
            Lihat Restoran Lainnya
          </RouterLink>
          <RouterLink to="/" class="btn-outline flex-1">
            Kembali ke Beranda
          </RouterLink>
        </div>

        <!-- Add to Calendar (Future Enhancement) -->
        <div class="pt-4 border-t border-dark-200">
          <button class="text-primary-600 hover:text-primary-700 font-medium text-sm flex items-center gap-2 mx-auto">
            <CalendarIcon class="w-4 h-4" />
            Tambah ke Kalender
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
