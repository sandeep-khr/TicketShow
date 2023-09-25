<template>
    <div class="container">
        <div class="" v-if="show">
            <Navigation></Navigation>
            <!-- <h1>{{ this.id }}</h1> -->
        </div>
        <div class="container mt-1" v-if="show && theater">
            <div class="row">
                <div class="col-md-3">
                    <!-- Movie Poster -->
                    <div class="card mb-3">
                        <div class="top-left p-1" style="border-radius: 0 0 0 0;">
                            <h6 class="text-warning" style="font-size: large; font-weight: 700;">{{ show.rating / show.total_rating || 0 }} ⭐</h6>
                            <span class="text-secondary">{{ show.total_rating }} votes</span>
                        </div>
                        <img :src="show.image_url" alt="Movie Poster" class="card-img-top">
                        <div class="card-body">
                            <h5 class="card-title">{{ show.name }}</h5>
                            <p class="card-text"><strong>Director: </strong>{{ show.director }}</p>
                            <p class="card-text"><strong>Writer: </strong> {{ show.writer }}</p>
                            <p class="card-text"><strong>Cast: </strong>{{ show.cast }}</p>
                        </div>
                    </div>
                    <hr>
                    <div>
                        <label for="quant">Ticket Quantity <i class="fa-solid fa-ticket"
                                style="color: #79c9ec;"></i></label>
                        <input class="w-100 p-1 my-1" type="number" id="quant" min="1" :max="theater.capacity"
                            v-model="quantity">
                        <p v-if="capMsg" class="text-warning">{{ capMsg }}</p>
                    </div>

                    <div v-if="theater.capacity > 0 && (new Date(show.show_date).toISOString().slice(0, 16) > currentDate)">
                        <button type="button" class="w-100 btn btnn btn-sm" data-bs-toggle="modal"
                            data-bs-target="#ticketModal">Book Now</button>
                    </div>
                    <div v-else-if="(new Date(show.show_date).toISOString().slice(0, 16) < currentDate)">
                        <p class="w-100 btn btn-sm btn-danger" style="cursor: not-allowed;">Show Expired</p>
                    </div>
                    <div v-else>
                        <p class="w-100 btn btn-sm btn-danger" style="cursor: not-allowed;">Houseful</p>
                    </div>
                    <!-- <h1>{{ (new Date(show.show_date).toISOString().slice(0, 16) < currentDate) }}</h1> -->
                    <!-- <p v-if="quantity > 20" class="text-danger">Quantity must be between 1 and 20.</p> -->

                </div>
                <div class="col-md-9">
                    <!-- Trailer Videos -->
                    <div class="mb-4">
                        <div class="embed-responsive embed-responsive-16by9 rounded">
                            <iframe :src="videoUrl(show.youtube)" title="YouTube video player" frameborder="0"
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                                allowfullscreen></iframe>
                        </div>
                    </div>

                    <!-- Movie Details -->
                    <div class="mb-4">
                        <h4>{{ show.name }}</h4>
                        <p>{{ show.movie_description }}</p>
                    </div>



                    <ul class="nav nav-tabs" id="myTab" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active" id="details" data-bs-toggle="tab" data-bs-target="#home" type="button" role="tab" aria-controls="home" aria-selected="true">Show Details</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link" id="review" data-bs-toggle="tab" data-bs-target="#profile" type="button" role="tab" aria-controls="profile" aria-selected="false">Rate & Review</button>
                    </li>
                    </ul>

                    <div class="tab-content" id="myTabContent">
                    <div class="tab-pane fade show active p-4" id="home" role="tabpanel" aria-labelledby="details">
                        <div class="">
                        <!-- <h4>Show Details</h4> -->
                        <div class="row">
                            <div class="col-md-6 mb-1">
                                <p><strong>Location:</strong> {{ show.location.charAt(0).toUpperCase() +
                                    show.location.slice(1) }}</p>
                                <p><strong>Theater:</strong> {{ theater.name }}</p>
                                <p><strong>Timing:</strong> {{ show.show_date }}</p>
                            </div>
                            <div class="col-md-6 mb-1">
                                <p><strong>Available Seats:</strong> {{ theater.capacity }}</p>
                                <p><strong>Price:</strong> ₹{{ show.ticket_price }}</p>
                            </div>
                            <!-- <div class="col-md-12">
                                <hr>
                            </div> -->
                        </div>
                    </div>


                    </div>
                    <div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="review">
                        <div class="row">
                            <div class="col-4">
                                <VoteShow :show-id="this.show.id"></VoteShow>
                            </div>
                            <div class="col-8">
                                <CommentShow :show-id="this.show.id"></CommentShow>
                            </div>
                        </div>
                        <div v-for="comment in show.comments_data" class="comment" style="margin-left: 34%;">
                            <div class="d-flex">
                                <div class="profile-icon" v-text="initials(comment.c_username)"></div>
                                <p class="text-secondary ms-2">@{{ comment.c_username }}</p>
                                <p class="ms-5 text-secondary">{{ comment.commented_at }}</p>
                            </div>
                            <p style="font-size: larger;" class="ms-5">{{ comment.comment }}</p>
                        </div>
                    </div>
                    <hr>
                    </div>


                    <!-- Location, Theater, Capacity, Available Seat, Price, Quantity -->
                    <!-- <div class="mb-4">
                        <h4>Show Details</h4>
                        <div class="row">
                            <div class="col-md-6 mb-1">
                                <p><strong>Location:</strong> {{ show.location.charAt(0).toUpperCase() +
                                    show.location.slice(1) }}</p>
                                <p><strong>Theater:</strong> {{ theater.name }}</p>
                                <p><strong>Timing:</strong> {{ show.show_date }}</p>
                            </div>
                            <div class="col-md-6 mb-1">
                                <p><strong>Available Seats:</strong> {{ theater.capacity }}</p>
                                <p><strong>Price:</strong> ₹{{ show.ticket_price }}</p>
                            </div>
                            <div class="col-md-12">
                                <hr>
                            </div>
                        </div>
                    </div> -->
                </div>
            </div>
            <!-- Modal Confirmation Dialog -->


            <div class="modal fade" id="ticketModal" tabindex="-1" aria-labelledby="ticketModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content booking-modal">
                        <div class="modal-header" style="background-color: #79c9ec;">
                            <h3 class="modal-title" id="ticketModalLabel">Confirm your booking</h3>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <div class="show-details">
                                <h3 class="show-name">{{ this.show.name }}</h3>
                                <p class="show-time">🕒 Show Time: {{ this.show.show_date }}
                                    <span class="mx-2"><i class="fa fa-location-dot"></i>
                                        {{ this.show.location.toUpperCase() }}</span>
                                </p>
                            </div>
                            <div class="booking-summary">
                                <p class="quantity-label">Number of Tickets:</p>
                                <p class="selected-quantity">🎫 {{ quantity }}</p>
                            </div>
                        </div>
                        <div class="modal-footer justify-content-between mb-5" style="background-color: #d1f2f6;">
                            <p class="total-amount " style="font-size: 25px;"> Total: <span style="color: gold;">₹</span> {{
                                show.ticket_price * quantity }}</p>
                            <div>
                                <button type="button" class="btn btn-secondary mx-1" data-bs-dismiss="modal">Not
                                    Today</button>
                                <button type="button" class="btn btn-success" @click="book" data-bs-dismiss="modal">Book Now</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


        </div>
    </div>
</template>

<script>
import NavigationVue from '../components/Navigation.vue';
import router from '../router';
import VoteShow from '../components/VoteShow.vue';
import CommentShow from '../components/CommentShow.vue';
import { useAuthStore } from '../stores/index.js';
export default {
    components: {
        Navigation: NavigationVue,
        VoteShow,
        CommentShow
    },
    data() {
        return {
            id: this.$route.params.id,
            show: null,
            theater: null,
            quantity: 1,
            currentDate: new Date().toISOString().slice(0, 16),
            capMsg: null
        }
    },
    watch: {
        quantity: function (val) {
            if (val > this.theater.capacity) {
                this.quantity = this.theater.capacity;
                this.capMsg = `Only ${this.theater.capacity} tickets available.`
            }
        }
    },
    async beforeMount() {
        const authStore = useAuthStore();
        try {
            this.show = await authStore.fetchShowById(this.id);
            this.theater = await authStore.fetchTheaterById(this.show.theatre_id);

        } catch (error) {
            console.error(error);
        }

    },
    methods: {
        videoUrl(id) {
            return `https://www.youtube.com/embed/${id}`;
        },
        book() {
            const authStore = useAuthStore();
            authStore.bookTicket({ "show_id": this.show.id, "quantity": this.quantity });
            router.push('/bookings');
            setTimeout(() => {
                window.location.reload();
            }, 100);
            window.location.reload();
        },
        initials(name) {
            return name.split(' ').map(n => n[0]).join('');
        }

    }
}
</script>

<style scoped>
.heart-icon {
    color: red;
}

.card-img-top {
    object-fit: cover;
    height: 40vh;
}

.top-left {
    position: absolute;
    top: 0px;
    left: 0px;
    background-color: whitesmoke;
    padding: 1px;
}

.embed-responsive iframe {
    width: 100%;
    height: 455px;
    border-radius: 15px;
}

.btnn {
    background-color: rgb(127, 234, 255);
    font-weight: bold;

    &:hover {
        background-color: rgb(6, 202, 241);
    }
}

.booking-modal {
    background-color: #a6ecf4;
    --mask: conic-gradient(from -45deg at bottom, #0000, #000 1deg 90deg, #0000 91deg) 50% / 60px 100%;
    -webkit-mask: var(--mask);
    mask: var(--mask);
}

.quantity-label {
    font-size: 18px;
    font-weight: bold;
    color: #333333;
    margin-bottom: 3px;
}

.selected-quantity {
    font-size: 24px;
    color: #333333;
}

.comment {
  border: 1px solid #ccc;
  margin: 10px;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 10px;
}



.profile-icon {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background-color: #3979d2;
    font-size: 20px;
    color: #fff;
    padding-bottom: 6px;
    padding-left: 10px;
    display: flex;
    /* use flexbox */
    /* justify-content: center; */
    /* center horizontally */
    align-items: center;
    
}
</style>

