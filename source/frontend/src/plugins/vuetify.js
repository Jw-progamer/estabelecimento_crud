import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: "mdi",
    primary: "#8bc34a",
    secondary: "#f44336",
    accent: "#607d8b",
    error: "#ff9800",
    warning: "#ffeb3b",
    info: "#00bcd4",
    success: "#03a9f4"
  }
});
