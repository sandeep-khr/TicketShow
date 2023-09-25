<template>
  <div>
    <RouterView />
  </div>
</template>

<script >
import { RouterLink, RouterView } from 'vue-router'
export default{
  components: {
    RouterLink,
    RouterView,
  }
}
</script>

<style >
.animated-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            background: linear-gradient(45deg, #f6ddc0, #f9bdd3, #8bebfa, #facede);
            background-size: 400% 400%;
            animation: gradientAnimation 15s ease infinite;
        }

        @keyframes gradientAnimation {
            0% {
                background-position: 0% 50%;
            }

            50% {
                background-position: 100% 50%;
            }

            100% {
                background-position: 0% 50%;
            }
        } 
</style>
