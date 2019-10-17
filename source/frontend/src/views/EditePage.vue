<template>
  <v-container bottom>
    <v-spacer></v-spacer>
    <v-form style="padding: 70px;">
      <label for="nome_estabelecimento"></label>
      <v-text-field
        name="nome_estabelecimento"
        label="nome"
        id="id_nome"
        placeholder="Digite o nome do estabelecimento"
        v-model="estabelecimento.nome"
      ></v-text-field>
      <label for="cnpj_estabelecimento"></label>
      <v-text-field
        name="cnpj_estabelecimento"
        label="cnpj"
        id="id_cnpj"
        placeholder="Digite o cnpj"
        v-model="estabelecimento.cnpj"
      ></v-text-field>
      <label for="endereco_estabelecimento"></label>
      <v-text-field
        name="endereco_estabelecimento"
        label="endereco"
        id="id_endereco"
        placeholder="Digite o endereço do estabelecimento"
        v-model="estabelecimento.endereco"
      ></v-text-field>
      <label for="raio_distancia_estabelecimento"></label>
      <v-text-field
        name="raio_distancia_estabelecimento"
        label="distancia"
        id="id_raio_distancia"
        placeholder="Digite o raio de distância do estabelecimento"
        v-model="estabelecimento.raio_distancia"
      ></v-text-field>
      <v-layout column centered>
        <v-flex xs12 wrap>
          <v-btn
            block
            color="warning"
            @click="deleteDatabase"
            :disabled="estabelecimento_key == 'new'"
            >revomer estabelecimento da lista</v-btn
          >
          <v-spacer></v-spacer>
          <v-btn block color="info" @click="updateDatabase"
            >Adicionar/Atualizar estabelecimento na lista</v-btn
          >
        </v-flex>
      </v-layout>
    </v-form>
  </v-container>
</template>

<script>
import axios from "axios";
import getHeaders from "../utils";

export default {
  name: "formulario",
  props: {
    estabelecimento_key: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      estabelecimento: {
        nome: null,
        cnpj: null,
        endereco: null,
        raio_distancia: null
      }
    };
  },
  created() {
    if (this.estabelecimento_key != "new") {
      axios
        .get(
          "http://localhost:8000/api/estabelecimentos/" +
            this.estabelecimento_key,
          {
            headers: getHeaders()
          }
        )
        .then(response => {
          this.estabelecimento = response.data;
        })
        .catch(response => {
          console.log(response);
        });
    }
  },
  methods: {
    updateDatabase() {
      if (this.estabelecimento_key === "new") {
        axios
          .post(
            "http://localhost:8000/api/estabelecimentos/",
            { ...this.estabelecimento },
            {
              headers: getHeaders()
            }
          )
          .then(response => {
            console.log(response);
            this.$router.push("/");
          })
          .catch(response => {
            console.log(response);
          });
      } else {
        axios
          .put(
            "http://localhost:8000/api/estabelecimentos/" +
              this.estabelecimento_key +
              "/",
            { ...this.estabelecimento },
            {
              headers: getHeaders()
            }
          )
          .then(response => {
            console.log(response);
            this.$router.push("/");
          })
          .catch(response => {
            console.log(response);
          });
      }
    },
    deleteDatabase() {
      axios
        .delete(
          "http://localhost:8000/api/estabelecimentos/" +
            this.estabelecimento_key +
            "/",
          {
            headers: getHeaders()
          }
        )
        .then(response => {
          console.log(response);
          this.$router.push("/");
        })
        .catch(response => {
          console.log(response);
        });
    }
  }
};
</script>

<style></style>
