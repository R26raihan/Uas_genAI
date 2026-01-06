<script setup lang="ts">
import { ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import { Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline';
import { SparklesIcon } from '@heroicons/vue/24/solid';

const route = useRoute();
const mobileMenuOpen = ref(false);

const navigation = [
  { name: 'Beranda', href: '/' },
  { name: 'Restoran', href: '/restaurants' },
  { name: 'Cek Pesanan', href: '/my-reservations' },
  { name: 'Reservasi AI', href: '/ai-reservation', special: true },
];

const isActive = (path: string) => {
  return route.path === path;
};
</script>

<template>
  <nav class="sticky top-0 z-50 bg-white/95 backdrop-blur-lg border-b-2 border-primary-200 shadow-lg">
    <!-- Batik Pattern Overlay -->
    <div 
      class="absolute inset-0 opacity-5 pointer-events-none"
      style="background-image: url('/src/assets/batik-bg.png'); background-size: 200px; background-repeat: repeat;"
    ></div>
    
    <div class="container-custom relative z-10">
      <div class="flex items-center justify-between min-h-[5rem] py-2">
        <!-- Logo -->
        <RouterLink to="/" class="flex items-center gap-3 group">
          <div class="hidden sm:block py-2">
            <span class="text-2xl md:text-3xl font-display font-bold bg-gradient-to-r from-primary-800 to-primary-600 bg-clip-text text-transparent block">
              Warung Nusantara
            </span>
            <p class="text-xl text-accent-600 font-bold tagline-aesthetic">Cita Rasa Indonesia</p>
          </div>
        </RouterLink>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex items-center gap-2">
          <RouterLink
            v-for="item in navigation.filter(i => !i.special)"
            :key="item.name"
            :to="item.href"
            class="px-5 py-2.5 rounded-lg font-semibold transition-all relative group"
            :class="
              isActive(item.href)
                ? 'text-primary-700 bg-primary-50'
                : 'text-primary-800 hover:text-primary-600 hover:bg-primary-50/50'
            "
          >
            {{ item.name }}
            <span
              class="absolute bottom-1 left-1/2 -translate-x-1/2 w-0 h-1 rounded-full bg-gradient-to-r from-primary-500 to-accent-500 transition-all group-hover:w-3/4"
              :class="{ 'w-3/4': isActive(item.href) }"
            ></span>
          </RouterLink>

          <!-- AI Reservation Special Button -->
          <RouterLink 
            to="/ai-reservation" 
            class="ml-2 px-5 py-2.5 rounded-lg font-semibold transition-all flex items-center gap-2 border-2"
            :class="
              isActive('/ai-reservation')
                ? 'bg-gradient-to-r from-batik-600 to-batik-700 text-primary-50 border-batik-600 shadow-lg'
                : 'bg-gradient-to-r from-batik-500 to-batik-600 text-primary-50 border-batik-500 hover:shadow-xl hover:scale-105'
            "
          >
            <SparklesIcon class="w-4 h-4" />
            <span>Reservasi AI</span>
          </RouterLink>

          <!-- CTA Button -->
          <RouterLink 
            to="/restaurants" 
            class="ml-2 px-6 py-2.5 rounded-lg font-semibold transition-all bg-gradient-to-r from-accent-500 to-accent-600 text-primary-50 hover:from-accent-600 hover:to-accent-700 shadow-lg hover:shadow-xl hover:scale-105 border-2 border-accent-600"
          >
            Lihat Restoran
          </RouterLink>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden p-2.5 rounded-lg hover:bg-primary-50 transition-colors border-2 border-primary-200"
        >
          <Bars3Icon v-if="!mobileMenuOpen" class="w-6 h-6 text-primary-900" />
          <XMarkIcon v-else class="w-6 h-6 text-primary-900" />
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div v-if="mobileMenuOpen" class="md:hidden border-t-2 border-primary-200 bg-white shadow-xl">
        <div class="container-custom py-4 space-y-2">
          <RouterLink
            v-for="item in navigation"
            :key="item.name"
            :to="item.href"
            @click="mobileMenuOpen = false"
            class="block px-5 py-3.5 rounded-lg font-semibold transition-all"
            :class="
              isActive(item.href)
                ? 'bg-gradient-to-r from-primary-600 to-primary-700 text-primary-50 shadow-md'
                : 'text-primary-800 hover:bg-primary-50 border-2 border-primary-100'
            "
          >
            <div class="flex items-center gap-2">
              <SparklesIcon v-if="item.special" class="w-5 h-5" />
              <span>{{ item.name }}</span>
            </div>
          </RouterLink>
          <RouterLink
            to="/restaurants"
            @click="mobileMenuOpen = false"
            class="block px-5 py-3.5 rounded-lg font-semibold text-center bg-gradient-to-r from-accent-500 to-accent-600 text-primary-50 shadow-lg"
          >
            Lihat Restoran
          </RouterLink>
        </div>
      </div>
    </Transition>
  </nav>
</template>
