import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";

import main_page from "./components/main_page.vue";
Vue.use(VueRouter);

const routes = [{ path: "/", component: main_page }, s];

const router = new VueRouter({
  mode: "history",
  routes // сокращённая запись для `routes: routes`
});

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
