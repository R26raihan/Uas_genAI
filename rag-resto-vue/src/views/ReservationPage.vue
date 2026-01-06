<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { CalendarIcon, ClockIcon, UserGroupIcon } from '@heroicons/vue/24/outline';
import { generateTimeSlots } from '../data/mockData';
import api from '../services/api';
import type { Reservation, Restaurant } from '../types';

interface Props {
  restaurantId: string;
}

const props = defineProps<Props>();
const router = useRouter();

const restaurant = ref<Restaurant | undefined>(undefined);
const loading = ref(true);
const error = ref<string | null>(null);
const totalBookings = ref(0);

onMounted(async () => {
  try {
    const [restaurantData, reservations] = await Promise.all([
      api.getRestaurant(props.restaurantId),
      api.getReservations({ restaurantId: props.restaurantId })
    ]);
    restaurant.value = restaurantData;
    totalBookings.value = reservations.length;
  } catch (err) {
    error.value = 'Gagal memuat data restoran';
    console.error(err);
  } finally {
    loading.value = false;
  }
});

const formData = ref<Partial<Reservation>>({
  restaurantId: props.restaurantId,
  date: '',
  time: '',
  guests: 2,
  customerName: '',
  customerEmail: '',
  customerPhone: '',
  specialRequests: '',
});

const errors = ref<Record<string, string>>({});
const isSubmitting = ref(false);

const availableTimeSlots = computed(() => {
  if (!formData.value.date) return [];
  return generateTimeSlots(formData.value.date);
});

const minDate = computed(() => {
  const today = new Date();
  return today.toISOString().split('T')[0];
});

const maxDate = computed(() => {
  const maxDate = new Date();
  maxDate.setMonth(maxDate.getMonth() + 2);
  return maxDate.toISOString().split('T')[0];
});

const validateForm = (): boolean => {
  errors.value = {};

  if (!formData.value.date) {
    errors.value.date = 'Please select a date';
  }

  if (!formData.value.time) {
    errors.value.time = 'Please select a time';
  }

  if (!formData.value.guests || formData.value.guests < 1) {
    errors.value.guests = 'Please select number of guests';
  }

  if (!formData.value.customerName?.trim()) {
    errors.value.customerName = 'Name is required';
  }

  if (!formData.value.customerEmail?.trim()) {
    errors.value.customerEmail = 'Email is required';
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.value.customerEmail)) {
    errors.value.customerEmail = 'Please enter a valid email';
  }

  if (!formData.value.customerPhone?.trim()) {
    errors.value.customerPhone = 'Phone number is required';
  }

  return Object.keys(errors.value).length === 0;
};

const submitReservation = async () => {
  if (!validateForm()) {
    return;
  }

  isSubmitting.value = true;
  error.value = null;

  try {
    const reservation = await api.createReservation(formData.value);
    // Navigate to confirmation with real booking ID
    router.push(`/confirmation/${reservation.id}`);
  } catch (err: any) {
    console.error(err);
    error.value = err.response?.data?.detail || 'Gagal membuat resevasi. Silakan coba lagi.';
    isSubmitting.value = false;
  }
};

const incrementGuests = () => {
  if (formData.value.guests! < 20) {
    formData.value.guests!++;
  }
};

const decrementGuests = () => {
  if (formData.value.guests! > 1) {
    formData.value.guests!--;
  }
};
</script>

<template>
  <!-- Loading State -->
  <div v-if="loading" class="min-h-screen flex items-center justify-center bg-dark-50">
    <div class="text-xl text-dark-600 font-semibold animate-pulse">Memuat data reservasi...</div>
  </div>

  <div v-else-if="restaurant" class="min-h-screen bg-dark-50 py-12">
    <div class="container-custom max-w-4xl">
      <!-- Header -->
      <div class="mb-8">
        <router-link
          :to="`/restaurant/${restaurant.id}`"
          class="text-primary-600 hover:text-primary-700 font-medium mb-4 inline-block"
        >
          ← Kembali ke {{ restaurant.name }}
        </router-link>
        <h1 class="text-4xl font-display font-bold text-dark-900 mb-2">
          Buat Reservasi
        </h1>
        <div class="flex items-center gap-3 text-lg text-dark-600">
          <span>{{ restaurant.name }} • {{ restaurant.location }}</span>
          <span class="text-dark-300">|</span>
          <span class="flex items-center gap-1 text-primary-600 font-medium">
            <UserGroupIcon class="w-5 h-5" />
            {{ totalBookings }} orang telah memesan
          </span>
        </div>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Form -->
        <div class="lg:col-span-2">
          <form @submit.prevent="submitReservation" class="card space-y-6">
            <!-- Date & Time -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <!-- Date -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  <CalendarIcon class="w-4 h-4 inline mr-1" />
                  Tanggal
                </label>
                <input
                  v-model="formData.date"
                  type="date"
                  :min="minDate"
                  :max="maxDate"
                  class="input"
                  :class="{ 'input-error': errors.date }"
                />
                <p v-if="errors.date" class="text-sm text-red-600 mt-1">{{ errors.date }}</p>
              </div>

              <!-- Time -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  <ClockIcon class="w-4 h-4 inline mr-1" />
                  Waktu
                </label>
                <select
                  v-model="formData.time"
                  class="input"
                  :class="{ 'input-error': errors.time }"
                  :disabled="!formData.date"
                >
                  <option value="">Pilih waktu</option>
                  <option v-for="slot in availableTimeSlots" :key="slot" :value="slot">
                    {{ slot }}
                  </option>
                </select>
                <p v-if="errors.time" class="text-sm text-red-600 mt-1">{{ errors.time }}</p>
              </div>
            </div>

            <!-- Guests -->
            <div>
              <label class="block text-sm font-semibold text-dark-700 mb-2">
                <UserGroupIcon class="w-4 h-4 inline mr-1" />
                Jumlah Tamu
              </label>
              <div class="flex items-center gap-4">
                <button
                  type="button"
                  @click="decrementGuests"
                  class="w-12 h-12 rounded-lg border-2 border-dark-200 hover:border-primary-500 hover:bg-primary-50 transition-colors font-bold text-xl"
                  :disabled="formData.guests === 1"
                >
                  −
                </button>
                <div class="flex-1 text-center">
                  <div class="text-3xl font-bold text-dark-900">{{ formData.guests }}</div>
                  <div class="text-sm text-dark-600">Tamu</div>
                </div>
                <button
                  type="button"
                  @click="incrementGuests"
                  class="w-12 h-12 rounded-lg border-2 border-dark-200 hover:border-primary-500 hover:bg-primary-50 transition-colors font-bold text-xl"
                  :disabled="formData.guests === 20"
                >
                  +
                </button>
              </div>
              <p v-if="errors.guests" class="text-sm text-red-600 mt-1">{{ errors.guests }}</p>
            </div>

            <hr class="border-dark-200" />

            <!-- Contact Information -->
            <div class="space-y-4">
              <h3 class="text-lg font-display font-bold text-dark-900">Informasi Kontak</h3>

              <!-- Name -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Nama Lengkap
                </label>
                <input
                  v-model="formData.customerName"
                  type="text"
                  placeholder="John Doe"
                  class="input"
                  :class="{ 'input-error': errors.customerName }"
                />
                <p v-if="errors.customerName" class="text-sm text-red-600 mt-1">{{ errors.customerName }}</p>
              </div>

              <!-- Email -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Email Address
                </label>
                <input
                  v-model="formData.customerEmail"
                  type="email"
                  placeholder="john@example.com"
                  class="input"
                  :class="{ 'input-error': errors.customerEmail }"
                />
                <p v-if="errors.customerEmail" class="text-sm text-red-600 mt-1">{{ errors.customerEmail }}</p>
              </div>

              <!-- Phone -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Nomor Telepon
                </label>
                <input
                  v-model="formData.customerPhone"
                  type="tel"
                  placeholder="+62 812 3456 7890"
                  class="input"
                  :class="{ 'input-error': errors.customerPhone }"
                />
                <p v-if="errors.customerPhone" class="text-sm text-red-600 mt-1">{{ errors.customerPhone }}</p>
              </div>

              <!-- Special Requests -->
              <div>
                <label class="block text-sm font-semibold text-dark-700 mb-2">
                  Permintaan Khusus (Opsional)
                </label>
                <textarea
                  v-model="formData.specialRequests"
                  rows="4"
                  placeholder="Alergi makanan, preferensi meja, atau acara khusus..."
                  class="input resize-none"
                ></textarea>
              </div>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              class="btn-primary w-full text-lg"
              :disabled="isSubmitting"
            >
              <span v-if="isSubmitting" class="flex items-center justify-center gap-2">
                <span class="w-5 h-5 border-2 border-primary-50 border-t-transparent rounded-full animate-spin"></span>
                Memproses...
              </span>
              <span v-else>Konfirmasi Reservasi</span>
            </button>
            <p v-if="error" class="text-sm text-red-600 text-center font-semibold">{{ error }}</p>
          </form>
        </div>

        <!-- Summary Sidebar -->
        <div class="lg:col-span-1">
          <div class="sticky top-20 card space-y-4">
            <h3 class="text-lg font-display font-bold text-dark-900">
              Ringkasan Reservasi
            </h3>

            <div class="space-y-3 text-sm">
              <div class="flex justify-between">
                <span class="text-dark-600">Restoran</span>
                <span class="font-semibold text-dark-900">{{ restaurant.name }}</span>
              </div>

              <div class="flex justify-between">
                <span class="text-dark-600">Tanggal</span>
                <span class="font-semibold text-dark-900">
                  {{ formData.date || '—' }}
                </span>
              </div>

              <div class="flex justify-between">
                <span class="text-dark-600">Waktu</span>
                <span class="font-semibold text-dark-900">
                  {{ formData.time || '—' }}
                </span>
              </div>

              <div class="flex justify-between">
                <span class="text-dark-600">Tamu</span>
                <span class="font-semibold text-dark-900">
                  {{ formData.guests }} Tamu
                </span>
              </div>
            </div>

            <hr class="border-dark-200" />

            <div class="bg-primary-50 rounded-lg p-4">
              <p class="text-xs text-primary-800">
                <strong>Catatan:</strong> Reservasi Anda akan dikonfirmasi melalui email. Harap tiba 10 menit sebelum waktu reservasi Anda.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Restaurant Not Found -->
  <div v-else class="min-h-screen flex items-center justify-center">
    <div class="text-center">
      <div class="text-6xl mb-4">🍽️</div>
      <h1 class="text-3xl font-display font-bold text-dark-900 mb-2">
        Restoran Tidak Ditemukan
      </h1>
      <p class="text-dark-600 mb-6">
        Restoran yang Anda cari tidak tersedia.
      </p>
      <router-link to="/restaurants" class="btn-primary">
        Jelajahi Restoran
      </router-link>
    </div>
  </div>
</template>
