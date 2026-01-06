<script setup lang="ts">
import { computed, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '../services/api';
import type { Restaurant } from '../types';
import { 
  StarIcon, 
  MapPinIcon, 
  PhoneIcon, 
  ClockIcon, 
  ChevronLeftIcon,
  CheckBadgeIcon,
  InformationCircleIcon,
  PhotoIcon,
  UsersIcon,
  SparklesIcon,
  ShoppingBagIcon,
  FireIcon
} from '@heroicons/vue/24/solid';
import { 
  HeartIcon, 
  ShareIcon,
  GlobeAltIcon
} from '@heroicons/vue/24/outline';

interface Props {
  id: string;
}

const props = defineProps<Props>();
const router = useRouter();
const isLoaded = ref(false);
const restaurant = ref<Restaurant | undefined>(undefined);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    restaurant.value = await api.getRestaurant(props.id);
  } catch (err) {
    error.value = 'Gagal memuat detail restoran.';
    console.error(err);
  } finally {
    loading.value = false;
    setTimeout(() => {
      isLoaded.value = true;
    }, 100);
  }
});

const goToReservation = () => {
  if (restaurant.value) {
    router.push(`/reservation/${restaurant.value.id}`);
  }
};

const priceRangeDisplay = computed(() => {
  if (!restaurant.value) return '';
  const ranges: Record<string, string> = {
    'budget': 'Rp 50rb - 100rb',
    'cheap': 'Rp < 50rb',
    'moderate': 'Rp 100rb - 500rb',
    'fine-dining': 'Rp 500rb - 1jt+',
    'expensive': 'Rp 500rb - 1jt+'
  };
  return ranges[restaurant.value.priceRange] || restaurant.value.priceRange;
});

const translateDay = (day: string) => {
  const translations: Record<string, string> = {
    monday: 'Senin',
    tuesday: 'Selasa',
    wednesday: 'Rabu',
    thursday: 'Kamis',
    friday: 'Jumat',
    saturday: 'Sabtu',
    sunday: 'Minggu'
  };
  return translations[day.toLowerCase()] || day;
};

const isCurrentlyOpen = computed(() => {
  if (!restaurant.value) return false;
  
  const now = new Date();
  const dayNames = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
  const today = dayNames[now.getDay()];
  const hours = restaurant.value.openingHours[today as keyof typeof restaurant.value.openingHours];
  
  if (!hours) return false;
  
  const [openH, openM] = hours.open.split(':').map(Number);
  const [closeH, closeM] = hours.close.split(':').map(Number);
  
  const currentTime = now.getHours() * 60 + now.getMinutes();
  const openTime = (openH || 0) * 60 + (openM || 0);
  const closeTime = (closeH || 0) * 60 + (closeM || 0);
  
  // Handle closing times past midnight (e.g., 00:00)
  const adjustedCloseTime = closeTime === 0 ? 24 * 60 : closeTime;
  
  return currentTime >= openTime && currentTime < adjustedCloseTime;
});
</script>

<template>
  <div class="min-h-screen bg-slate-50 selection:bg-accent-200">
    <!-- Loading State -->
    <div v-if="loading" class="min-h-screen flex items-center justify-center bg-white">
      <div class="flex flex-col items-center gap-6">
        <div class="relative">
          <div class="w-20 h-20 border-4 border-slate-100 border-t-accent-500 rounded-full animate-spin"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <SparklesIcon class="w-10 h-10 text-primary-400 animate-pulse" />
          </div>
        </div>
        <p class="text-slate-500 font-display text-xl animate-pulse font-bold">Mempersiapkan Meja Anda...</p>
      </div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="min-h-screen flex flex-col items-center justify-center p-4">
      <div class="text-xl text-red-600 mb-4">{{ error }}</div>
      <button @click="router.back()" class="px-6 py-2 bg-primary-600 text-white rounded-full hover:bg-primary-700 transition-colors">Kembali</button>
    </div>

    <!-- Main Content -->
    <div v-else-if="restaurant">
      <!-- Immersive Hero Section -->
      <section class="relative h-[70vh] min-h-[500px] overflow-hidden">
        <!-- Background Image with Parallax-like effect -->
        <div class="absolute inset-0 transition-transform duration-1000 scale-105">
          <img
            :src="restaurant.images[0]"
            :alt="restaurant.name"
            class="w-full h-full object-cover"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-black/20"></div>
        </div>

        <!-- Hero Content -->
        <div class="container-custom relative h-full flex flex-col justify-end pb-12 z-20">
        <button 
          @click="router.back()"
          class="absolute top-8 left-4 md:left-8 group flex items-center gap-2 px-4 py-2 rounded-full glass text-primary-900 font-semibold hover:bg-white transition-all shadow-lg"
        >
          <ChevronLeftIcon class="w-5 h-5 group-hover:-translate-x-1 transition-transform" />
          Kembali
        </button>

        <div class="max-w-4xl animate-fade-in-up">
          <div class="flex flex-wrap items-center gap-3 mb-6">
            <span class="px-4 py-1.5 rounded-full bg-accent-500 text-white text-xs font-bold tracking-wider uppercase shadow-lg">
              {{ restaurant.cuisine }}
            </span>
            <div :class="[
              'px-4 py-1.5 rounded-full text-xs font-bold tracking-wider uppercase shadow-lg flex items-center gap-2 border',
              isCurrentlyOpen ? 'bg-emerald-500 text-white border-emerald-400' : 'bg-rose-500 text-white border-rose-400'
            ]">
              <span class="relative flex h-2 w-2">
                <span :class="[
                  'animate-ping absolute inline-flex h-full w-full rounded-full opacity-75',
                  isCurrentlyOpen ? 'bg-emerald-200' : 'bg-rose-200'
                ]"></span>
                <span :class="[
                  'relative inline-flex rounded-full h-2 w-2',
                  isCurrentlyOpen ? 'bg-emerald-100' : 'bg-rose-100'
                ]"></span>
              </span>
              {{ isCurrentlyOpen ? 'Buka Sekarang' : 'Tutup' }}
            </div>
            <span class="px-4 py-1.5 rounded-full glass text-primary-900 text-xs font-bold tracking-wider uppercase shadow-lg">
              {{ priceRangeDisplay }}
            </span>
          </div>

          <h1 class="text-4xl md:text-6xl lg:text-7xl font-display font-black text-white mb-6 leading-tight drop-shadow-2xl">
            {{ restaurant.name }}
          </h1>

          <div class="flex flex-wrap items-center gap-6 text-white/90">
            <div class="flex items-center gap-2 group">
              <div class="p-2 rounded-lg bg-white/10 backdrop-blur-md group-hover:bg-accent-500 transition-colors">
                <StarIcon class="w-6 h-6 text-yellow-400" />
              </div>
              <div>
                <p class="text-2xl font-bold leading-none">{{ restaurant.rating }}</p>
                <p class="text-xs opacity-75 uppercase tracking-tighter">{{ restaurant.reviewCount }} ulasan</p>
              </div>
            </div>
            
            <div class="w-px h-10 bg-white/20 hidden sm:block"></div>

            <div class="flex items-center gap-3 group">
              <div class="p-2 rounded-lg bg-white/10 backdrop-blur-md group-hover:bg-primary-500 transition-colors">
                <MapPinIcon class="w-6 h-6 text-white" />
              </div>
              <p class="text-lg font-medium">{{ restaurant.location }}</p>
            </div>
          </div>
        </div>

        <!-- Sticky Reservation Overlay (Mobile) -->
        <div class="md:hidden mt-8">
          <button @click="goToReservation" class="w-full btn-primary py-4 rounded-2xl text-lg shadow-2xl animate-pulse">
            Pesan Meja Sekarang
          </button>
        </div>
      </div>
    </section>

    <!-- Content Sections -->
    <div class="container-custom relative z-30 -mt-8">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-12">
        
        <!-- Left Column: Details -->
        <div class="lg:col-span-2 space-y-8">
          
          <!-- Quick Info Bar -->
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4 animate-fade-in-up delay-100">
            <div class="card bg-white p-5 flex flex-col items-center text-center gap-2 group hover:border-accent-400">
              <UsersIcon class="w-6 h-6 text-primary-600 group-hover:scale-110 transition-transform" />
              <p class="text-xs text-slate-500 uppercase tracking-widest font-bold">Kapasitas</p>
              <p class="text-lg font-bold text-slate-900">{{ restaurant.capacity }} Kursi</p>
            </div>
            <div class="card bg-white p-5 flex flex-col items-center text-center gap-2 group hover:border-accent-400">
              <CheckBadgeIcon class="w-6 h-6 text-emerald-600 group-hover:scale-110 transition-transform" />
              <p class="text-xs text-slate-500 uppercase tracking-widest font-bold">Verified</p>
              <p class="text-lg font-bold text-slate-900">Restoran</p>
            </div>
            <div class="card bg-white p-5 flex flex-col items-center text-center gap-2 group hover:border-accent-400">
              <SparklesIcon class="w-6 h-6 text-amber-500 group-hover:scale-110 transition-transform" />
              <p class="text-xs text-slate-500 uppercase tracking-widest font-bold">Cuisine</p>
              <p class="text-lg font-bold text-slate-900">{{ restaurant.cuisine }}</p>
            </div>
            <div class="card bg-white p-5 flex flex-col items-center text-center gap-2 group hover:border-accent-400">
              <GlobeAltIcon class="w-6 h-6 text-blue-500 group-hover:scale-110 transition-transform" />
              <p class="text-xs text-slate-500 uppercase tracking-widest font-bold">Respon</p>
              <p class="text-lg font-bold text-slate-900">Cepat</p>
            </div>
          </div>

          <!-- Description Card -->
          <div class="card bg-white p-8 md:p-10 space-y-6 animate-fade-in-up delay-200">
            <div class="flex items-center gap-4">
              <div class="h-1 bg-accent-500 w-12 rounded-full"></div>
              <h2 class="text-2xl font-display font-black text-slate-900 uppercase tracking-tight">
                Tentang Kami
              </h2>
            </div>
            <p class="text-slate-700 leading-relaxed text-lg font-medium italic border-l-4 border-primary-200 pl-6 py-2">
              "{{ restaurant.description }}"
            </p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 pt-4">
              <div class="space-y-4">
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                  <InformationCircleIcon class="w-5 h-5 text-primary-500" />
                  Keunggulan
                </h3>
                <div class="flex flex-wrap gap-2">
                  <span v-for="feature in restaurant.features" :key="feature" 
                    class="px-4 py-2 bg-slate-100 rounded-lg text-sm text-slate-700 font-semibold border border-slate-200 hover:bg-white hover:border-accent-400 transition-all cursor-default">
                    ● {{ feature }}
                  </span>
                </div>
              </div>
              
              <div class="space-y-4">
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                  <ClockIcon class="w-5 h-5 text-primary-500" />
                  Jam Buka Hari Ini
                </h3>
                <div class="p-4 bg-primary-50 rounded-2xl border border-primary-100 relative overflow-hidden group">
                  <!-- Decorative Circle -->
                  <div class="absolute -right-4 -bottom-4 w-24 h-24 bg-primary-200/30 rounded-full blur-2xl group-hover:scale-150 transition-transform duration-700"></div>
                  
                  <div class="relative z-10 flex justify-between items-center">
                    <span class="text-primary-900 font-bold capitalize">
                      {{ translateDay(new Date().toLocaleDateString('en-US', { weekday: 'long' })) }}
                    </span>
                    <span class="text-2xl font-display font-black text-primary-700">
                      {{ restaurant.openingHours[new Date().toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase() as keyof typeof restaurant.openingHours]?.open }} - 
                      {{ restaurant.openingHours[new Date().toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase() as keyof typeof restaurant.openingHours]?.close }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Menu Section -->
          <div v-if="restaurant.menu && restaurant.menu.length > 0" class="space-y-8 animate-fade-in-up delay-300">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-4">
                <div class="h-1 bg-accent-500 w-12 rounded-full"></div>
                <h2 class="text-2xl font-display font-black text-slate-900 uppercase tracking-tight flex items-center gap-2">
                  <ShoppingBagIcon class="w-6 h-6 text-primary-500" />
                  Menu Andalan
                </h2>
              </div>
              <div class="flex gap-2">
                <span class="px-3 py-1 bg-primary-100 text-primary-700 text-xs font-bold rounded-full uppercase">Pilihan Koki</span>
              </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div v-for="item in restaurant.menu" :key="item.id" 
                class="group flex gap-4 p-4 bg-white rounded-3xl border border-slate-100 shadow-sm hover:shadow-xl hover:border-accent-200 transition-all">
                <div class="relative w-24 h-24 sm:w-32 sm:h-32 rounded-2xl overflow-hidden flex-shrink-0">
                  <img :src="item.image" :alt="item.name" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" />
                  <div v-if="item.isBestSeller" class="absolute top-2 left-2 p-1.5 bg-amber-500 text-white rounded-lg shadow-lg">
                    <FireIcon class="w-4 h-4" />
                  </div>
                </div>
                
                <div class="flex flex-col justify-between py-1 flex-1">
                  <div>
                    <div class="flex justify-between items-start gap-2">
                      <h3 class="font-bold text-slate-900 group-hover:text-primary-600 transition-colors line-clamp-1">
                        {{ item.name }}
                      </h3>
                      <span class="text-sm font-black text-primary-700 whitespace-nowrap">
                        Rp {{ (item.price / 1000).toLocaleString() }}rb
                      </span>
                    </div>
                    <p class="text-xs text-slate-500 mt-1 line-clamp-2 leading-relaxed">
                      {{ item.description }}
                    </p>
                  </div>
                  
                  <div class="flex items-center justify-between mt-2">
                    <span class="px-2 py-0.5 bg-slate-100 text-[10px] font-bold text-slate-500 rounded uppercase tracking-wider">
                      {{ item.category }}
                    </span>
                    <button class="p-1 px-3 bg-primary-50 text-primary-600 rounded-full text-[10px] font-black hover:bg-primary-600 hover:text-white transition-all uppercase tracking-widest">
                      Detail
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Featured Gallery -->
          <div class="space-y-6 animate-fade-in-up delay-300">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-4">
                <div class="h-1 bg-accent-500 w-12 rounded-full"></div>
                <h2 class="text-2xl font-display font-black text-slate-900 uppercase tracking-tight">
                  Galeri Foto
                </h2>
              </div>
              <button class="text-primary-600 font-bold text-sm hover:text-accent-600 transition-colors flex items-center gap-2">
                Lihat Semua <PhotoIcon class="w-4 h-4" />
              </button>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
              <div v-for="(img, idx) in restaurant.images" :key="idx" 
                class="group relative aspect-square rounded-3xl overflow-hidden shadow-xl"
                :class="idx === 0 ? 'md:col-span-2 md:row-span-2 aspect-auto' : ''">
                <img :src="img" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" />
                <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                  <span class="p-3 bg-white/20 backdrop-blur-md rounded-full text-white">
                    <SparklesIcon class="w-8 h-8" />
                  </span>
                </div>
              </div>
            </div>
          </div>

          <!-- Detailed Opening Hours List -->
          <div class="card bg-white p-8 md:p-10 animate-fade-in-up delay-400">
            <div class="flex items-center gap-4 mb-8">
              <div class="h-1 bg-accent-500 w-12 rounded-full"></div>
              <h2 class="text-2xl font-display font-black text-slate-900 uppercase tracking-tight">
                Jadwal Operasional Lengkap
              </h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-4">
              <div v-for="(hours, day) in restaurant.openingHours" :key="day" 
                class="flex items-center justify-between py-3 border-b border-slate-100 last:border-0 hover:bg-slate-50 px-2 rounded-lg transition-colors group">
                <span :class="[
                  'text-lg font-bold capitalize transition-colors',
                  day === new Date().toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase() ? 'text-primary-600' : 'text-slate-600'
                ]">
                  {{ translateDay(day as string) }}
                  <span v-if="day === new Date().toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase()" 
                    class="ml-2 text-[10px] bg-primary-100 px-2 py-0.5 rounded-full uppercase tracking-tighter">Hari Ini</span>
                </span>
                <span class="font-mono font-bold text-slate-900 group-hover:text-primary-700">
                  {{ hours.open }} — {{ hours.close }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Sidebar -->
        <div class="lg:col-span-1">
          <div class="sticky top-28 space-y-6">
            
            <!-- Reservation Card VIP Style -->
            <div class="card p-0 overflow-hidden shadow-[0_30px_60px_-15px_rgba(0,0,0,0.15)] bg-white border-0 animate-scale-in">
              <div class="relative gradient-primary p-8 text-white">
                <!-- Batik Overlay in reservation card -->
                <div class="absolute inset-0 opacity-10" style="background-image: url('/src/assets/batik-bg.png'); background-size: 150px; background-repeat: repeat;"></div>
                
                <div class="relative z-10 flex flex-col items-center text-center">
                  <div class="w-16 h-16 bg-white/20 backdrop-blur-md rounded-2xl flex items-center justify-center mb-4 shadow-xl border border-white/30">
                    <SparklesIcon class="w-8 h-8 text-white" />
                  </div>
                  <h3 class="text-3xl font-display font-black mb-2">Pesan Kursi</h3>
                  <p class="text-primary-50 text-sm font-semibold opacity-90 leading-relaxed">
                    Pastikan pengalaman bersantap Anda sempurna dengan reservasi meja terlebih dahulu.
                  </p>
                </div>
              </div>
              
              <div class="p-8 space-y-6">
                <!-- Social & Utility -->
                <div class="grid grid-cols-2 gap-4">
                  <button class="flex flex-col items-center gap-2 p-4 bg-slate-50 rounded-2xl border border-slate-100 hover:border-accent-400 transition-all group">
                    <HeartIcon class="w-6 h-6 text-slate-400 group-hover:text-rose-500 transition-colors" />
                    <span class="text-xs font-bold text-slate-600">Simpan</span>
                  </button>
                  <button class="flex flex-col items-center gap-2 p-4 bg-slate-50 rounded-2xl border border-slate-100 hover:border-accent-400 transition-all group">
                    <ShareIcon class="w-6 h-6 text-slate-400 group-hover:text-primary-500 transition-colors" />
                    <span class="text-xs font-bold text-slate-600">Bagikan</span>
                  </button>
                </div>

                <div class="space-y-3">
                  <div class="flex items-center gap-4 text-sm font-bold text-slate-700">
                    <CheckBadgeIcon class="w-10 h-10 text-emerald-500 p-2 bg-emerald-50 rounded-xl" />
                    Konfirmasi Instan via Email
                  </div>
                  <div class="flex items-center gap-4 text-sm font-bold text-slate-700">
                    <UsersIcon class="w-10 h-10 text-primary-500 p-2 bg-primary-50 rounded-xl" />
                    Batas Grup: 1-20 Orang
                  </div>
                </div>

                <button 
                  @click="goToReservation" 
                  class="group relative w-full btn-primary py-5 rounded-3xl text-xl shadow-2xl overflow-hidden hover-glow"
                >
                  <div class="absolute inset-0 bg-gradient-to-r from-accent-600 to-accent-400 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                  <span class="relative z-10 flex items-center justify-center gap-3">
                    Booking Meja
                    <ChevronLeftIcon class="w-6 h-6 rotate-180" />
                  </span>
                </button>
                
                <p class="text-[10px] text-center text-slate-400 font-bold uppercase tracking-widest">
                  100% Gratis Tanpa Biaya Booking
                </p>
              </div>
            </div>

            <!-- Quick Contact Block -->
            <div class="card bg-white p-8 space-y-6 shadow-xl relative overflow-hidden group border border-slate-100">
              <!-- Animated Glow -->
              <div class="absolute top-0 right-0 w-32 h-32 bg-primary-500/5 rounded-full blur-3xl group-hover:bg-primary-500/10 transition-colors duration-700"></div>
              
              <h4 class="text-lg font-display font-black uppercase tracking-tighter text-primary-900">Hubungi Langsung</h4>
              <div class="space-y-4 relative z-10">
                <a :href="`tel:${restaurant.phone}`" class="flex items-center gap-4 hover:bg-primary-50 p-3 rounded-2xl transition-all">
                  <div class="w-10 h-10 bg-primary-100 rounded-xl flex items-center justify-center ring-1 ring-primary-200">
                    <PhoneIcon class="w-5 h-5 text-primary-600" />
                  </div>
                  <div>
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest">Telepon</p>
                    <p class="text-lg font-bold text-primary-900">{{ restaurant.phone }}</p>
                  </div>
                </a>
                
                <div class="flex items-center gap-4 hover:bg-primary-50 p-3 rounded-2xl transition-all">
                  <div class="w-10 h-10 bg-primary-100 rounded-xl flex items-center justify-center ring-1 ring-primary-200">
                    <MapPinIcon class="w-5 h-5 text-primary-600" />
                  </div>
                  <div>
                    <p class="text-xs text-slate-500 font-bold uppercase tracking-widest">Alamat</p>
                    <p class="text-xs font-semibold leading-relaxed text-slate-700">{{ restaurant.address }}</p>
                  </div>
                </div>
              </div>
            </div>
            
          </div>
        </div>
      </div>
    </div>
  </div>

  </div>
</template>

<style scoped>
.glass {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.hover-glow:hover {
  box-shadow: 0 0 30px rgba(var(--color-accent), 0.3);
}

.hover-scale {
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.hover-scale:hover {
  transform: scale(1.05);
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.animate-float {
  animation: float 4s ease-in-out infinite;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #a67c52;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #8b6f47;
}
</style>
