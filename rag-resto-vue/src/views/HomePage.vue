<script setup lang="ts">
import { RouterLink } from 'vue-router';
import { MagnifyingGlassIcon, SparklesIcon, ClockIcon, CheckCircleIcon, MapPinIcon, StarIcon } from '@heroicons/vue/24/outline';
import RestaurantCard from '../components/restaurant/RestaurantCard.vue';
import { mockRestaurants } from '../data/mockData';

const featuredRestaurants = mockRestaurants.slice(0, 3);

const features = [
  {
    icon: MagnifyingGlassIcon,
    title: 'Jelajahi',
    description: 'Temukan ratusan restoran masakan Nusantara terbaik di kota Anda'
  },
  {
    icon: ClockIcon,
    title: 'Reservasi',
    description: 'Pesan meja Anda secara instan dengan ketersediaan real-time'
  },
  {
    icon: CheckCircleIcon,
    title: 'Nikmati',
    description: 'Datang dan nikmati hidangan lezat - kami yang mengurus sisanya'
  }
];

const cuisineTypes = [
  { name: 'Jawa', icon: '🍛', count: 150 },
  { name: 'Sunda', icon: '🥗', count: 120 },
  { name: 'Padang', icon: '🍖', count: 95 },
  { name: 'Bali', icon: '🦆', count: 80 },
  { name: 'Betawi', icon: '🍜', count: 65 },
  { name: 'Manado', icon: '🌶️', count: 55 },
];
</script>

<template>
  <div class="min-h-screen">
    <!-- Hero Section dengan Background Batik -->
    <section class="relative overflow-hidden py-20 md:py-32 bg-gradient-to-br from-primary-950 via-primary-900 to-primary-800">
      <!-- Batik Background Pattern -->
      <div 
        class="absolute inset-0 opacity-10"
        style="background-image: url('/src/assets/batik-bg.png'); background-size: 400px; background-repeat: repeat;"
      ></div>
      
      <!-- Decorative Overlay -->
      <div class="absolute inset-0 bg-gradient-to-b from-primary-950/80 via-primary-900/60 to-primary-900"></div>
      
      <!-- Ornamental Elements -->
      <div class="absolute top-10 right-10 w-64 h-64 border-4 border-accent-400/20 rounded-full"></div>
      <div class="absolute bottom-10 left-10 w-48 h-48 border-4 border-accent-400/20 rounded-full"></div>
      
      <div class="container-custom relative z-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <!-- Left Content -->
          <div class="text-primary-50 space-y-8 animate-fade-in">
            <!-- Badge -->
            <div class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20">
              <SparklesIcon class="w-5 h-5 text-accent-300" />
              <span class="text-sm font-semibold text-accent-100">Cita Rasa Nusantara Terbaik</span>
            </div>

            <!-- Main Heading -->
            <div>
              <h1 class="text-5xl md:text-6xl lg:text-7xl font-display font-bold leading-tight mb-4">
                Jelajahi Kelezatan
                <span class="block text-accent-300">
                  Kuliner Indonesia
                </span>
              </h1>
              <p class="text-xl text-primary-100 max-w-xl leading-relaxed">
                Temukan dan pesan meja di restoran-restoran masakan Indonesia terbaik. 
                Dari warung tradisional hingga fine dining Nusantara.
              </p>
            </div>

            <!-- CTA Buttons -->
            <div class="flex flex-col sm:flex-row items-start gap-4">
              <RouterLink 
                to="/restaurants" 
                class="btn bg-amber-500 hover:bg-amber-600 text-primary-950 font-bold border-0 text-lg shadow-xl hover:shadow-2xl transform hover:scale-105 transition-all"
              >
                <MagnifyingGlassIcon class="w-5 h-5" />
                Jelajahi Restoran
              </RouterLink>
              <RouterLink 
                to="/ai-reservation" 
                class="btn bg-primary-50 hover:bg-primary-100 text-primary-950 font-semibold border-2 border-primary-50 text-lg"
              >
                <SparklesIcon class="w-5 h-5" />
                Asisten AI
              </RouterLink>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-3 gap-6 pt-8 border-t border-white/20">
              <div>
                <div class="text-4xl font-display font-bold text-accent-400">500+</div>
                <div class="text-sm text-primary-300 mt-1">Restoran</div>
              </div>
              <div>
                <div class="text-4xl font-display font-bold text-accent-400">50K+</div>
                <div class="text-sm text-primary-300 mt-1">Reservasi</div>
              </div>
              <div>
                <div class="text-4xl font-display font-bold text-accent-400">4.9</div>
                <div class="text-sm text-primary-300 mt-1">Rating</div>
              </div>
            </div>
          </div>

          <!-- Right Image -->
          <div class="hidden lg:block animate-float">
            <div class="relative">
              <div class="absolute inset-0 bg-accent-400/20 rounded-3xl blur-3xl"></div>
              <img 
                src="/src/assets/hero-food.png" 
                alt="Indonesian Cuisine" 
                class="relative rounded-3xl shadow-2xl w-full h-auto"
              />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Cuisine Types Section -->
    <section class="py-16 bg-white border-b-4 border-primary-100">
      <div class="container-custom">
        <div class="text-center mb-10">
          <h2 class="text-3xl font-display font-bold text-primary-900 mb-3">
            Jenis Masakan
          </h2>
          <p class="text-lg text-primary-700">
            Pilih dari berbagai cita rasa Nusantara
          </p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
          <div
            v-for="cuisine in cuisineTypes"
            :key="cuisine.name"
            class="group cursor-pointer"
          >
            <div class="card text-center hover:shadow-xl hover:scale-105 transition-all duration-300 border-2 border-primary-100 hover:border-accent-400">
              <div class="text-5xl mb-3 group-hover:scale-110 transition-transform">
                {{ cuisine.icon }}
              </div>
              <h3 class="font-display font-bold text-primary-900 mb-1">
                {{ cuisine.name }}
              </h3>
              <p class="text-sm text-primary-600">
                {{ cuisine.count }} restoran
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Restaurants -->
    <section class="py-20 bg-gradient-to-br from-primary-50 via-white to-accent-50">
      <div class="container-custom">
        <div class="text-center mb-12 animate-slide-up">
          <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-accent-100 text-accent-700 font-semibold mb-4">
            <StarIcon class="w-5 h-5" />
            Pilihan Terbaik
          </div>
          <h2 class="text-4xl md:text-5xl font-display font-bold text-primary-900 mb-4">
            Restoran Unggulan
          </h2>
          <p class="text-lg text-primary-700 max-w-2xl mx-auto">
            Pilihan terbaik dari restoran-restoran masakan Indonesia terbaik kami
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <RestaurantCard
            v-for="restaurant in featuredRestaurants"
            :key="restaurant.id"
            :restaurant="restaurant"
            class="animate-slide-up hover:scale-105 transition-transform duration-300"
          />
        </div>

        <div class="text-center mt-12">
          <RouterLink to="/restaurants" class="btn-primary text-lg">
            <MapPinIcon class="w-5 h-5" />
            Lihat Semua Restoran
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section class="py-20 bg-white relative overflow-hidden">
      <!-- Decorative Batik Pattern -->
      <div 
        class="absolute inset-0 opacity-5"
        style="background-image: url('/src/assets/batik-bg.png'); background-size: 300px; background-repeat: repeat;"
      ></div>
      
      <div class="container-custom relative z-10">
        <div class="text-center mb-16">
          <h2 class="text-4xl md:text-5xl font-display font-bold text-primary-900 mb-4">
            Cara Kerja
          </h2>
          <p class="text-lg text-primary-700 max-w-2xl mx-auto">
            Tiga langkah sederhana menuju pengalaman bersantap sempurna Anda
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div
            v-for="(feature, index) in features"
            :key="feature.title"
            class="relative"
          >
            <!-- Connector Line (hidden on mobile) -->
            <div 
              v-if="index < features.length - 1"
              class="hidden md:block absolute top-16 left-1/2 w-full h-1 bg-gradient-to-r from-accent-400 to-accent-200 z-0"
            ></div>
            
            <!-- Feature Card -->
            <div class="relative z-10 text-center space-y-4 p-8 rounded-2xl bg-white hover:shadow-2xl transition-all duration-300 border-2 border-primary-100 hover:border-accent-300">
              <!-- Number Badge -->
              <div class="absolute -top-4 -right-4 w-12 h-12 rounded-full bg-gradient-to-br from-accent-400 to-accent-600 text-primary-50 font-display font-bold text-xl flex items-center justify-center shadow-lg">
                {{ index + 1 }}
              </div>
              
              <!-- Icon -->
              <div class="inline-flex items-center justify-center w-20 h-20 rounded-2xl bg-gradient-to-br from-primary-600 to-primary-800 shadow-xl">
                <component :is="feature.icon" class="w-10 h-10 text-primary-50" />
              </div>
              
              <!-- Title -->
              <h3 class="text-2xl font-display font-bold text-primary-900">
                {{ feature.title }}
              </h3>
              
              <!-- Description -->
              <p class="text-primary-700 leading-relaxed">
                {{ feature.description }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section dengan Batik -->
    <section class="relative py-20 overflow-hidden bg-gradient-to-br from-primary-900 via-primary-800 to-accent-900">
      <!-- Batik Background -->
      <div 
        class="absolute inset-0 opacity-10"
        style="background-image: url('/src/assets/batik-bg.png'); background-size: 400px; background-repeat: repeat;"
      ></div>
      
      <!-- Decorative Elements -->
      <div class="absolute top-0 right-0 w-96 h-96 bg-accent-500/20 rounded-full blur-3xl"></div>
      <div class="absolute bottom-0 left-0 w-96 h-96 bg-primary-500/20 rounded-full blur-3xl"></div>
      
      <div class="container-custom relative z-10 text-center space-y-8">
        <div class="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white/10 backdrop-blur-md border border-white/20 text-accent-200 font-semibold">
          <SparklesIcon class="w-5 h-5" />
          Mulai Sekarang
        </div>
        
        <h2 class="text-4xl md:text-5xl lg:text-6xl font-display font-bold text-primary-50 leading-tight">
          Siap Memesan Meja Anda?
        </h2>
        
        <p class="text-xl text-primary-100 max-w-2xl mx-auto leading-relaxed">
          Bergabunglah dengan ribuan pecinta kuliner yang mempercayai kami untuk reservasi bersantap mereka
        </p>
        
        <div class="flex flex-col sm:flex-row items-center justify-center gap-4 pt-4">
          <RouterLink 
            to="/restaurants" 
            class="btn bg-amber-500 hover:bg-amber-600 text-primary-950 font-bold border-0 text-lg shadow-xl hover:shadow-2xl transform hover:scale-105 transition-all"
          >
            Mulai Sekarang
          </RouterLink>
          <RouterLink 
            to="/ai-reservation" 
            class="btn bg-primary-50 hover:bg-primary-100 text-primary-950 font-semibold border-2 border-primary-50 text-lg"
          >
            <SparklesIcon class="w-5 h-5" />
            Coba Asisten AI
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* Additional custom styles for Nusantara theme */
.batik-overlay::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url('/src/assets/batik-bg.png');
  background-size: 300px;
  background-repeat: repeat;
  opacity: 0.03;
  pointer-events: none;
}
</style>
