<template>
  <center-layout>
    <v-col cols="12">
      <h1>Qui sommes-nous?</h1>
      <p>Nous sommes des étudiants en 2ème année du cycle ingénieur à l'ESIEE Paris.</p>
    </v-col>
    <v-col v-for="student in students" :key="student.name" cols="12" md="4">
      <v-card :class="['student-card', currentTheme]" max-width="400">
        <v-card-title class="d-flex flex-column align-center">
          <v-img :src="student.image" alt="Student Image" class="student-image"></v-img>
          {{ student.name }}
        </v-card-title>
        <v-card-text class="text-center">
          {{ student.description }}
          <div class="social-links">
            <v-btn :href="student.github" target="_blank" icon>
              <v-img src="/src/assets/github.svg" alt="GitHub" class="social-icon"></v-img>
            </v-btn>
            <v-btn :href="student.linkedin" target="_blank" icon>
              <v-img src="/src/assets/linkedin.png" alt="LinkedIn" class="social-icon"></v-img>
            </v-btn>
          </div>
        </v-card-text>
      </v-card>
    </v-col>
  </center-layout>
</template>

<script>
import CenterLayout from "@/components/CenterLayoutAboutUs.vue";
import settingsStorageService from "@/services/SettingsStorageService";

// Import SVG images
import CharlesImage from "@/assets/margelo_faces_szymon.svg";
import YanisImage from "@/assets/margelo_faces_thomas.svg";
import SteeveImage from "@/assets/margelo_faces_christoph.svg";

export default {
  name: "AboutUs",
  components: {
    CenterLayout
  },
  data() {
    return {
      students: [
        { name: "Charles BATCHAEV", description: "Passionné par le développement web et les nouvelles technologies.", image: CharlesImage, github: "https://github.com/charlesbchv", linkedin: "https://www.linkedin.com/in/charles-batchaev/" },
        { name: "Yanis AIT TAOUIT", description: "Intéressé par l'intelligence artificielle et la science des données.", image: YanisImage, github: "https://github.com/y200-anis", linkedin: "https://www.linkedin.com/in/yanis-ait-taouit-511b661ba/" },
        { name: "Steeve Rabehantaa", description: "Enthousiaste à propos de la cybersécurité et des réseaux.", image: SteeveImage, github: "https://github.com/stwrr", linkedin: "https://www.linkedin.com/in/steeve-rabehanta-59049123b/" }
      ]
    };
  },
  computed: {
    currentTheme() {
      return this.$vuetify.theme.dark ? 'dark-theme' : 'light-theme';
    }
  }
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}

.student-card {
  margin: 10px;
  padding: 20px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
}

.student-image {
  width: 150px;
  height: 150px;
  margin-bottom: 10px;
}

.student-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
  background-color: #7b42f6; /* Violet color */
  color: #fff;
}

.student-card.dark-theme {
  background-color: #333;
  color: #fff;
}

.student-card.light-theme {
  background-color: #f5f5f5;
  color: #000;
}

.light-theme .v-card-subtitle h2,
.light-theme .v-card-subtitle p {
  color: #000;
}

.v-card-title {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.social-links {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}

.social-icon {
  width: 24px;
  height: 24px;
}
</style>
