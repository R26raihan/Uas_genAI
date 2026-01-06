<script setup lang="ts">
import { computed } from 'vue';

interface Props {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  fullWidth?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  disabled: false,
  loading: false,
  fullWidth: false,
});

const buttonClasses = computed(() => {
  const classes = ['btn'];
  
  // Variant classes
  if (props.variant === 'primary') classes.push('btn-primary');
  else if (props.variant === 'secondary') classes.push('btn-secondary');
  else if (props.variant === 'outline') classes.push('btn-outline');
  else if (props.variant === 'ghost') classes.push('hover:bg-dark-100 text-dark-700');
  
  // Size classes
  if (props.size === 'sm') classes.push('px-4 py-2 text-sm');
  else if (props.size === 'lg') classes.push('px-8 py-4 text-lg');
  
  // Full width
  if (props.fullWidth) classes.push('w-full');
  
  // Disabled/Loading
  if (props.disabled || props.loading) classes.push('opacity-50 cursor-not-allowed');
  
  return classes.join(' ');
});
</script>

<template>
  <button
    :class="buttonClasses"
    :disabled="disabled || loading"
  >
    <span v-if="loading" class="w-5 h-5 border-2 border-primary-50 border-t-transparent rounded-full animate-spin"></span>
    <slot v-else />
  </button>
</template>
