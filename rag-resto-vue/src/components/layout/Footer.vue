<script setup lang="ts">
import { RouterLink } from 'vue-router';
import { 
  EnvelopeIcon, 
  PhoneIcon, 
  MapPinIcon 
} from '@heroicons/vue/24/outline';

const currentYear = new Date().getFullYear();

const quickLinks = [
  { name: 'Beranda', href: '/' },
  { name: 'Restoran', href: '/restaurants' },
  { name: 'Reservasi AI', href: '/ai-reservation' },
  { name: 'Tentang Kami', href: '#' },
  { name: 'Kontak', href: '#' },
];

const legalLinks = [
  { name: 'Syarat & Ketentuan', href: '#' },
  { name: 'Kebijakan Privasi', href: '#' },
  { name: 'FAQ', href: '#' },
];

</script>

<template>
  <footer class="relative z-50 isolate bg-gradient-to-br from-primary-900 via-primary-800 to-primary-900 text-primary-50 overflow-hidden">
    <!-- Batik Background Pattern -->
    <div 
      class="absolute inset-0 opacity-10 bg-primary-950"
      style="background-image: url('/src/assets/batik-bg.png'); background-size: 200px; background-repeat: repeat;"
    ></div>
    
    <!-- Dark Gradient Overlay for Readability -->
    <div class="absolute inset-0 bg-gradient-to-t from-primary-950 via-primary-900/80 to-primary-950/90"></div>
    
    <!-- Decorative Elements -->
    <div class="absolute top-0 right-0 w-96 h-96 bg-accent-500/10 rounded-full blur-3xl"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-primary-500/10 rounded-full blur-3xl"></div>
    
    <div class="container-custom relative z-10">
      <!-- Main Footer Content -->
      <div class="py-20">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-8 gap-y-12">
          <!-- Brand Section -->
          <div class="lg:col-span-1 space-y-6">
            <div class="flex items-center gap-3">
              <div class="relative">
                <div class="absolute inset-0 rounded-xl bg-gradient-to-br from-accent-500 to-accent-600 blur-md opacity-50"></div>
                <div class="relative w-14 h-14 rounded-xl bg-gradient-to-br from-accent-500 to-accent-600 flex items-center justify-center shadow-xl">
                </div>
              </div>
              <div>
                <span class="text-2xl font-display font-bold text-primary-50">
                  Warung Nusantara
                </span>
                <p class="text-xs text-accent-200 font-medium">Cita Rasa Indonesia</p>
              </div>
            </div>
            <p class="text-primary-100 text-sm leading-relaxed">
              Platform reservasi restoran Indonesia terbaik. Nikmati kelezatan kuliner Nusantara dengan kemudahan reservasi online yang modern dan terpercaya.
            </p>
          </div>

          <!-- Quick Links -->
          <div>
            <h3 class="font-display font-bold text-xl mb-6 text-accent-400">Menu Cepat</h3>
            <ul class="space-y-3">
              <li v-for="link in quickLinks" :key="link.name">
                <RouterLink
                  :to="link.href"
                  class="text-primary-100 hover:text-accent-300 transition-colors text-sm flex items-center gap-2 group"
                >
                  <span class="w-1.5 h-1.5 rounded-full bg-accent-400 group-hover:w-3 transition-all"></span>
                  {{ link.name }}
                </RouterLink>
              </li>
            </ul>
          </div>

          <!-- Legal Links -->
          <div>
            <h3 class="font-display font-bold text-xl mb-6 text-accent-400">Informasi</h3>
            <ul class="space-y-3">
              <li v-for="link in legalLinks" :key="link.name">
                <a
                  :href="link.href"
                  class="text-primary-100 hover:text-accent-300 transition-colors text-sm flex items-center gap-2 group"
                >
                  <span class="w-1.5 h-1.5 rounded-full bg-accent-400 group-hover:w-3 transition-all"></span>
                  {{ link.name }}
                </a>
              </li>
            </ul>
          </div>

          <!-- Contact Info -->
          <div>
            <h3 class="font-display font-bold text-xl mb-6 text-accent-400">Hubungi Kami</h3>
            <ul class="space-y-4">
              <li class="flex items-start gap-3 text-primary-100 text-sm group">
                <div class="w-10 h-10 rounded-lg bg-white/10 backdrop-blur-sm flex items-center justify-center flex-shrink-0 group-hover:bg-accent-500 transition-colors border border-white/20">
                  <MapPinIcon class="w-5 h-5 text-accent-300" />
                </div>
                <div>
                  <p class="font-semibold text-primary-50 mb-1">Alamat</p>
                  <p>Jakarta Pusat, Indonesia</p>
                </div>
              </li>
              <li class="flex items-start gap-3 text-primary-100 text-sm group">
                <div class="w-10 h-10 rounded-lg bg-white/10 backdrop-blur-sm flex items-center justify-center flex-shrink-0 group-hover:bg-accent-500 transition-colors border border-white/20">
                  <PhoneIcon class="w-5 h-5 text-accent-300" />
                </div>
                <div>
                  <p class="font-semibold text-primary-50 mb-1">Telepon</p>
                  <p>+62 21 1234 5678</p>
                </div>
              </li>
              <li class="flex items-start gap-3 text-primary-100 text-sm group">
                <div class="w-10 h-10 rounded-lg bg-white/10 backdrop-blur-sm flex items-center justify-center flex-shrink-0 group-hover:bg-accent-500 transition-colors border border-white/20">
                  <EnvelopeIcon class="w-5 h-5 text-accent-300" />
                </div>
                <div>
                  <p class="font-semibold text-primary-50 mb-1">Email</p>
                  <p>info@warungnusantara.id</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="border-t-2 border-white/10 py-6">
        <div class="flex flex-col md:flex-row items-center justify-between gap-4">
          <p class="text-primary-100 text-sm text-center md:text-left">
            &copy; {{ currentYear }} <span class="font-semibold text-accent-400">Warung Nusantara</span>. Seluruh Hak Cipta Dilindungi.
          </p>
          <div class="flex items-center gap-6 text-sm text-primary-100">
            <a href="#" class="hover:text-accent-400 transition-colors">Syarat & Ketentuan</a>
            <span class="text-primary-50/20">•</span>
            <a href="#" class="hover:text-accent-400 transition-colors">Kebijakan Privasi</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
