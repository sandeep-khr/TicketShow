<template>
  <div class="container mt-2">
    <div class="venue-card">
      <div class="d-flex justify-content-between mb-1" style="border-bottom: 1px dotted black;">
        <h4>{{ theater.name.toUpperCase() }}</h4>
        <p><i class="fas fa-location-dot text-secondary"></i> {{ theater.place }}</p>
        <p mx-2><i class="fas fa-couch text-secondary"></i> {{ theater.capacity }}</p>
        <!-- <p style="font-size: 20px;"><i class="fa-solid fa-file-csv"></i></p> -->
        <p type="button" data-bs-toggle="tooltip" data-bs-placement="top" title="Download Theater Data" @click="exportData(theater.id)">
          <i class="fa-solid fa-file-csv text-primary" style="font-size: 20px;"></i>
        </p>
        <div v-show="edit">
          <div v-show="edit" class="icons d-flex">
            <span @click="showModal('edit')"><i class="fas fa-edit mx-3" style="color: green;"></i></span>
            <span @click="showModal('delete')"><i class="fas fa-trash-alt" style="color: brown;"></i></span>
          </div>
        </div>
      </div>
      <!-- <hr> -->
      <div class="row">
        <ShowCard v-for="show in filteredShows" :key="show.id" :show="show" :edit="edit"></ShowCard>
        <NoShow :theaterId="theater.id"></NoShow>
      </div>
    </div>
    <div v-if="expMsg" class="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>{{ expMsg }}</strong>
      <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    </div>
    <!-- <Modal v-if="modalVisible" :modalMessage="modalMessage" @close-modal="closeModal" @confirm-modal="confirmModal"></Modal> -->
    <div v-if="modalVisible" class="modal">
      <div class="modal-content">
        <span class="close text-secondary" @click="closeModal"><i class="fa-solid fa-xmark"></i></span>
        <form v-if="modalType === 'edit'" @submit.prevent="editTheater">
          <h2>Edit Theater</h2>
          <label for="capacity">Capacity:</label>
          <input type="number" id="capacity" v-model="capacity">
          <label for="location">Location:</label>
          <select v-model="location">
            <option value="patna">Patna</option>
            <option value="delhi">Delhi</option>
            <option value="mumbai">Mumbai</option>
            <option value="chennai">Chennai</option>
          </select>
          <div class="d-flex justify-content-end mt-2"><button type="submit" class="btn btm-sm btn-outline-success">Update</button></div>
        </form>
        <div v-else-if="modalType === 'delete'">
          <h3 class="mt-2">Confirm Delete Theater</h3>
          <p>Are you sure you want to delete this theater?</p>
          <div class="d-flex justify-content-center mt-2"><button @click="deleteTheater" class="btn btn-outline-danger">Delete</button></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ShowCard from './ShowCard.vue';
import NoShow from './NoShow.vue';
import { useAuthStore } from '../stores/index.js';
// import Modal from './Modal.vue';

export default {
  props: {
    theater: {
      type: Object,
      required: true,
    },
    edit: {
      type: Boolean,
      required: false,
    },
  },
  components: {
    ShowCard, NoShow,
  },
  data(){
    return {
      shows: null,
      modalVisible: false,
      modalType: '',
      editMode: this.edit,
      capacity: this.theater.capacity, 
      location: this.theater.place, 
      expMsg: ''
    };
  },
  async mounted(){
    const authStore = useAuthStore();
    try {
      this.shows = await authStore.fetchShows();
    } catch (error) {
      console.error(error);
    }
  },
  computed: {
  filteredShows() {
    if (!this.shows) {
      return [];
    }
    return this.shows.filter(show => this.theater.shows.includes(show.id));
  },

},
methods:{
  showModal(type) {
      this.modalType = type;
      this.modalVisible = true;
    },
    closeModal() {
      this.modalVisible = false;
    },

    async editTheater() {
      const authStore = useAuthStore();
      try {
        this.theater.capacity = this.capacity;
        this.theater.place = this.location;
        let theaterData = {
          "capacity": this.capacity,
          "place": this.location,
        };
        await authStore.updateTheater(this.theater.id, theaterData);
        this.closeModal();
      } catch (error) {
        console.error(error);
      }
    },
    async deleteTheater() {
      const authStore = useAuthStore();
      try {
        await authStore.deleteTheater(this.theater.id);
        window.location.reload();
        // this.$router.push('/');
      } catch (error) {
        console.error(error);
      } finally {
        this.closeModal();
      }
    },
    // async exportData(){
    //   const authStore = useAuthStore();
    //   try {
    //     response = await authStore.export(this.theater.id);
    //     console.log(response);
    //   } catch (error) {
    //     console.error(error);
    //   }
    // },
    exportData(theatreId) {
    fetch(`http://127.0.0.1:8000/export_data/${theatreId}`)
      .then(response => response.json())
      .then(data => {
        console.log(data.message);
        this.expMsg = data.message;
      });
  },
  // async editTheater(){
  //   const authStore = useAuthStore();
  //   try {
  //     await authStore.editTheater(this.theater.id);
  //   } catch (error) {
  //     console.error(error);
  //   }
  // },
  confirmModal(type) {
      if (type === 'edit') {
        this.editTheater();
      } else if (type === 'delete') {
        this.deleteTheater();
      }
    },
  
}  
};
</script>

<style scoped>
input,
  select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    
  }
.venue-card {
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}

.show-cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 10px;
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 9999;
}

.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  max-width: 400px;
}

.close {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  font-size: 20px;
}

</style>