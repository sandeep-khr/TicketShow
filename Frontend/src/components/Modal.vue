<template>
    <div class="modal">
      <div class="modal-content">
        <p>{{ modalMessage }}</p>
        <button @click="closeModal" class="btn btn-primary btn-sm mb-1">Close</button>
        <button @click="confirmDelete" v-if="modalMessage === 'Confirm Delete Theater'" class="btn btn-danger btn-sm">Delete</button>
        <button @click="confirmEdit" v-if="modalMessage === 'Edit Theater'">Confirm Edit</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ["modalMessage"],
    methods: {
      closeModal() {
        this.$emit("close-modal");
      },
      confirmDelete() {
        this.$emit("confirm-modal", "delete");
      },
      confirmEdit() {
        this.$emit("confirm-modal", "edit");
      },
    },
  };
  </script>
  
<style lang="scss" scoped>
.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 101;
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    background-color: rgba(0, 0, 0, 0.7);

    .modal-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-radius: 8px;
        width: 300px;
        padding: 40px 30px;
        background-color: #fff;

        p {
            text-align: center;
        }

        button {
            align-self: center;
        }
    }
}</style>