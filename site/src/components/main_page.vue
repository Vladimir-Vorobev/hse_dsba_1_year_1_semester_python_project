<template>
  <div>
    <!-- Navigation -->
    <nav
      id="navbar"
      class="navbar navbar-expand-lg fixed-top navbar-dark"
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
              <a class="nav-link active" aria-current="page" href="#home"
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

    <!-- Home -->
    <section class="home py-5 d-flex align-items-center" id="home">
      <div class="container text-light py-5" data-aos="fade-right">
        <h1 class="headline">
          HSE DSBA <span class="home_text">LA</span><br />City Payroll Data<br>
          Python Project
        </h1>
        <p class="para para-light py-3">
          This site was developed by Vladimir Vorobev specially for HSE
          DSBA 1st year 1st semester Python project. It contains a research and 
          can show you a detailed information about state jobs in LA from 2013 to 2016.
        </p>
        <div class="my-3">
          <a class="btn" href="#search">Try it</a>
        </div>
      </div>
      <!-- end of container -->
    </section>
    <!-- end of home -->

    <!-- Information -->
    <section class="information">
      <div class="container-fluid">
        <div class="row text-light">
          <div class="col-lg-4 text-center p-5" data-aos="zoom-in">
            <i class="fas fa-tachometer-alt fa-3x p-2"></i>
            <h4 class="py-3">Instantly find an information about the job</h4>
          </div>
          <div class="col-lg-4 text-center p-5" data-aos="zoom-in">
            <i class="fas fa-wifi fa-3x p-2"></i>
            <h4 class="py-3">
              The search is conducted through the database of 1549 unique job positions in 58 departments
            </h4>
          </div>
          <div class="col-lg-4 text-center p-5 text-dark" data-aos="zoom-in">
            <i class="fas fa-headset fa-3x p-2"></i>
            <h4 class="py-3">Official job descriptions are provided</h4>
          </div>
        </div>
      </div>
      <!-- end of container -->
    </section>
    <!-- end of information -->

    <!-- Search line -->
    <section class="contact d-flex align-items-center py-5" id="find-job">
      <div class="container-fluid text-light">
        <div class="row">
          <div
            class="col-lg-10 d-flex justify-content-center align-items-center px-lg-9"
            data-aos="fade-right"
          >
            <div style="width: 90%">
              <div class="text-center text-lg-start py-4 pt-lg-0">
                <p>SEARCH LINE</p>
                <h2 class="py-2">Choose a Department from the list</h2>
                <!-- <p class="para-light">
                  The system will answer in a few seconds
                </p> -->
              </div>

              <select
                style="display:inline; position:relative; padding-right: 30px; padding-top: 0px; padding-bottom: 0px; margin-bottom: 10px;"
                class="form-control form-control-input"
                id="select_department"
                @change="find_jobs_by_department()"
              >
                <option disabled selected>Select department</option>
                <option v-for="item in departments" :key="item">{{ item }}</option>
              </select>

              <select
                  style="display:inline; position:relative; padding-right: 30px; padding-top: 0px; padding-bottom: 0px; margin-bottom: 10px;"
                  class="form-control form-control-input"
                  id="select_job"
                  @change="find_job_description()"
                >
                  <option disabled selected>Select job position</option>
                  <option v-for="item in jobs" :key="item">{{ item }}</option>
                </select>
                
                <embed type="application/pdf" :src="job_description_link" />
            </div>
            <!-- end of div -->
          </div>
        </div>
        <!-- end of row -->
      </div>
      <!-- end of container -->
    </section>
    <!-- end of search line -->

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
import Swal from "sweetalert2";
import pdf from 'vue-pdf';
export default {
  name: "MainPage",
  data() {
    return {
      departments: [],
      jobs: [],
      job_description_file: null
    };
  },
  beforeMount(){
      fetch(this.$store.state.server_ip + "/get_departments", {
        method: "GET",
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(response => {
        return response.json();
      })
      .then(body => {
        if (body.answer.departments.length == 0) {
          Swal.fire({
            title: "Failed to fetch!",
            icon: "error"
          });
        }
        else {
          this.departments = body.answer.departments
        }
      })
      .catch(error => {
        Swal.fire({
          title: "Error",
          text: error,
          icon: "error"
        });
      });
  },
  methods: {
    find_jobs_by_department() {
      let department = document.getElementById("select_department").value
      fetch(this.$store.state.server_ip + "/find_jobs_by_department", {
        method: "POST",
        body: JSON.stringify({ department: department }),
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(response => {
        return response.json();
      })
      .then(body => {
        this.jobs = body.answer.jobs
      })
      .catch(error => {
        Swal.fire({
          title: "Error",
          text: error,
          icon: "error"
        });
      });
    },
    find_job_description() {
      let job = document.getElementById("select_job").value
      fetch(this.$store.state.server_ip + "/find_job_description/" + job, {
        method: "GET",
        headers: {
          "Content-Type": "application/pdf"
        }
      })
      .then(response => {
        return response.json();
      })
      .then(body => {
        console.log(body)
        this.job_description_file = body.answer.description_file
      })
      .catch(error => {
        Swal.fire({
          title: "Error",
          text: error,
          icon: "error"
        });
      });
    },
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

option {
  margin: 100px;
}
</style>
