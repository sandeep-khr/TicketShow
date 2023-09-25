<template>
    <div class="m-2">
      <div class="rating">
        <span v-for="star in 5" :key="star" @click="setRating(star)" class="span">
          <i class="fa-solid fa-star"></i>
        </span>
      </div>
      
      <button @click="vote" class="btn btn-sm btn-outline-warning mt-1" style="width: 115px;">
        <span style="font-weight: bold;">Rate {{ this.rating }}⭐</span> 
      </button>
      <p v-if="errMsg" style="color: red;">{{ errMsg }}</p>

    </div>
</template>
  
  
<script>
import { useAuthStore } from '@/stores/index';
export default {
  data() {
    return {
      tempRating: null,
      rating: null,
      errMsg: '',
    };
  },
  methods: {
    setRating(star) {
      this.rating = star;
      this.tempRating = star;
      console.log(this.rating);
    },
    hoverRating(star) {
      this.tempRating = star;
    },
    resetRating() {
      this.tempRating = this.rating;
    },
    async vote() {
      try {
        const authStore = useAuthStore();
        const voteData = {
          rating: this.rating,
        };
        console.log(voteData);

        const response = await authStore.vote(this.showId, voteData);

        // console.log(response.data.message); // Handle success
      } catch (error) {
        console.error(error);
        this.errMsg=error;
      }
    },
  },
  props: {
    showId: Number,
  },
};
</script>

  
  <style scoped>
  .rating {
    display: flex;
  }
  
  .fa-star {
    font-size: 15px;
    padding: 3px;
    cursor: pointer;
    transition: color 0.2s;
    color: rgb(149, 144, 144);
  }
  .fa-star:hover {
    color: gold;
  }
    .fa-star:active {
        color: gold;
    }
    .span:selected{
        background-color: gold;
        color: gold;
    }
        
    
  
  button:active {
    background-color: gold;
    box-shadow: 0 5px goldenrod;
    transform: translateY(4px);
  }
  </style>
  