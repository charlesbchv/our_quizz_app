<template>
  <v-container fluid class="d-flex justify-center align-center" style="min-height: 100vh;">
    <v-row justify="center" align="center" class="text-center">
      <slot></slot>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "CenterLayout"
};
</script>
