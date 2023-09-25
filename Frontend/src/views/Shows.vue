<template>
    <div v-if="!location" class="container mt-3">
        <div class="d-flex justify-content-between">
            <h3 class="mb-2" style="text-shadow: rgb(7, 195, 253) 1px 0 10px;">🎬 Latest Shows</h3>
            <span></span>
        </div>
        <div class="row mt-2">
            <div class="col-md-2" v-for="show in filteredShows2" :key="show.id">
                <div class="card mb-2">
                    <router-link :to="{ name: 'ShowDetails', params: { id: show.id } }">
                        <img :src="show.image_url" class="card-img-top" alt="Movie Poster">
                    </router-link>
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
                            <p><i class="fas fa-indian-rupee-sign" style="color: #FFCC33;"></i> {{ show.ticket_price }}</p>
                        </div>
                        <p class="card-text">
                        <div class="d-flex justify-content-between">
                            <p>{{ show.language.charAt(0).toUpperCase() + show.language.slice(1) }}</p>
                            <p>{{ show.movie_length }}</p>
                        </div>
                        <!-- {{ new Date(show.show_date).toLocaleString('en-GB', {
                            day: 'numeric', month: 'short', hour: '2-digit',
                            minute: '2-digit'
                        }) }} -->

                        <p class="mb-0 text-center border-top">{{ this.formatMovieShowTime(show.show_date) }}</p>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <div v-else class="container mt-4">
        <h3 style="text-shadow: rgb(7, 195, 253) 1px 0 10px;" class="mb-2">🎬 Latest Shows In {{
            location.charAt(0).toUpperCase() + location.slice(1) }}</h3>
        <div class="row mt-2">
            <div class="col-md-2" v-for="show in filteredShows" :key="show.id">
                <div class="card mb-2">
                    <router-link :to="{ name: 'ShowDetails', params: { id: show.id } }">
                        <img :src="show.image_url" class="card-img-top" alt="Movie Poster">
                    </router-link>
                    <div class="card-body">
                        <div class="d-flex justify-content-between">
                            <div class="text-warning" style="font-weight: 700; font-size: large;">
                                <!-- <i class="fa fa-heart mx-1"></i> -->
                                <span class="ml-2">{{ show.rating/show.total_rating || 0}} ⭐</span>
                            </div>
                            <p class="text-muted">{{ show.total_rating }} Votes</p>
                        </div>
                        <div class="d-flex justify-content-between">
                            <h6 class="card-title">{{ show.name }}</h6>
                            <p><i class="fas fa-indian-rupee-sign" style="color: #FFCC33;"></i> {{ show.ticket_price }}</p>
                        </div>
                        <p class="card-text">
                        <div class="d-flex justify-content-between">
                            <p>{{ show.language.charAt(0).toUpperCase() + show.language.slice(1) }}</p>
                            <p>{{ show.movie_length }}</p>
                        </div>
                        <!-- {{ new Date(show.show_date).toLocaleString('en-GB', {
                            day: 'numeric', month: 'long', hour: '2-digit',
                            minute: '2-digit'
                        }) }} -->

                        {{ formatMovieShowTime(show.show_date) }}

                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useAuthStore } from '../stores/index.js';
export default {
    props: { location, },
    data() {
        return {
            shows: [],
        }
    },
    async mounted() {
        const authStore = useAuthStore();
        try {
            this.shows = await authStore.fetchShows();
        } catch (error) {
            console.error(error);
        }
    },
    computed: {
        // Filter shows based on location (l)
        filteredShows() {
            if (!this.shows) {
                return [];
            }

            const currentDate = new Date().toISOString().slice(0, 16);
            // if (!this.location) {
            //     // Show all latest shows whose show_date is greater than the current date
            //     return this.shows.filter((show) => new Date(show.show_date).toISOString().slice(0, 16) > currentDate).sort((a, b) => new Date(b.show_date) - new Date(a.show_date));
            // }

            // if (!this.location) {
            //     return this.shows.filter(show => show.location == 'patna');
            // }
            // Show latest shows for the selected location whose show_date is greater than the current date
            return this.shows.filter((show) => show.location === this.location && new Date(show.show_date).toISOString().slice(0, 16) > currentDate).sort((a, b) => new Date(b.show_date) - new Date(a.show_date));
        },
        filteredShows2() {
            const currentDate = new Date().toISOString().slice(0, 16);

            return this.shows.filter((show) => new Date(show.show_date).toISOString().slice(0, 16) > currentDate).sort((a, b) => new Date(b.show_date) - new Date(a.show_date));
        },


    },
    methods: {
        formatMovieShowTime(show_date) {
            const showDate = new Date(show_date);
            const day = showDate.toLocaleString('en-GB', { day: '2-digit' });
            const month = showDate.toLocaleString('en-GB', { month: 'short' });
            const time = showDate.toLocaleString('en-GB', { hour: '2-digit', minute: '2-digit' });
            return `⌚${time} 📆${day} ${month}`;
        }
    }

}
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

.card-img-top {
    height: 30vh;
    object-fit: cover;
}
</style>