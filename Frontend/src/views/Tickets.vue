<template>
    <div>
      <Navigation />
    
      <div class="d-flex justify-content-center">
        <div class="mt-5" style="width: 500px;">
      <!-- <div v-if="errorMsg" class="alert alert-warning alert-dismissible fade show" role="alert">
        {{ errorMsg }}  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="reloadPg"></button>
      </div>
      <div v-if="suscessMsg" class="alert alert-success alert-dismissible fade show" role="alert">
        {{ suscessMsg }}  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="reloadPg"></button>
      </div> -->
          <div
            class="card-horizontal box"
            v-for="booking in sortedBookings"
            :key="booking.id"
          >
            <div class="card-left">
              <img
                src="@/assets/images/ticket.png"
                alt="Ticket Logo"
                class="ticket-logo"
              />
            </div>
            <div class="card-right">
              <div class="row">
                <div class="col-8">
                  <h6 class="card-title mb-1">Booking ID: {{ booking.id }}</h6>
                  <h6 class="card-text">
                    <span style="margin-right: 5px;">#{{ booking.show_id }}</span>
                    {{ booking.movie_name }}
                  </h6>
                </div>
                <!-- <div class="col-4">
                  <button
                    class="p-2"
                    @click="voteShow(booking.show_id, 1)"
                    :disabled="booking.isLiked"
                  >
                    <i class="fa-regular fa-thumbs-up fa-lg"></i>
                  </button>
                  <button
                    class="p-2"
                    @click="voteShow(booking.show_id, -1)"
                    :disabled="booking.isDisliked"
                  >
                    <i class="fa-regular fa-thumbs-down fa-lg"></i>
                  </button>
                </div> -->
              </div>
              <p class="card-text">Booking Date: {{ booking.booking_date }}</p>
              <div class="d-flex justify-content-between">
                <p class="card-text">Quantity: {{ booking.quantity }}</p>
                <p class="card-text" style="margin-right: 50%;">
                  ₹{{ booking.amount }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Navigation from '@/components/Navigation.vue';
  import { useAuthStore } from '@/stores/index';
  
  export default {
    components: { Navigation },
    data() {
      return {
        bookings: [],
        errorMsg: '',
        suscessMsg: '',
      };
    },
    computed: {
      sortedBookings() {
        return this.bookings.slice().sort((a, b) => new Date(b.booking_date) - new Date(a.booking_date));
      },
    },
    methods: {
      async fetchBookings() {
        try {
          const authStore = useAuthStore();
          this.bookings = await authStore.fetchBookings();
        } catch (error) {
          console.error(error);
        }
      },
      async voteShow(showId, rating) {
        const authStore = useAuthStore();
        try {
            await authStore.vote(showId, { rating });
            const booking = this.bookings.find(booking => booking.show_id === showId);
            if (rating === 1) {
            booking.isLiked = true;
            } else if (rating === -1) {
            booking.isDisliked = true;
            }
            this.disableVoteButtons();
            this.suscessMsg = 'Vote Recorded Successfully';
        } catch (error) {
            console.error(error);
            // Handle the error appropriately, e.g., show an error notification to the user.
            this.errorMsg = error;
        }
        },

      disableVoteButtons() {
        setTimeout(() => {
          this.bookings.forEach(booking => {
            booking.isLiked = false;
            booking.isDisliked = false;
          });
        }, 1000);
      },
      reloadPg() {
        window.location.reload();
      }
    },
    mounted() {
      this.fetchBookings();
    },
  };
  </script>
  
  
  
<style scoped>
/* Customize the card appearance */
@keyframes thumbsAnimation {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.2);
    }
    100% {
        transform: scale(1);
    }
}

.fa-thumbs-up.clicked,
.fa-thumbs-down.clicked {
    animation: thumbsAnimation 1s ease; /* Apply the animation to the clicked elements */
}

.card-horizontal {
    display: flex;
    border: 1px solid #ddd;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 10px;
}

.card-left {
    flex: 0 0 60px;
    background-color: #f8f9fa;
    border-radius: 15px 0 0 15px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card-right {
    flex: 1;
    padding: 10px;
}

.card-title {
    font-size: 18px;
    font-weight: bold;
}

.card-text {
    font-size: 14px;
    color: #555;
}

/* Customize the ticket logo appearance */
.ticket-logo {
    width: 100px;
    height: 100px;
    padding: 5px;
    /* border-radius: 50%; */
}

.box {
    background-color: #c5d9f8;
    --mask: conic-gradient(from -135deg at right, #0000, #000 1deg 89deg, #0000 90deg) 50%/100% 30.00px;
    -webkit-mask: var(--mask);
    mask: var(--mask);
}



</style>
  