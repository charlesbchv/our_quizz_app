<template>
  <v-container class="fill-height d-flex justify-center align-center">
    <v-card :class="['login-card', themeClass]" max-width="400">
      <v-card-title class="justify-center">
        <v-img src="/logo_without.png" alt="Logo" class="logo-image"></v-img>
      </v-card-title>
      <v-card-subtitle class="text-center">
        <h2>Bienvenue sur QuizMaster</h2>
        <p>Connectez-vous avec votre mot de passe</p>
      </v-card-subtitle>
      <v-card-text>
        <v-alert v-if="error" class="mb-4" type="error" :title="error" closable @click:close="error = undefined" />
        <v-form @submit="login" ref="form" v-model="valid" lazy-validation>
          <v-text-field 
            label="Mot de passe" 
            type="password" 
            v-model="password" 
            :error="error"
            :rules="passwordRules"
            required 
          />
          <div class="text-center">
            <v-btn type="submit" color="primary" :disabled="!password" class="login-button">Connexion</v-btn>
          </div>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import authenticationService from "@/services/AuthenticationService";

export default {
  name: "Login",
  data() {
    return {
      password: "",
      error: undefined,
      valid: false,
      passwordRules: [
        v => !!v || 'Le mot de passe est requis',
        v => (v && v.length >= 8) || 'Le mot de passe doit contenir au moins 8 caractères'
      ]
    };
  },
  computed: {
    themeClass() {
      return this.$vuetify.theme.dark ? 'dark-theme' : 'light-theme';
    }
  },
  methods: {
    login(e) {
      e.preventDefault();
      if (this.$refs.form.validate()) {
        authenticationService.login(this.password).then(success => {
          if (success) {
            const returnTo = this.$route.params.returnTo;
            this.$router.push(returnTo ?? { name: "admin" });
          } else {
            this.password = "";
            this.error = "Mot de passe invalide";
          }
        });
      } else {
        this.error = "Vous devez spécifier le mot de passe";
      }
    }
  }
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}

.login-card {
  padding: 20px;
}

.logo-image {
  border-radius: 0;
  width: 100px;
  height: 100px;
}

.v-card-title,
.v-card-subtitle {
  margin: 0;
  padding: 0;
}

.v-card-subtitle h2 {
  margin-top: 10px;
  font-size: 24px;
}

.v-card-subtitle p {
  margin-top: 0;
}

.v-btn {
  margin-top: 20px;
  width: 100%;
}

.login-button {
  background-color: #1a73e8;
  color: #fff;
}

.dark-theme {
  background-color: #1e1e1ee9;
  color: #fff;
}

.light-theme {
  background-color: #f5f5f5;
  color: #000;
}

.light-theme .v-card-subtitle h2,
.light-theme .v-card-subtitle p {
  color: #000;
}

.v-card-title.justify-center {
  display: flex;
  justify-content: center;
}
</style>
