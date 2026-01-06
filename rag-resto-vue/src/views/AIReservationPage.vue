<script setup lang="ts">
import { ref } from 'vue';
import { SparklesIcon, PaperAirplaneIcon } from '@heroicons/vue/24/solid';
import { ChatBubbleLeftRightIcon } from '@heroicons/vue/24/outline';
import { useRouter } from 'vue-router';

import api from '../services/api';

const router = useRouter();

const messages = ref<Array<{ role: 'user' | 'assistant'; content: string }>>([
  {
    role: 'assistant',
    content: 'Selamat datang di Asisten Reservasi Cerdas! 🍽️ Saya akan membantu Anda menemukan restoran Indonesia terbaik. Apa yang Anda cari hari ini?'
  }
]);

const userInput = ref('');
const isLoading = ref(false);

// Booking form state
const showBookingForm = ref(false);
const bookingFormData = ref({
  restaurantId: '',
  restaurantName: '',
  date: '',
  time: '',
  guests: 2,
  customerName: '',
  customerEmail: '',
  customerPhone: '',
  specialRequests: ''
});

const quickSuggestions = [
  'Apa rekomendasi restoran untuk keluarga?',
  'Saya mencari makanan pedas',
  'Restoran dengan suasana romantis',
  'Tempat makan yang buka sampai malam',
];

const sendMessage = async () => {
  if (!userInput.value.trim() || isLoading.value) return;

  const userMessage = userInput.value;
  messages.value.push({
    role: 'user',
    content: userMessage
  });

  userInput.value = '';
  isLoading.value = true;

  try {
    const response = await api.chat(userMessage);
    console.log('AI Response:', response);
    
    const aiResponse = response.response;
    console.log('AI Response Text:', aiResponse);
    
    // Check if response is empty
    if (!aiResponse || aiResponse.trim() === '') {
      messages.value.push({
        role: 'assistant',
        content: 'Maaf, saya tidak mendapat respons yang valid. Silakan coba lagi.'
      });
      return;
    }
    
    // Check if AI wants to show booking form
    if (aiResponse.includes('SHOW_FORM:')) {
      const formMarker = 'SHOW_FORM:';
      const jsonStart = aiResponse.indexOf(formMarker) + formMarker.length;
      const textBeforeJson = aiResponse.substring(0, aiResponse.indexOf(formMarker));
      
      // Extract JSON by finding the first { and matching }
      const restOfText = aiResponse.substring(jsonStart).trim();
      const firstBrace = restOfText.indexOf('{');
      
      if (firstBrace !== -1) {
        let braceCount = 0;
        let jsonEnd = firstBrace;
        
        for (let i = firstBrace; i < restOfText.length; i++) {
          if (restOfText[i] === '{') braceCount++;
          if (restOfText[i] === '}') braceCount--;
          if (braceCount === 0) {
            jsonEnd = i + 1;
            break;
          }
        }
        
        const jsonStr = restOfText.substring(firstBrace, jsonEnd);
        const textAfterJson = restOfText.substring(jsonEnd).trim();
        
        try {
          const formData = JSON.parse(jsonStr);
          console.log('Parsed form data:', formData);
          
          // Show AI message without the JSON part
          let messageContent = '';
          if (textBeforeJson.trim()) {
            messageContent = textBeforeJson.trim();
          }
          if (textAfterJson) {
            messageContent += (messageContent ? '\n\n' : '') + textAfterJson;
          }
          if (messageContent) {
            messageContent += '\n\n📝 Silakan isi form booking di bawah untuk melanjutkan reservasi.';
            messages.value.push({
              role: 'assistant',
              content: messageContent
            });
          }
          
          // Pre-fill form data
          bookingFormData.value.restaurantId = formData.restaurantId || '';
          bookingFormData.value.restaurantName = formData.restaurantName || '';
          showBookingForm.value = true;
          
          console.log('Form should now be visible:', showBookingForm.value);
          
        } catch (parseError) {
          console.error('Error parsing form data:', parseError, 'JSON string:', jsonStr);
          messages.value.push({
            role: 'assistant',
            content: aiResponse
          });
        }
      } else {
        console.error('No JSON object found after SHOW_FORM:');
        messages.value.push({
          role: 'assistant',
          content: aiResponse
        });
      }
    } else {
      // Normal chat response
      messages.value.push({
        role: 'assistant',
        content: aiResponse
      });
    }
  } catch (error) {
    console.error('AI Chat Error:', error);
    messages.value.push({
      role: 'assistant',
      content: 'Maaf, saya sedang mengalami gangguan koneksi. Mohon coba lagi nanti.'
    });
  } finally {
    isLoading.value = false;
  }
};

const submitBooking = async () => {
  if (isLoading.value) return;
  
  isLoading.value = true;
  
  try {
    const reservation = await api.createReservation(bookingFormData.value);
    
    // Navigate to confirmation page with booking ID
    router.push({
      name: 'confirmation',
      params: { id: reservation.id }
    });
    
  } catch (error) {
    console.error('Booking Error:', error);
    messages.value.push({
      role: 'assistant',
      content: '❌ Maaf, terjadi kesalahan saat membuat reservasi. Silakan coba lagi.'
    });
  } finally {
    isLoading.value = false;
  }
};

const useSuggestion = (suggestion: string) => {
  userInput.value = suggestion;
  sendMessage();
};
</script>

<template>
  <div class="min-h-screen bg-gradient-to-br from-primary-50 via-white to-accent-50 py-8">
    <div class="container-custom max-w-5xl">
      <!-- Header -->
      <div class="text-center mb-8 animate-fade-in">
        <div class="inline-flex items-center justify-center w-20 h-20 rounded-full gradient-primary mb-4 animate-float">
          <SparklesIcon class="w-10 h-10 text-primary-50" />
        </div>
        <h1 class="text-4xl md:text-5xl font-display font-bold text-primary-900 mb-3">
          Asisten Reservasi Cerdas
        </h1>
        <p class="text-lg text-primary-700 max-w-2xl mx-auto">
          Powered by AI - Temukan restoran Indonesia terbaik dengan bantuan asisten pintar kami
        </p>
      </div>

      <!-- Chat Container -->
      <div class="card max-w-4xl mx-auto batik-overlay">
        <!-- Chat Messages -->
        <div class="h-[500px] overflow-y-auto mb-6 space-y-4 pr-2">
          <div
            v-for="(message, index) in messages"
            :key="index"
            class="flex animate-slide-up"
            :class="message.role === 'user' ? 'justify-end' : 'justify-start'"
          >
            <div
              class="max-w-[80%] rounded-2xl px-5 py-3 shadow-md"
              :class="
                message.role === 'user'
                  ? 'bg-primary-700 text-primary-50'
                  : 'bg-white border-2 border-primary-200 text-primary-900'
              "
            >
              <div class="flex items-start gap-2 mb-1">
                <ChatBubbleLeftRightIcon
                  v-if="message.role === 'assistant'"
                  class="w-5 h-5 text-primary-600 flex-shrink-0 mt-0.5"
                />
                <div class="flex-1">
                  <p class="text-sm whitespace-pre-line" v-html="message.content.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')"></p>
                </div>
              </div>
            </div>
          </div>

          <!-- Booking Form (Inside Chat) -->
          <div v-if="showBookingForm" class="flex justify-start animate-slide-up">
            <div class="max-w-[90%] bg-white border-2 border-primary-500 rounded-2xl shadow-lg">
              <div class="bg-gradient-to-r from-primary-600 to-primary-700 text-white px-5 py-3 rounded-t-2xl">
                <div class="flex items-center justify-between">
                  <h3 class="text-lg font-display font-bold flex items-center gap-2">
                    📝 Form Reservasi
                  </h3>
                  <button
                    @click="showBookingForm = false"
                    class="text-white hover:text-primary-100 transition-colors text-xl"
                  >
                    ✕
                  </button>
                </div>
              </div>

              <form @submit.prevent="submitBooking" class="p-5 space-y-4">
                <!-- Restaurant Name (Read-only) -->
                <div>
                  <label class="block text-xs font-semibold text-primary-900 mb-1">
                    Restoran
                  </label>
                  <input
                    type="text"
                    v-model="bookingFormData.restaurantName"
                    class="input w-full bg-primary-50 text-sm"
                    readonly
                  />
                </div>

                <div class="grid grid-cols-2 gap-3">
                  <!-- Date -->
                  <div>
                    <label class="block text-xs font-semibold text-primary-900 mb-1">
                      Tanggal <span class="text-red-500">*</span>
                    </label>
                    <input
                      type="date"
                      v-model="bookingFormData.date"
                      class="input w-full text-sm"
                      required
                    />
                  </div>

                  <!-- Time -->
                  <div>
                    <label class="block text-xs font-semibold text-primary-900 mb-1">
                      Waktu <span class="text-red-500">*</span>
                    </label>
                    <input
                      type="time"
                      v-model="bookingFormData.time"
                      class="input w-full text-sm"
                      required
                    />
                  </div>
                </div>

                <!-- Number of Guests -->
                <div>
                  <label class="block text-xs font-semibold text-primary-900 mb-1">
                    Jumlah Tamu <span class="text-red-500">*</span>
                  </label>
                  <input
                    type="number"
                    v-model.number="bookingFormData.guests"
                    min="1"
                    max="20"
                    class="input w-full text-sm"
                    required
                  />
                </div>

                <!-- Customer Name -->
                <div>
                  <label class="block text-xs font-semibold text-primary-900 mb-1">
                    Nama Lengkap <span class="text-red-500">*</span>
                  </label>
                  <input
                    type="text"
                    v-model="bookingFormData.customerName"
                    class="input w-full text-sm"
                    placeholder="Masukkan nama lengkap"
                    required
                  />
                </div>

                <!-- Customer Email -->
                <div>
                  <label class="block text-xs font-semibold text-primary-900 mb-1">
                    Email <span class="text-red-500">*</span>
                  </label>
                  <input
                    type="email"
                    v-model="bookingFormData.customerEmail"
                    class="input w-full text-sm"
                    placeholder="email@example.com"
                    required
                  />
                </div>

                <!-- Customer Phone -->
                <div>
                  <label class="block text-xs font-semibold text-primary-900 mb-1">
                    Nomor Telepon <span class="text-red-500">*</span>
                  </label>
                  <input
                    type="tel"
                    v-model="bookingFormData.customerPhone"
                    class="input w-full text-sm"
                    placeholder="08123456789"
                    required
                  />
                </div>

                <!-- Special Requests -->
                <div>
                  <label class="block text-xs font-semibold text-primary-900 mb-1">
                    Permintaan Khusus (Opsional)
                  </label>
                  <textarea
                    v-model="bookingFormData.specialRequests"
                    class="input w-full text-sm"
                    rows="2"
                    placeholder="Contoh: Meja dekat jendela, high chair untuk anak, dll."
                  ></textarea>
                </div>

                <!-- Submit Button -->
                <div class="flex gap-2 pt-2">
                  <button
                    type="button"
                    @click="showBookingForm = false"
                    class="btn-secondary flex-1 text-sm py-2"
                    :disabled="isLoading"
                  >
                    Batal
                  </button>
                  <button
                    type="submit"
                    class="btn-primary flex-1 text-sm py-2"
                    :disabled="isLoading"
                  >
                    {{ isLoading ? 'Memproses...' : 'Konfirmasi Reservasi' }}
                  </button>
                </div>
              </form>
            </div>
          </div>

          <!-- Loading indicator -->
          <div v-if="isLoading" class="flex justify-start animate-slide-up">
            <div class="bg-white border-2 border-primary-200 rounded-2xl px-5 py-3 shadow-md">
              <div class="flex items-center gap-2">
                <div class="flex gap-1">
                  <div class="w-2 h-2 bg-primary-500 rounded-full animate-bounce" style="animation-delay: 0ms"></div>
                  <div class="w-2 h-2 bg-primary-500 rounded-full animate-bounce" style="animation-delay: 150ms"></div>
                  <div class="w-2 h-2 bg-primary-500 rounded-full animate-bounce" style="animation-delay: 300ms"></div>
                </div>
                <span class="text-sm text-primary-700">AI sedang berpikir...</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Suggestions -->
        <div v-if="messages.length === 1" class="mb-6">
          <p class="text-sm font-semibold text-primary-700 mb-3">Saran Pencarian:</p>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
            <button
              v-for="(suggestion, index) in quickSuggestions"
              :key="index"
              @click="useSuggestion(suggestion)"
              class="text-left px-4 py-3 rounded-lg border-2 border-primary-200 hover:border-primary-500 hover:bg-primary-50 transition-all text-sm text-primary-800 hover:text-primary-900"
            >
              {{ suggestion }}
            </button>
          </div>
        </div>

        <!-- Input Area -->
        <div class="border-t-2 border-primary-100 pt-4">
          <form @submit.prevent="sendMessage" class="flex gap-3">
            <input
              v-model="userInput"
              type="text"
              placeholder="Tanyakan tentang restoran, menu, atau buat reservasi..."
              class="input flex-1"
              :disabled="isLoading"
            />
            <button
              type="submit"
              class="btn-primary px-6"
              :disabled="!userInput.trim() || isLoading"
            >
              <PaperAirplaneIcon class="w-5 h-5" />
            </button>
          </form>
          <p class="text-xs text-primary-600 mt-3 text-center">
            💡 Tip: Sebutkan jenis masakan, lokasi, jumlah tamu, atau waktu yang Anda inginkan
          </p>
        </div>
      </div>


      <!-- Info Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-8">
        <div class="card text-center">
          <div class="text-4xl mb-3">🤖</div>
          <h3 class="font-display font-bold text-primary-900 mb-2">AI Powered</h3>
          <p class="text-sm text-primary-700">Menggunakan teknologi RAG untuk rekomendasi akurat</p>
        </div>
        <div class="card text-center">
          <div class="text-4xl mb-3">🍜</div>
          <h3 class="font-display font-bold text-primary-900 mb-2">Kuliner Nusantara</h3>
          <p class="text-sm text-primary-700">Spesialis restoran masakan Indonesia</p>
        </div>
        <div class="card text-center">
          <div class="text-4xl mb-3">⚡</div>
          <h3 class="font-display font-bold text-primary-900 mb-2">Reservasi Instan</h3>
          <p class="text-sm text-primary-700">Booking langsung melalui chat</p>
        </div>
      </div>

      <!-- Note -->
      <div class="mt-8 text-center">
        <p class="text-sm text-primary-600">
          <strong>Catatan:</strong> Fitur AI ini akan terhubung dengan backend FastAPI menggunakan RAG (Retrieval-Augmented Generation) untuk memberikan rekomendasi restoran yang personal dan akurat.
        </p>
      </div>
    </div>
  </div>
</template>
