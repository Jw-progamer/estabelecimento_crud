<template>
  <v-app>
    <v-app-bar app color="#8bc34a">
      <v-toolbar-title class="headline text-uppercase">
        <span>Estabelecimentos</span>
      </v-toolbar-title>
    </v-app-bar>
    <router-view></router-view>
  </v-app>
</template>

<script>

export default {
  name: "App",
  data: () => ({
    //
  })
};
</script>
