<template>
  <div class="home-container">
    <spline-viewer v-if="!isDarkTheme" url="https://prod.spline.design/qIOBKVY7NlrAZFv2/scene.splinecode" class="spline-background"></spline-viewer>
    <div class="content-wrapper">
      <center-layout>
        <div class="content">
          <div class="welcome-section text-center">
            <h1>Bienvenue sur QuizMaster</h1>
            <p>Testez vos connaissances et défiez vos amis avec nos quiz passionnants!</p>
            <v-btn :to="{ name: 'start' }" size="x-large" rounded="xl" color="purple-lighten-1">Participer au quiz</v-btn>
          </div>
          <div class="leaderboard-section">
            <leaderboard />
          </div>
        </div>
      </center-layout>
    </div>
  </div>
</template>

<script>
import CenterLayout from "@/components/CenterLayout.vue";
import Leaderboard from "@/components/Leaderboard.vue";
import settingsStorageService from "@/services/SettingsStorageService";

export default {
  name: "HomePage",
  components: { Leaderboard, CenterLayout },
  data() {
    return {
      theme: settingsStorageService.getTheme() ?? "sync"
    };
  },
  computed: {
    isDarkTheme() {
      if (this.theme === "sync") {
        return matchMedia("(prefers-color-scheme: dark)").matches;
      }
      return this.theme === "dark";
    }
  },
  watch: {
    theme(value) {
      settingsStorageService.setTheme(value);
      this.$emit("settings-updated");
    }
  },
  created() {
    this.theme = settingsStorageService.getTheme() ?? "sync";
  },
  inheritAttrs: false
};
</script>

<style scoped>
.home-container {
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

.content-wrapper {
  position: relative;
  z-index: 2;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.center-layout .content {
  background-color: rgba(255, 255, 255, 0.8); /* Adjust background color and opacity as needed */
  padding: 40px 20px;
  border-radius: 10px; /* Optional: for rounded corners */
}

.welcome-section {
  padding: 40px 20px;
  margin-bottom: 40px;
}

.welcome-section h1 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

.welcome-section p {
  font-size: 1.25em;
  margin-bottom: 30px;
}

.leaderboard-section {
  padding: 20px;
}
</style>
