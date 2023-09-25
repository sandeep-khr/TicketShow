<template>
  <div class="bgi">
    <div class="container p-4">
      <div class="row d-flex justify-content-center align-items-center ">
        <div class="col">
          <div class="card my-4">
            <div class="row g-0">
              <div class="col-xl-6 d-none d-xl-block">
                <img src="../assets/images/thtbg.jpeg"
                  alt="Sample photo" class="img-fluid"
                  style="border-top-left-radius: .25rem; border-bottom-left-radius: .25rem;" />
              </div>
              <div class="col-xl-6">
                <div class="card-body p-md-5 text-black">
                  <h3 class="mb-4 text-uppercase">Add Theater <i class="fa-solid fa-couch"></i></h3>
  
                  <div class="form-outline">
                        <input type="text" id="name" class="form-control form-control-lg" v-model="name"/>
                        <label class="form-label" for="name">Theater Name</label>
                  </div>
  
                  
  
                  <div class="form-outline mb-4">
                    <input type="number" id="capacity" class="form-control form-control-lg" v-model="capacity"/>
                    <label class="form-label" for="capacity">Capacity</label>
                  </div>
  
  
                  <div class="row">
                    <div class="col-md-6 mb-4">
  
                      <select class="select" v-model="loc">
                        <option value="patna">Patna</option>
                        <option value="delhi">Delhi</option>
                        <option value="mumbai">Mumbai</option>
                        <option value="chennai">Chennai</option>
                      </select>
                      <p>Location</p>
                      <p v-if="error" class="alert alert-danger" >{{ error }}</p>
                    </div>

                  <!-- <div v-if="error" class="alert alert-warning alert-dismissible fade show" role="alert">
                    <strong>{{ error }}</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                  </div> -->

                </div>                  
                    <button type="button" class="btn btn-primary" @click="addTheater">Add</button>
                </div>
                <router-link to="/admin" class="btn" style="padding-left: 50px; color: blue;">🚶‍♂️Go Back</router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </template>
  
  <script>
  import { useAuthStore } from '../stores'
      export default {
        data(){
          return{
            name:"",
            capacity:"",
            loc:null,
            error:""
          }
        },
        methods:{
          async addTheater(){
            let theaterData = {
              "name":this.name,
              "place":this.loc,
              "capacity":this.capacity,
            }
            const authStore = useAuthStore();
            try{
              await authStore.createTheater(theaterData)
              this.$router.push({name:"Admin"})
            }catch(err){
              console.log(err)
              this.error = err.message
            }
          }
        }
          
      }
  </script>
  
  <style scoped>
  .bgi {
  background-image: linear-gradient(to bottom right, lightblue, rgba(255, 255, 255, 0.5));
}

input,
  select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }

  button{
    width: 100px;
  }
  
  </style>
  
<!-- <style scoped>


.page-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh; /* Ensures the container takes the full viewport height */
}

.background-image {
    background-image: url('../assets/images/theaterbg.jpg');
    width: 100%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
    z-index: -1;
    opacity: 0.4; 
    
  }

  .container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    /* background-color: #f7f7f7; */
    border-radius: 10px;
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    text-align: center;
    color: #333;
    margin-bottom: 20px;
  }
  
  .form-container {
    display: flex;
    flex-direction: column;

  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    font-weight: bold;
  }
  
  input,
  select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style> -->
  