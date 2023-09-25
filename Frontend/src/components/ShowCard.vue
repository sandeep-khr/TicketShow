<template>
  <div class="col-md-2">
    <div class="card mb-2">
      <!-- <a :href="bookingPageUrl"> -->
      <img :src="show.image_url" class="card-img-top" :alt="show.name + ' Poster'">
      <!-- </a> -->
      <div class="card-body">
        <div class="d-flex justify-content-between">
          <div class="text-warning" style="font-weight: 700; font-size: large;">
            <!-- <i class="fa fa-heart mx-1"></i> -->
            <span class="ml-2">{{ show.rating / show.total_rating || 0 }} ⭐</span>
          </div>
          <p class="text-muted">{{ show.total_rating }} Votes</p>
        </div>
        <div class="d-flex justify-content-between">
          <h6 class="card-title">{{ show.name }}</h6>
          <p><i class="fas fa-indian-rupee-sign" style="color: #FFCC33;"></i>{{ show.ticket_price }}</p>
        </div>
        <p class="card-text">
        <div class="d-flex justify-content-between">
          <p>{{ show.language.charAt(0).toUpperCase() + show.language.slice(1) }}</p>
          <p>{{ show.movie_length }}</p>
        </div>
        {{ new Date(show.show_date).toLocaleString('en-GB', {
          day: 'numeric', month: 'long', hour: '2-digit', minute:
            '2-digit'
        }) }}

        </p>
        <div v-show="edit">
          <div class="icons d-flex justify-content-between">
            <!-- <i class="fas fa-edit mx-2" style="color: green;"></i>
            <i class="fas fa-trash-alt" style="color: brown;"></i> -->

            <span @click="showModal('edit')"><i class="fas fa-edit mx-2" style="color: green;"></i></span>
            <span @click="showModal('delete')"><i class="fas fa-trash-alt" style="color: brown;"></i></span>

          </div>
        </div>
      </div>
    </div>


    <!-- <Modal v-if="modalVisible" :modalMessage="modalMessage" @close-modal="closeModal" @confirm-modal="confirmModal"></Modal> -->
    <div v-if="modalVisible" class="modal">
      <div class="modal-content">
        <span class="close text-secondary" @click="closeModal"><i class="fa-solid fa-xmark"></i></span>
        <form v-if="modalType === 'edit'" @submit.prevent="editShow">
          <h2>Edit Show</h2>
          <h1>{{ this.date }}</h1>
          <label for="tprice">Price:</label>
          <input type="number" id="tprice" v-model="price">
          <label for="yt">Youtube:</label>
          <input type="text" id="yt" v-model="youtube">
          <label>Tag:</label>
          <select v-model="tags">
            <option value="drama">Drama</option>
            <option value="action">Action</option>
            <option value="comedy">Comedy</option>
          </select>
          <label>Language:</label>
          <select v-model="lang">
            <option value="english">English</option>
            <option value="hindi">Hindi</option>
          </select>
          <!-- <DateTime/> -->
          <div class="form-outline mb-4">
            <label class="form-label" for="datetime">Show Date and Time</label>
            <input type="datetime-local" id="datetime" class="form-control form-control-md" v-model="date"
              :min="minDate" />
          </div>
          <div class="d-flex justify-content-end mt-2"><button type="submit"
              class="btn btm-sm btn-outline-success">Update</button></div>
        </form>
        <div v-else-if="modalType === 'delete'">
          <h3 class="mt-2">Confirm Delete Theater</h3>
          <p>Are you sure you want to delete this theater?</p>
          <div class="d-flex justify-content-center mt-2"><button @click="deleteShow"
              class="btn btn-outline-danger">Delete</button></div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { useAuthStore } from '../stores/index.js';
export default {
  props: {
    show: {
      type: Object,
      required: true
    },
    edit: {
      type: Boolean,
      required: false
    }
  },
  data() {
    return {
      modalVisible: false,
      modalType: '',
      price: this.show.ticket_price,
      tags: this.show.tags,
      lang: this.show.language,
      modalMessage: '',
      youtube: this.show.youtube,
      date: this.show.show_date,

    }
  },
  methods: {
    showModal(type) {
      this.modalType = type;
      this.modalVisible = true;
    },
    closeModal() {
      this.modalVisible = false;
    },

    async editShow() {
      const authStore = useAuthStore();
      try {
        // Update theater properties based on form inputs
        let showData = {
          "ticket_price": this.price,
          "tags": this.tags,
          "language": this.lang,
          "youtube_url": this.youtube,
          "show_date": new Date(this.date).toISOString().slice(0, 16)
        };

        await authStore.updateShow(this.show.id, showData);
        console.log(showData);
        this.closeModal();
        setTimeout(() => {
          window.location.reload();
        }, 100);
      } catch (error) {
        console.error(error);
        // Handle the error, e.g., show an error message to the user.
      }
    },
    async deleteShow() {
      const authStore = useAuthStore();
      try {
        await authStore.deleteShow(this.show.id);
        window.location.reload();
        // this.$router.push('/');
      } catch (error) {
        console.error(error);
        // Handle the error, e.g., show an error message to the user.
      } finally {
        this.closeModal();
      }
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
        this.editShow();
      } else if (type === 'delete') {
        this.deleteShow();
      }
    },

  },
  computed: {
    minDate() {
      // Get the current date in YYYY-MM-DDTHH:mm format (e.g., "2023-07-29T12:00")
      const now = new Date().toISOString().slice(0, 16);
      return now;
    },
  }
};
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: 0.5s ease all;

  &:hover {
    transform: rotateZ(-1deg) scale(1.01);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
      0 2px 4px -1px rgba(0, 0, 0, 0.06);
  }

}

input,
select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;

}

.card-img-top {
  height: 30vh;
  object-fit: cover;
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
