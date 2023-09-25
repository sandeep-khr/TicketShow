<template>
    <div class="mb-2" style="width: 13.9vw; height: 5vh;">
    <div class="empty-list-card">
      <div class="empty-list-card-content" @click="addShow">
        <i class="fas fa-plus-circle"></i>
        <p>Add a new show</p>
      </div>
    </div>
    </div>
  </template> 
  <script>
  export default {
    props: {
    theaterId: {
      type: [String, Number],
      required: true
    }
  },
    methods: {
      addShow() {
        this.$router.push({ path: `/admin/show/add/${this.theaterId}` });
      },
    },
  };
  </script>
  
  <style scoped>
  .empty-list-card {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .empty-list-card-content {
    text-align: center;
    color: #888;
  }
  
  .empty-list-card-content i {
    font-size: 50px;
    margin-bottom: 10px;
  }
  
  .empty-list-card-content p {
    margin: 0;
  }
  </style>
  