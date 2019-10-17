<template>
  <v-content>
    <v-list three-line>
      <template v-for="estabelecimento in estabelecimentos">
        <Estabelecimento
          :estabelecimento="estabelecimento"
          :key="estabelecimento['id']"
        />
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
