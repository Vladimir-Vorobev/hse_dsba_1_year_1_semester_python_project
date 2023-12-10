<template>
    <div>
      <!-- Navigation -->
      <nav
        id=""
        class="navbar navbar-expand-lg fixed-top navbar-dark top-nav-collapse"
        aria-label="Main navigation"
      >
        <div class="container">
          <!-- Image Logo -->
          <!-- <a class="navbar-brand logo-image" href="index.html"><img src="images/logo.svg" alt="alternative"></a> -->
  
          <!-- Text Logo - Use this if you don't have a graphic logo -->
  
          <button
            class="navbar-toggler p-0 border-0"
            type="button"
            id="navbarSideCollapse"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
  
          <div
            class="navbar-collapse offcanvas-collapse"
            id="navbarsExampleDefault"
          >
            <ul class="navbar-nav ms-auto navbar-nav-scroll">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#header"
                  >Home</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/research">Research</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#find-job">Find job</a>
              </li>
              <!-- <li class="nav-item">
                          <router-link class="nav-link" to="/qa-search">QA-search</router-link>
                      </li> -->
            </ul>
          </div>
          <!-- end of navbar-collapse -->
        </div>
        <!-- end of container -->
      </nav>
      <!-- end of navbar -->
      <!-- end of navigation -->
  
      <div class="research-html" v-html="HTMLResearch"></div>
  
      <!-- Bottom -->
      <div class="bottom py-2 text-light">
        <div class="container d-flex justify-content-between">
          <div>
            <p>Copyright © Vladimir Vorobev, 2023</p>
            <br />
          </div>
        </div>
        <!-- end of container -->
      </div>
      <!-- end of bottom -->
  
      <!-- Back To Top Button -->
      <button @click="topFunction()" id="myBtn">
        <img src="../assets/images/up-arrow.png" alt="alternative" />
      </button>
      <!-- end of back to top button -->
    </div>
  </template>
  
  <script>
  import HTMLResearch from "vue-html-loader!../research.html"
  export default {
    name: "Research",
    data() {
      return {
        HTMLResearch: HTMLResearch
      };
    },
    methods: {
      topFunction() {
        document.body.scrollTop = 0; // for Safari
        document.documentElement.scrollTop = 0; // for Chrome, Firefox, IE and Opera
      }
    }
  };
  </script>
  
  <style scoped>
  div ::-webkit-scrollbar-thumb {
    background-color: red;
  }
  
  .research-html {
    margin-top: 50px;
  }
  </style>
  