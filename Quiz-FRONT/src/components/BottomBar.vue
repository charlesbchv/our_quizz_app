<template>
    <v-footer app padless>
      <v-col class="text-center py-3">
        <v-row justify="center">
          <v-col cols="12" md="6" class="text-center">
            <div class="mb-2">
              <strong>Nous suivre</strong>
            </div>
            <v-btn icon href="https://www.facebook.com" target="_blank" rel="noopener noreferrer">
              <v-icon>mdi-facebook</v-icon>
            </v-btn>
            <v-btn icon href="https://www.twitter.com" target="_blank" rel="noopener noreferrer">
              <v-icon>mdi-twitter</v-icon>
            </v-btn>
            <v-btn icon href="https://www.linkedin.com" target="_blank" rel="noopener noreferrer">
              <v-icon>mdi-linkedin</v-icon>
            </v-btn>
            <v-btn icon href="https://www.instagram.com" target="_blank" rel="noopener noreferrer">
              <v-icon>mdi-instagram</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <v-row justify="center">
          <v-col cols="12" class="text-center">
            <div class="mt-2">
              <a href="https://www.esiee.fr" target="_blank" rel="noopener noreferrer">Visitez ESIEE Paris</a>
            </div>
          </v-col>
          <div class="mb-2">
              <strong>&copy; 2024 ESIEE Paris</strong>
          </div>
        </v-row>
      </v-col>
    </v-footer>
  </template>
  
  <script>
  export default {
    name: "BottomBar"
  };
  </script>
  
  <style scoped>
  .v-footer {
    background-color: #333;
    color: #fff;
  }
  a {
    color: #7b42f6;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
  }
  </style>
  