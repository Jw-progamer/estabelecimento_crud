<template>
  <v-app>
    <v-app-bar app color="#8bc34a">
      <v-toolbar-title class="headline text-uppercase">
        <span>Estabelecimentos</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text v-if="isLogged" @click="logoff">logoff</v-btn>
    </v-app-bar>
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    //
  }),
  computed: {
    isLogged() {
      const token = localStorage.getItem("token");
      if (token === null) {
        return false;
      }
      return true;
    }
  },
  methods: {
    logoff() {
      localStorage.removeItem("token");
      this.$router.push("/login");
    }
  }
};
</script>
