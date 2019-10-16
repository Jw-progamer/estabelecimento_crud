<template>
  <v-content>
    <div v-for="estabelecimento in estabelecimentos" :key="estabelecimento.id">
      <h1>{{ estabelecimento.nome }}</h1>
      <h2>{{ estabelecimento.cnpj }}</h2>
      <h6>{{ estabelecimento.raio_distancia }}</h6>
    </div>
  </v-content>
</template>

<script>
import axios from "axios";
import getHeaders from "../utils";

export default {
  name: "estabelecimentos",
  data() {
    return {
      estabelecimentos: []
    };
  },
  created() {
    axios
      .get("http://localhost:8000/api/estabelecimentos", {
        headers: getHeaders()
      })
      .then(response => {
        this.estabelecimentos = response.data;
      })
      .catch(response => {
        console.log(response);
      });
  }
};
</script>

<style></style>
