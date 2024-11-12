<template>
  <div class="container my-5">
    <h1 class="text-center mb-4">Cipher Tool</h1>

    <!-- Form Enkripsi -->
    <b-card class="mb-4 p-4 shadow-sm" header="Encryption">
      <b-form @submit.prevent="handleEncrypt">
        <b-row>
          <!-- Cipher Selector -->
          <b-col md="6">
            <b-form-group label="Cipher Type" label-for="cipher">
              <b-form-select v-model="cipher" id="cipher" :options="cipherOptions" />
            </b-form-group>
          </b-col>

          <!-- Key Input -->
          <b-col md="6">
            <b-form-group label="Key" label-for="key">
              <b-form-input v-model="key" id="key" type="text" placeholder="Enter cipher key" required />
            </b-form-group>
          </b-col>
        </b-row>

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
        <b-button type="submit" variant="primary" block>Encrypt</b-button>
      </b-form>

      <!-- Hasil Enkripsi -->
      <div v-if="ciphertextResult" class="mt-4">
        <h4>Ciphertext (Base64 Encoded):</h4>
        <b-card class="shadow-sm p-3">
          <pre>{{ ciphertextResult }}</pre>
        </b-card>
      </div>
    </b-card>

    <!-- Form Dekripsi -->
    <b-card class="mb-4 p-4 shadow-sm" header="Decryption">
      <b-form @submit.prevent="handleDecrypt">
        <b-row>
          <!-- Cipher Selector -->
          <b-col md="6">
            <b-form-group label="Cipher Type" label-for="cipherDecrypt">
              <b-form-select v-model="cipherDecrypt" id="cipherDecrypt" :options="cipherOptions" />
            </b-form-group>
          </b-col>

          <!-- Key Input -->
          <b-col md="6">
            <b-form-group label="Key" label-for="keyDecrypt">
              <b-form-input v-model="keyDecrypt" id="keyDecrypt" type="text" placeholder="Enter cipher key" required />
            </b-form-group>
          </b-col>
        </b-row>

        <!-- Ciphertext Input -->
        <b-form-group label="Ciphertext" label-for="ciphertext">
          <b-form-textarea
            v-model="ciphertext"
            id="ciphertext"
            placeholder="Enter ciphertext to decrypt"
            rows="5"
            required
          ></b-form-textarea>
        </b-form-group>

        <!-- Submit Button -->
        <b-button type="submit" variant="danger" block>Decrypt</b-button>
      </b-form>

      <!-- Hasil Dekripsi -->
      <div v-if="plaintextResult" class="mt-4">
        <h4>Plaintext:</h4>
        <b-card class="shadow-sm p-3">
          <pre>{{ plaintextResult }}</pre>
        </b-card>
      </div>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      cipher: 'vigenere',
      cipherDecrypt: 'vigenere',
      key: '',
      keyDecrypt: '',
      plaintext: '',
      ciphertext: '',
      ciphertextResult: '',
      plaintextResult: '',
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
    // Fungsi Enkripsi
    async handleEncrypt() {
      try {
        const response = await axios.post('http://localhost:5000/encrypt', {
          cipher: this.cipher,
          key: this.key,
          plaintext: this.plaintext
        })
        this.ciphertextResult = response.data.ciphertext
      } catch (error) {
        console.error('Error encrypting:', error)
      }
    },

    // Fungsi Dekripsi
    async handleDecrypt() {
      try {
        const response = await axios.post('http://localhost:5000/decrypt', {
          cipher: this.cipherDecrypt,
          key: this.keyDecrypt,
          ciphertext: this.ciphertext
        })
        this.plaintextResult = response.data.plaintext
      } catch (error) {
        console.error('Error decrypting:', error)
      }
    }
  }
}
</script>

<style scoped>
.container {
  max-width: 900px;
}

h1 {
  font-size: 2.5rem;
  color: #343a40;
}

b-card {
  border-radius: 8px;
  background-color: #f8f9fa;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

b-form-group label {
  font-weight: 600;
}

.result-container {
  max-width: 800px;
  margin: 0 auto;
}

pre {
  word-wrap: break-word;
  white-space: pre-wrap;
  background-color: #f1f3f5;
  padding: 1rem;
  border-radius: 5px;
  border: 1px solid #ced4da;
}

b-button {
  font-size: 1.2rem;
  padding: 0.5rem 2rem;
}

.mt-4 {
  margin-top: 2rem;
}

.mb-4 {
  margin-bottom: 2rem;
}

.shadow-sm {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12);
}
</style>
