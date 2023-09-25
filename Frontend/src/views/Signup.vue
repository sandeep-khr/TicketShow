<template>
    <div class="background-container">
        <div class="container">
            <form @submit.prevent="signupUser" class="formm">
                <h3 class="text-center p-2 signup">Sign Up</h3>
                
            <div class="form-outline mb-3">
                <input v-model="username" type="text" id="username" class="form-control bg-transparent text-white"/>
                <label class="form-label" for="username">Username</label>
            </div>

            <div class="form-outline mb-3">
                <input v-model="email" type="email" id="email" class="form-control bg-transparent text-white" />
                <label class="form-label" for="email">Email</label>
            </div>
            
            <div class="form-outline mb-3">
                <input v-model="password" type="password" id="password" class="form-control bg-transparent text-white" />
                <label class="form-label" for="password">Password</label>
            </div>
            
            <button type="submit" class="btn btn-primary btn-block mb-3" style="width: 300px; font-weight: bold; font-size: 20px;">Sign up</button>
            
            <div v-if="error" class="alert alert-danger">{{ error }}</div>
            
            <div class="text-center">
                <p>Already have an account? <router-link to="/login"><span style="color: rgb(104, 154, 219);">Login</span></router-link></p>
            </div>
        </form>  
    </div>
</div>
</template>

<script setup>
import { defineComponent, ref } from 'vue';
import { useAuthStore } from '../stores/index.js';

    const authStore = useAuthStore();
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const error = ref(null);

    const signupUser = async () => {
      try {
        await authStore.signup({ username: username.value, email: email.value, password: password.value });
        router.push('/login');
      } catch (e) {
        error.value = e.message || 'Failed to sign up';
      }
    };
</script>

<style scoped>
.background-container {
  background-image: url('../assets/images/tubebg.jpg'); /* Replace with the actual path to your image */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh; /* Ensure the background covers the entire viewport */
  /* opacity: 0.5; */
}

.container{
    display: flex;
    justify-content: center;
    border-color: pink;
    font-weight: 400;
    font-size: 20px;

    .formm{
    padding: 10px;
    color: rgb(201, 201, 197);
    max-width: 400px;
    margin: 100px auto;
    border-radius: 5px;
    box-shadow: 4px 4px 4px 4px rgba(113, 112, 112, 0.5);
    

    .btn{
        background: rgb(4,89,166);
        background: linear-gradient(90deg, rgb(71, 116, 157) 40%, rgba(172,6,126,1) 100%);
    }

    .signup{
        font-family: 'Lobster', cursive;
        font-size: 50px;
        background: #3304CF;
        background: linear-gradient(to right, #0352da 0%, #ED00B6 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }
}
}
.background-container::before {
   content : "" ;
   position : absolute ;
   top :0 ;
   left :0 ;
   width :100% ;
   height :100% ;
   z-index :1 ;
   background-color : rgba(0 ,0 ,0 ,0.5) ;
}
.container{
   position : relative ;
   z-index :2 ;
}
</style>