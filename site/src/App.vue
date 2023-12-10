<template>
  <div id="app" style="height: 100% !important;">
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.0.13/css/all.css"
      integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp"
      crossorigin="anonymous"
    />
    <router-view></router-view>
    <div style="display:none;" class="scrollup">
      <i class="fa fa-chevron-up"></i>
    </div>
  </div>
</template>

<script>
import "../js/bootstrap.min.js";
import "../js/purecounter.min.js";
import "../js/swiper.min.js";
import "../js/aos.js";
import "../js/script.js";
export default {
  name: "App"
};
</script>

<style>
@import "../css/bootstrap.min.css";
@import "../css/fontawesome-all.min.css";
@import "../css/aos.min.css";
@import "../css/swiper.css";
@import "../css/style.css";
</style>
