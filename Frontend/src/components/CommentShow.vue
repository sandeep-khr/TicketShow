<!-- CommentShow.vue -->
<template>
    <div class="mt-2">
      <textarea v-model="comment" class="p-2"></textarea>
      <button @click="commentOnShow" class="btn btn-md btn-primary">Comment</button>
      <span v-if="errorMsg" class="text-danger ms-2">{{ errorMsg }}</span>
    </div>

</template>
  
  <script>
  import { useAuthStore } from '@/stores/index';
  export default {
    data() {
      return {
        comment: '',
        errorMsg: ''
      };
    },
    methods: {
      async commentOnShow() {
        try {
          const authStore = useAuthStore();
          const commentData = {
            comment: this.comment
          };
          console.log(commentData);

          const response = await authStore.comment(this.showId, commentData);

        //   console.log(response.data.message); // Handle success
        } catch (error) {
          console.error(error);
          this.errorMsg = error;
        }
      }
    },
    props: {
      showId: Number
    }
  };
  </script>

<style scoped>
textarea {
  width: 100%;
  height: 60px;
  border-radius: 5px;
  border: 1px solid #ccc;
  padding: 10px;
  /* margin-bottom: 10px; */
}    

</style>
  