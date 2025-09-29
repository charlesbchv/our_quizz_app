<template>
  <v-theme-provider :theme="theme" with-background>
    <v-layout full-height style="min-height: 100vh">
      <v-app-bar>
          <router-link to="/">
            <v-img src="/logo_without.png" :style="theme === 'light' ? 'filter: invert(1)' : undefined" class="logo" max-height="70" max-width="70"/>
          </router-link>
          <v-spacer></v-spacer>
          <v-btn :to="{ name: 'home' }" class="mr-2">Accueil</v-btn>
          <v-btn :to="{ name: 'settings' }" class="mr-2">Paramètres</v-btn>
          <v-btn :to="{ name: 'aboutUs' }" class="mr-2">Qui sommes-nous</v-btn>
          <v-btn v-if="!isAdminPage || isLoginPage" :to="{ name: 'admin' }">Connexion</v-btn>
          <v-btn v-else @click="logout">Déconnexion</v-btn>
      </v-app-bar>
      <v-main>
        <router-view @settings-updated="theme = getTheme()" :theme="theme" />
      </v-main>
      <bottom-bar />
    </v-layout>
  </v-theme-provider>
</template>

<script>
import settingsStorageService from "@/services/SettingsStorageService";
import authenticationService from "@/services/AuthenticationService";

export default {
  name: "App",
  data() {
    return {
      theme: this.getTheme()
    };
  },
  computed: {
    isAdminPage() {
      return this.$route.path.startsWith('/admin') && !this.isLoginPage;
    },
    isLoginPage() {
      return this.$route.path === '/admin/login';
    }
  },
  methods: {
    getTheme() {
      const theme = settingsStorageService.getTheme() ?? "sync";
      if (theme === "sync")
        return matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
      return theme;
    },
    logout() {
      authenticationService.logout();
      this.$router.push({ name: "home" });
    }
  },
  watch: {
    '$route' (to, from) {
      if (this.isAdminPage) {
        this.$emit('settings-updated');
      }
    }
  }
};
</script>

<style scoped>
.logo {
  margin-left: 20px; /* Adjust the margin value as needed */
}
</style>
