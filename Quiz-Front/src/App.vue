<template>
  <v-theme-provider :theme="theme" with-background>
    <v-layout full-height style="min-height: 100vh">
      <v-app-bar>
        <router-link to="/">
          <v-img src="/logo_modelise.png" :style="theme === 'light' ? 'filter: invert(1)' : undefined" max-height="120" max-width="120"/>
        </router-link>
        <v-spacer></v-spacer>
        <v-btn :to="{ name: 'home' }" class="mr-2">Accueil</v-btn>
        <v-btn :to="{ name: 'settings' }" class="mr-2">Paramètres</v-btn>
        <v-btn :to="{ name: 'admin' }">Admin</v-btn>
      </v-app-bar>
      <v-main>
        <router-view @settings-updated="theme = getTheme()" />
      </v-main>
    </v-layout>
  </v-theme-provider>
</template>

<script>
import settingsStorageService from "@/services/SettingsStorageService";

export default {
  name: "App",
  data() {
    return {
      theme: this.getTheme()
    };
  },
  methods: {
    getTheme() {
      const theme = settingsStorageService.getTheme() ?? "sync";
      if (theme === "sync")
        return matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
      return theme;
    }
  }
};
</script>