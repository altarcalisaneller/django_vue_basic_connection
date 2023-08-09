import axios from 'axios'
import VueAxios from 'vue-axios'
import { createApp } from 'vue'
import router from './router' // import our router
import App from './App.vue'


axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"; // This code tells axios to include the CSRF token value with every requestautomatically.
const app = createApp(App); // create our app instance

app.use(router); // tell our app to use our router
app.use(VueAxios, axios); // tell our app to use axios
app.mount("#app") // mount our app on the div#app element in our template 
