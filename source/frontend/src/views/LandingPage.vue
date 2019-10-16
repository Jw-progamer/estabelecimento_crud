<template>
  <v-content fluid>
    <v-form>
      <v-text-field name="username" label="Usuario" id="username" v-model="username"></v-text-field>
      <v-text-field name="password" label="Senha" id="password" type="password" v-model="password"> </v-text-field>
      <v-col>
        <v-row justify-center justify="center">
          <v-btn color="primary" centered @click="onLogin()">Realizar Login</v-btn>
        </v-row>
      </v-col>
    </v-form>
  </v-content>
</template>

<script>
import axios from "axios"

export default {
  name: "LandingPage",
  data () {
    return{
      username:"",
      password:""
    }
  },
  methods:{
    onLogin(){
      console.log("chego aqui")
      axios.post("http://localhost:8000/api/token/",{
        username: this.username,
        password: this.password
      })
      .then( response => {
        console.log(response.data)
        localStorage.setItem("token",response.data.access)
      }).catch( response => {
        console.log("Caio no cath")
        console.log(response)
      })
    }
  }
};
</script>

<style></style>
