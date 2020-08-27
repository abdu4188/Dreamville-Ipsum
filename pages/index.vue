<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center logo">
        <logo />
      </div>
      <div class="row avatar-container">
        <div v-for="(artist, index) in artists" :key="index" :class="vWidth < 576 ? 'col-4' : ''">
          <div>
            <v-avatar style="z-index: 2" :size="vWidth < 576 ? 100 : 110" @click="artistClicked(artist)">
              <img :id="selectedArtist == artist.name ? 'overlay' : ''" :src="artist.path" :alt="artist.name">
              <span v-if="selectedArtist == artist.name" class="white--text selected-name">{{ artist.name }}</span>
            </v-avatar>
          </div>
        </div>
      </div>
    </v-flex>
    <div class="text-center select-items row">
      <div class="col-sm-4" style="z-index: 2">
        <v-text-field
          v-model="number"
          type="number"
        />
      </div>
      <div class="col-sm-4">
        <v-select
          v-model="selectedType"
          style="z-index: 2"
          :items="items"
        />
      </div>
      <div class="col-sm-4">
        <v-btn style="z-index: 2" @click="generateLyrics">
          Generate
        </v-btn>
      </div>
    </div>
    <div class="text-center">
      <div v-show="lyricsFetched" style="z-index: 2" class="box">
        <div class="copy-tab" style="z-index: 2" @click="copyText">
          <p class="copy">
            Copy
          </p>
        </div>
        <p> {{ lyrics }} </p>
      </div>
    </div>
    <input id="lyrics-to-be-copied" type="hidden" :value="lyrics">
    <v-snackbar
      v-model="snackbar"
      style="z-index: 2"
      :timeout="2000"
    >
      Copied to clipboard
      <template v-slot:action="{ attrs }">
        <v-btn
          dark
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
    <v-snackbar
      v-model="errorSnackbar"
      style="z-index: 2"
      :timeout="2000"
    >
      Select your artist first
      <template v-slot:action="{ attrs }">
        <v-btn
          dark
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </v-layout>
</template>

<script>
import { required } from 'vuelidate/lib/validators'
import { getLyrics } from '../api/getRandomLyrics'
import Logo from '~/components/Logo.vue'

export default {
  name: 'Home',
  components: {
    Logo
  },
  data () {
    return {
      artists: [
        {
          name: 'Cozz',
          path: 'cozz.jpg'
        },
        {
          name: 'Bas',
          path: 'bas.jpg'
        },
        {
          name: 'Ari Lennox',
          path: 'ari.jpeg'
        },
        {
          name: 'J. Cole',
          path: 'jcole.jpg'
        },
        {
          name: 'JID',
          path: 'jid.jpg'
        },
        {
          name: 'Lute',
          path: 'lute.jpeg'
        },
        {
          name: 'EARTHGANG',
          path: 'earthgang.jpg'
        },
        {
          name: 'Omen',
          path: 'omen.jpg'
        }
      ],
      vWidth: null,
      items: [
        'Paragraphs',
        'Sentences',
        'Words'
      ],
      number: 0,
      selectedType: 'Words',
      lyricsFetched: false,
      lyrics: null,
      selectedArtist: null,
      snackbar: false,
      errorSnackbar: false
    }
  },
  validations: {
    selectedArtist: {
      required
    }
  },
  mounted () {
    this.vWidth = window.innerWidth
  },
  methods: {
    async getLyrics () {
      this.lyricsFetched = true
      this.lyrics = await getLyrics(this.selectedType.toLowerCase(), this.number, this.selectedArtist)
    },
    artistClicked (artist) {
      this.selectedArtist = artist.name
    },
    generateLyrics () {
      this.$v.$touch()
      if (!this.$v.$invalid) {
        this.getLyrics()
      } else {
        this.errorSnackbar = true
      }
    },
    copyText () {
      const lyricsCodeToCopy = document.querySelector('#lyrics-to-be-copied')
      lyricsCodeToCopy.setAttribute('type', 'text')
      lyricsCodeToCopy.select()

      try {
        document.execCommand('copy')
        this.snackbar = true
      } catch (err) {
        alert('Oops, unable to copy')
      }
      lyricsCodeToCopy.setAttribute('type', 'hidden')
      window.getSelection().removeAllRanges()
    }
  }
}
</script>
<style lang="scss" scoped>
input {
  color: white;
}
.v-avatar {
  margin-left: 1vw;
  margin-right: 1vw;
  cursor: pointer;
  display: inline !important;
}
.logo {
  margin-bottom: 4vh;
}
.select-items {
  margin-top: 7vh;
  width: 50vw;
}
.select-items .v-btn {
  margin-top: 3vh;
}
.box {
  margin-left: -3vw;
  width: 45vw;
  height: 30vh;
  max-height: 30vh;
  overflow-y: auto;
  border: #ffffff 1px solid;
  color: #ffffff;
}
.copy-tab {
  width: 5vw;
  height: 5vh;
  background-color: #ffffff;
  color: #0a0a0a;
  cursor: pointer;
}
.copy-tab:active {
  background-color: #0a0a0a;
  color: #ffffff;
}
#overlay {
  position: relative;
  transition: all 0.3s ease;
  opacity: 0.2;
  background-color: #c9c9c9;
}
.selected-name {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  font-size: 1.5rem;
}
</style>
