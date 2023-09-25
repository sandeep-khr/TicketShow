<template>
    <div class="container my-1">
      <div
        id="myCarousel"
        class="carousel slide mx-auto my-2"
        data-bs-ride="carousel"
        data-bs-interval="5000"
        
      >
        <!-- <ol class="carousel-indicators">
          <li data-bs-target="#myCarousel" data-bs-slide-to="0" class="active"></li>
          <li data-bs-target="#myCarousel" data-bs-slide-to="1"></li>
          <li data-bs-target="#myCarousel" data-bs-slide-to="2"></li>
        </ol> -->
        <!-- src="../assets/images/avng1.jpeg" -->
        <div class="carousel-inner" >
          <div class="carousel-item active">
            <router-link to="/show/7">
              <img
                class="d-block w-100"
                src="../assets/images/Untitled.png"
                alt="Image 1"
              />
            </router-link>
          </div>
          <div class="carousel-item">
            <router-link to="/show/4">
              <img
                class="d-block w-100"
                src="../assets/images/hobbit-l.jpg"
                alt="Image 2"
              />
            </router-link>
          </div>
          <div class="carousel-item">
            <router-link to="/show/6">
              <img
                class="d-block w-100"
                src="https://www.thebatman.com/images/banner_img.jpg"
                alt="Image 3"
              />
            </router-link>
          </div>
        </div>
  
        <a
          class="carousel-control-prev"
          href="#myCarousel"
          role="button"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </a>
        <a
          class="carousel-control-next"
          href="#myCarousel"
          role="button"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </a>
        
      </div>
    </div>
  </template>
  
  <script>
  export default {
    // mounted() {
    //   // Initialize the Bootstrap carousel when the component is mounted
    //   this.initCarousel();
    // },
    // methods: {
    //   initCarousel() {
    //     // Manually create the carousel instance
    //     new bootstrap.Carousel(document.getElementById('myCarousel'), {
    //       interval: 5000,
    //     });
    //   },
    // },
  };
  </script>
  
  <style scoped>
  .carousel-item img {
    /* object-fit: cover; */
    border-radius: 15px;
    height: 30vh; /* Adjust the height as per your requirement */
    
  }
  </style>
  