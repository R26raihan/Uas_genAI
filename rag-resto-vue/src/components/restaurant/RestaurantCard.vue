<script setup lang="ts">
import { computed } from 'vue';
import { RouterLink } from 'vue-router';
import type { Restaurant } from '../../types';
import { StarIcon, MapPinIcon } from '@heroicons/vue/24/solid';


interface Props {
  restaurant: Restaurant;
}

const props = defineProps<Props>();

const priceRangeDisplay = computed(() => {
  const ranges: Record<string, string> = {
    'budget': 'Rp 50rb - 100rb',
    'cheap': 'Rp < 50rb',
    'moderate': 'Rp 100rb - 500rb',
    'fine-dining': 'Rp 500rb - 1jt+',
    'expensive': 'Rp 500rb - 1jt+'
  };
  return ranges[props.restaurant.priceRange] || props.restaurant.priceRange;
});

const primaryImage = computed(() => props.restaurant.images[0] || 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800');
</script>

<template>
  <RouterLink
    :to="`/restaurant/${restaurant.id}`"
    class="group block"
  >
    <div class="card-hover overflow-hidden">
      <!-- Image -->
      <div class="relative h-48 overflow-hidden rounded-t-xl">
        <img
          :src="primaryImage"
          :alt="restaurant.name"
          class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
        />
        <div class="absolute top-3 right-3 px-3 py-1 rounded-full glass text-sm font-semibold text-dark-900">
          {{ priceRangeDisplay }}
        </div>
      </div>

      <!-- Content -->
      <div class="p-5 space-y-3">
        <!-- Title & Cuisine -->
        <div>
          <h3 class="font-display font-bold text-xl text-dark-900 group-hover:text-primary-600 transition-colors line-clamp-1">
            {{ restaurant.name }}
          </h3>
          <p class="text-sm text-dark-600 mt-1">{{ restaurant.cuisine }}</p>
        </div>

        <!-- Rating & Reviews -->
        <div class="flex items-center gap-2">
          <div class="flex items-center gap-1">
            <StarIcon class="w-5 h-5 text-yellow-400" />
            <span class="font-semibold text-dark-900">{{ restaurant.rating }}</span>
          </div>
          <span class="text-sm text-dark-500">({{ restaurant.reviewCount }} ulasan)</span>
        </div>

        <!-- Location -->
        <div class="flex items-center gap-2 text-dark-600">
          <MapPinIcon class="w-4 h-4 flex-shrink-0" />
          <span class="text-sm line-clamp-1">{{ restaurant.location }}</span>
        </div>

        <!-- Dynamic Open/Close Status -->
        <div class="flex items-center gap-2">
          <div :class="[
            'px-2 py-0.5 rounded text-[10px] font-bold uppercase tracking-wider',
            restaurant.isOpen ? 'bg-emerald-100 text-emerald-700' : 'bg-rose-100 text-rose-700'
          ]">
            {{ restaurant.isOpen ? 'Buka' : 'Tutup' }}
          </div>
          <span class="text-xs text-dark-500" v-if="restaurant.isOpen">
            — Tutup {{ restaurant.openingHours[new Date().toLocaleDateString('en-US', { weekday: 'long' }).toLowerCase()]?.close }}
          </span>
        </div>

        <!-- CTA Button -->
        <button class="btn-primary w-full mt-4">
          Pesan Meja
        </button>
      </div>
    </div>
  </RouterLink>
</template>
