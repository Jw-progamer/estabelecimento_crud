<template>
  <v-content>
    <ListaEstabelecimento />
    <v-btn absolute dark fab right color="#f44336" :to="'edit/new'">
      <v-icon>mdi-plus</v-icon>
    </v-btn>
  </v-content>
</template>

<script>
import ListaEstabelecimento from "../components/estabelecimentos/ListaEstabelecimento";

export default {
  name: "estabelecimentos",
  components: {
    ListaEstabelecimento
  },
  data() {
    return {};
  }
};
</script>

<style></style>
