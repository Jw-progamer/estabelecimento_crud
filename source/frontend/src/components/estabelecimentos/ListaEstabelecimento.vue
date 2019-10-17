<template>
  <v-content>
    <h4>O raio de alçance atual é de 30, logo os estabelecimentos estão ordenados pela diferença de 30</h4>
    <v-list three-line>
      <template v-for="estabelecimento in estabelecimentos">
        <Estabelecimento :estabelecimento="estabelecimento" :key="estabelecimento['id']" />
      </template>
    </v-list>
  </v-content>
</template>

<script>
import axios from "axios";
import getHeaders from "../../utils";

import Estabelecimento from "./Estabelecimento";

export default {
  name: "ListaEstabelecimentos",
  components: {
    Estabelecimento
  },
  data() {
    return {
      estabelecimentos: [],
      raio: 0
    };
  },
  created() {
    axios
      .get(
        "http://127.0.0.1:8000/api/estabelecimentos/location_close/?raio=30",
        {
          headers: getHeaders()
        }
      )
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
