import Vue from "vue";
import Vuex from "vuex";
import { APP_STORE } from "../store";
import VueRouter from "vue-router";
import App from "./App.vue";

import main_page from "./components/main_page.vue";
import research from "./components/research.vue";

Vue.config.productionTip = false;
Vue.use(VueRouter);
Vue.use(Vuex);

const routes = [
  { path: "/", component: main_page },
  { path: "/research", component: research },
];

const router = new VueRouter({
  mode: "history",
  routes
});

const store = new Vuex.Store(APP_STORE);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
