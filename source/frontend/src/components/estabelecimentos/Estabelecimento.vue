<template>
  <v-list-item>
    <v-list-item-content>
      <v-list-item-title>
        <router-link
          :to="{
            path: '/edit/' + estabelecimento['id'],
            params: estabelecimento
          }"
          >{{ estabelecimento.nome }}</router-link
        >
      </v-list-item-title>
      <v-list-item-subtitle>{{ estabelecimento.cnpj }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{
        estabelecimento.endereco
      }}</v-list-item-subtitle>
      <v-list-item-subtitle>{{
        estabelecimento.raio_distancia
      }}</v-list-item-subtitle>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  name: "Estabelecimento",
  props: {
    estabelecimento: {
      type: Object
    }
  }
};
</script>

<style></style>
