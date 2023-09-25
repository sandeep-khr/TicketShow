<template>
    <div class="background-container">
        <div class="container">
        <form @submit.prevent="loginUser">
            <h3 class="text-center p-2 login">Login</h3>
            <!-- Username input -->
            <div class="form-outline mb-4">
                <input v-model="username" type="text" id="username" class="form-control bg-transparent text-white" />
                <label class="form-label" for="username">Username</label>
            </div>

            <!-- Password input -->
            <div class="form-outline mb-4">
                <input v-model="password" type="password" id="password" class="form-control bg-transparent text-white" />
                <label class="form-label" for="password">Password</label>
            </div>

            <!-- Submit button -->
            <button type="submit" class="btn btn-primary btn-block mb-4" style="width: 300px; font-weight: bold; font-size: 20px;">Sign In</button>

            <!-- Display error message if login fails -->
            <div v-if="error" class="alert alert-danger">{{ error }}</div>

            <!-- Register buttons -->
            <div class="text-center">
                <p>Not a member? <router-link to="/signup"><span style="color: rgb(104, 154, 219);">SignUp</span></router-link></p> 
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
    const password = ref('');
    const error = ref(null);

    const loginUser = async () => {
      try {
        await authStore.login({ username: username.value, password: password.value });
        // Redirect the user to the dashboard or home page after successful login
        router.push('/');
      } catch (e) {
        error.value = e.message;   
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

}

form {
    padding: 10px;
    color: beige;
    max-width: 400px;
    margin: 100px auto;
    border-radius: 5px;
    box-shadow: 4px 4px 4px 4px rgba(113, 112, 112, 0.5);

    .btn{
        background: rgb(4,89,166);
        background: linear-gradient(90deg, rgb(71, 116, 157) 40%, rgba(172,6,126,1) 100%);
    }

    .login{
        font-family: 'Lobster', cursive;
        font-size: 50px;
        background: #3304CF;
        background: linear-gradient(to right, #0352da 0%, #ED00B6 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
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