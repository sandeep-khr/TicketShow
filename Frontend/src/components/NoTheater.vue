<template>
    <div class="container mt-2 mb-2">
        <div class="empty-list-card">
      <div class="empty-list-card-content" @click="addVenue">
        <i class="fas fa-plus-circle"></i>
        <p>Add a new theater</p>
      </div>
    </div>
    </div>
</template>

  <script>
  export default {
    methods: {
      addVenue() {
        this.$router.push('/admin/theater/add');
      },
    },
  };
  </script>
  
  <style scoped>
  .empty-list-card {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .empty-list-card-content {
    text-align: center;
    color: #888;
  }
  
  .empty-list-card-content i {
    font-size: 250px;
    margin-bottom: 10px;
  }
  
  .empty-list-card-content p {
    margin: 0;
  }
  </style>
  