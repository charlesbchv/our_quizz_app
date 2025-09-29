<template>
  <div class="settings-page">
    <spline-viewer url="https://prod.spline.design/qIOBKVY7NlrAZFv2/scene.splinecode" class="spline-background"></spline-viewer>
    <center-layout>
      <div class="settings-container">
        <h2>Thème du site</h2>
        <p>Préférence du navigateur : {{ themeDescription }}</p>
        <div class="theme-toggle">
          <v-btn @click="toggleTheme" :class="['theme-button', themeClass]" variant="elevated" rounded="xl" color="primary">
            <v-icon v-if="theme === 'light'">mdi-lightbulb-on-outline</v-icon>
            <v-icon v-else-if="theme === 'sync'">mdi-theme-light-dark</v-icon>
            <v-icon v-else>mdi-weather-night</v-icon>
            <span v-if="theme === 'light'">Clair</span>
            <span v-else-if="theme === 'sync'">Synchronisé</span>
            <span v-else>Sombre</span>
          </v-btn>
        </div>
      </div>
    </center-layout>
  </div>
</template>

<script>
import CenterLayout from "@/components/CenterLayout.vue";
import settingsStorageService from "@/services/SettingsStorageService";

export default {
  name: "ResultPage",
  components: { CenterLayout },
  data() {
    return {
      theme: settingsStorageService.getTheme() ?? "sync"
    };
  },
  computed: {
    preferedColorScheme() {
      return matchMedia("(prefers-color-scheme: dark)").matches ? "Sombre" : "Clair";
    },
    themeClass() {
      return {
        'light-theme': this.theme === 'light',
        'sync-theme': this.theme === 'sync',
        'dark-theme': this.theme === 'dark'
      };
    },
    themeDescription() {
      if (this.theme === 'light') {
        return 'Clair';
      } else if (this.theme === 'sync') {
        return 'Synchronisé';
      } else {
        return 'Sombre';
      }
    }
  },
  methods: {
    toggleTheme() {
      if (this.theme === 'light') {
        this.theme = 'sync';
      } else if (this.theme === 'sync') {
        this.theme = 'dark';
      } else {
        this.theme = 'light';
      }
      settingsStorageService.setTheme(this.theme);
      this.$emit("settings-updated");
    }
  },
  watch: {
    theme(value) {
      settingsStorageService.setTheme(value);
      this.$emit("settings-updated");
    }
  },
  emits: ["settings-updated"]
};
</script>

<style scoped>
.settings-page {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.spline-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
}

.settings-container {
  position: relative;
  z-index: 2;
  text-align: center;
  margin: auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8); /* Adjust the opacity for better readability */
  border-radius: 10px; /* Optional: for rounded corners */
  color: #000; /* Ensure text color stays black */
}

.theme-toggle {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.theme-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 150px;
  height: 50px;
  transition: background-color 0.3s, color 0.3s;
}

.light-theme {
  background-color: #ffffff;
  color: #000000;
}

.sync-theme {
  background-color: #e0e0e0;
  color: #000000;
}

.dark-theme {
  background-color: #333333;
  color: #000000; /* Ensure text color stays black */
}

.theme-button v-icon {
  margin-right: 8px;
}
</style>
