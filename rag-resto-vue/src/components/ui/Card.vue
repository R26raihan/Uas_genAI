<script setup lang="ts">
import { computed } from 'vue';

interface Props {
  hover?: boolean;
  glass?: boolean;
  padding?: string;
}

const props = withDefaults(defineProps<Props>(), {
  hover: false,
  glass: false,
  padding: 'p-6',
});

const cardClasses = computed(() => {
  const classes = [props.padding, 'rounded-xl', 'transition-all', 'duration-300'];
  
  if (props.glass) {
    classes.push('glass');
  } else {
    classes.push('bg-primary-50', 'shadow-lg');
  }
  
  if (props.hover) {
    classes.push('hover:shadow-xl', 'hover:-translate-y-1', 'cursor-pointer');
  }
  
  return classes.join(' ');
});
</script>

<template>
  <div :class="cardClasses">
    <slot />
  </div>
</template>
