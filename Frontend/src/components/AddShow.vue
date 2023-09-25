<template>
  <div class="bg-dark">
    <div class="container p-4">
      <div class="row d-flex justify-content-center align-items-center">
        <div class="col">
          <div class="card my-4">
            <div class="row g-0">
              <div class="col-xl-6 d-none d-xl-block">
                <img src="../assets/images/showbg.jpg"
                  style="border-top-left-radius: .25rem; border-bottom-left-radius: .25rem;" />
              </div>
              <div class="col-xl-6">
                <div class="card-body p-md-5 text-black">
                  <h3 class="mb-4 text-uppercase">Add Show <i class="fa-solid fa-film"></i></h3>

                  <div class="form-outline">
                    <input type="text" id="ShowName" class="form-control form-control-md" v-model="name" />
                    <label class="form-label" for="ShowName">Show Name</label>
                  </div>

                  <div class="form-outline">
                    <input type="text" id="YoutubeUrl" class="form-control form-control-md" v-model="youtube" />
                    <label class="form-label" for="YoutubeUrl">Youtube URL</label>
                  </div>

                  <div class="form-outline mb-2">
                    <input type="number" id="ShowPrice" class="form-control form-control-md" v-model="price" />
                    <label class="form-label" for="ShowPrice">Ticket Price</label>
                  </div>

                  <div class="row">
                    <div class="col-md-6 mb-2">

                      <select class="select" v-model="tag">
                        <option value="action">Action</option>
                        <option value="drama">Drama</option>
                        <option value="comedy">Comedy</option>
                      </select>
                      <p class="mx-1">Tag</p>
                    </div>
                    <div class="col-md-6 mb-2">
                      <select class="select" v-model="lang">
                        <option value="english">English</option>
                        <option value="hindi">Hindi</option>
                      </select>
                      <p class="mx-1">Language</p>
                    </div>

                    <p v-if="error" class="alert alert-danger">{{ error }}</p>
                  </div>

                  <!-- <DateTime/> -->
                  <div class="form-outline mb-4">
                    <label class="form-label" for="datetime">Show Date and Time</label>
                    <input type="datetime-local" id="datetime" class="form-control form-control-md" v-model="date"
                      :min="minDate" />
                  </div>

                  <!-- <div class="form-outline mb-3 d-none">
                    <input type="text" id="theaterId" class="form-control form-control-lg" :value="theater_id" readonly/>
                    <label class="form-label" for="theaterId">Theater_id</label>
                  </div> -->

                  <button type="button" class="btn btn-secondary" @click="addShow">Add</button>
                  <router-link to="/admin" class="btn" style="padding-left: 50px; color: blue;">🚶‍♂️Go Back</router-link>

                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
// import DateTime from './DateTime.Vue'
import { useAuthStore } from '../stores';
export default {
  data() {
    return {
      name: "",
      youtube: "",
      price: null,
      theater_id: this.$route.params.id,
      tag: "",
      lang: "",
      date: null,
      error: ''
    }
  },
  computed: {
    minDate() {
      // Get the current date in YYYY-MM-DDTHH:mm format (e.g., "2023-07-29T12:00")
      const now = new Date().toISOString().slice(0, 16);
      return now;
    },
  },
  methods: {
    async addShow() {
      let showData = {
        "name": this.name,
        "tags": this.tag,
        "language": this.lang,
        "ticket_price": this.price,
        "date": this.date,
        "theater_id": this.theater_id,
        "youtube_url": this.youtube,
      };
      try {
        const authStore = useAuthStore();
        await authStore.createShow({
          "name": this.name,
          "tags": this.tag,
          "language": this.lang,
          "ticket_price": this.price,
          "date": this.date,
          "theatre_id": this.theater_id,
          "youtube_url": this.youtube,
        })
        this.$router.push("/admin");
        // setTimeout(() => {
        //   window.location.reload();
        // }, 200);
        console.log(showData)
      } catch (err) {
        console.log(err)
        this.error = err;
      }
    },
    formatDateForAPI(date) {
      const formattedDate = new Date(date);
      const year = formattedDate.getFullYear();
      const month = String(formattedDate.getMonth() + 1).padStart(2, "0");
      const day = String(formattedDate.getDate()).padStart(2, "0");
      const hours = String(formattedDate.getHours()).padStart(2, "0");
      const minutes = String(formattedDate.getMinutes()).padStart(2, "0");

      const formattedDateString = `${year}-${month}-${day} ${hours}:${minutes}`;
      return formattedDateString;
    },

  }
}
</script>
  
<style scoped>
button {
  width: 100px;
}

input,
select {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;

}
</style>