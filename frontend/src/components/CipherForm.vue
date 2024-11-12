<template>
  <div class="cipher-form">
    <b-form @submit.prevent="handleSubmit" class="form-group">
      <!-- Cipher Selector -->
      <b-form-group label="Cipher Type" label-for="cipher">
        <b-form-select v-model="cipher" id="cipher" :options="cipherOptions" />
      </b-form-group>

      <!-- Key Input -->
      <b-form-group label="Key" label-for="key">
        <b-form-input v-model="key" id="key" type="text" placeholder="Enter cipher key" required />
      </b-form-group>

      <!-- Plaintext Input -->
      <b-form-group label="Plaintext" label-for="plaintext">
        <b-form-textarea
          v-model="plaintext"
          id="plaintext"
          placeholder="Enter plaintext to encrypt"
          rows="5"
          required
        ></b-form-textarea>
      </b-form-group>

      <!-- Submit Button -->
      <b-button type="submit" variant="primary">Encrypt</b-button>
    </b-form>

    <!-- Ciphertext Display -->
    <div v-if="ciphertext" class="mt-4">
      <h4>Ciphertext (Base64 Encoded):</h4>
      <pre>{{ ciphertext }}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      cipher: 'vigenere',
      key: '',
      plaintext: '',
      ciphertext: '',
      cipherOptions: [
        { value: 'vigenere', text: 'Vigenere Cipher' },
        { value: 'auto_key_vigenere', text: 'Auto-Key Vigenere Cipher' },
        { value: 'extended_vigenere', text: 'Extended Vigenere Cipher' },
        { value: 'playfair', text: 'Playfair Cipher' },
        { value: 'affine', text: 'Affine Cipher' },
        { value: 'hill', text: 'Hill Cipher' },
        { value: 'extended_vigenere_transposition', text: 'Extended Vigenere + Transposition' }
      ]
    }
  },
  methods: {
    async handleSubmit() {
      try {
        const response = await axios.post('http://localhost:5000/encrypt', {
          cipher: this.cipher,
          key: this.key,
          plaintext: this.plaintext
        })
        this.ciphertext = response.data.ciphertext
      } catch (error) {
        console.error('Error encrypting:', error)
      }
    }
  }
}
</script>

<style scoped>
.cipher-form {
  max-width: 600px;
  margin: 0 auto;
}

pre {
  word-wrap: break-word;
  white-space: pre-wrap;
  background-color: #f8f9fa;
  padding: 1rem;
  border-radius: 5px;
  border: 1px solid #ced4da;
}
</style>
