<template>
          <div class="animated-background"></div>

    <Navigation />
    <div class="container mt-2">
        <div class="">
            <div class="row">
                <div class="col-md-3">
                    <!-- Sidebar with filter options -->
                    <div class="card">
                        <div class="card-body">
                            <!-- Filter options -->
                            <div class="d-flex justify-content-between">
                                <h5 class="card-title">Filter Options</h5>
                                <p class="text-primary" @click="clear" style="cursor: pointer;">clear all</p>
                            </div>

                            <!-- Genre filter -->
                            <h6>Tags</h6>
                            <div class="form-group">
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="action" name="genre"
                                        id="genreAction" v-model="selectedGenre">
                                    <label class="form-check-label" for="genreAction">Action</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="comedy" name="genre"
                                        id="genreComedy" v-model="selectedGenre">
                                    <label class="form-check-label" for="genreComedy">Comedy</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="drama" name="genre" id="genreDrama"
                                        v-model="selectedGenre">
                                    <label class="form-check-label" for="genreDrama">Drama</label>
                                </div>
                            </div>

                            <!-- Language filter -->
                            <h6>Language</h6>
                            <div class="form-group">
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="english" name="lang"
                                        id="langEnglish" v-model="selectedLanguage">
                                    <label class="form-check-label" for="langEnglish">English</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="hindi" name="lang" id="langHindi"
                                        v-model="selectedLanguage">
                                    <label class="form-check-label" for="langHindi">Hindi</label>
                                </div>

                                <!-- Add more language radioes here -->
                            </div>

                            <!-- Location filter -->
                            <h6>Location</h6>
                            <div class="form-group">
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="patna" name="location"
                                        id="locationPatna" v-model="selectedLocation">
                                    <label class="form-check-label" for="locationPatna">Patna</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="delhi" name="location"
                                        id="locationDelhi" v-model="selectedLocation">
                                    <label class="form-check-label" for="locationDelhi">Delhi</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="mumbai" name="location"
                                        id="locationMumbai" v-model="selectedLocation">
                                    <label class="form-check-label" for="locationMumbai">Mumbai</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="chennai" name="location"
                                        id="locationChennai" v-model="selectedLocation">
                                    <label class="form-check-label" for="locationChennai">Chennai</label>
                                </div>
                            </div>

                            <!-- Theater name search -->
                            <h6 v-if="theaters">Theater Name</h6>
                            <div class="form-group">
                                <div class="form-check" v-for="theater in theaters" :key="theater.id">
                                    <input class="form-check-input" type="radio" :value="theater.id" name="theater"
                                        :id="theater.name" v-model="selectedTheater">
                                    <label class="form-check-label" :for="theater.name">{{ theater.name.toUpperCase()
                                    }}</label>
                                </div>
                            </div>

                            <!-- Voting filter -->
                            <h6>Voting</h6>
                            <div class="form-group">
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="above4" name="rating"
                                        id="votingAbove80" v-model="selectedRating">
                                    <label class="form-check-label" for="votingAbove80">Above 4 ⭐</label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" value="above3" name="rating"
                                        id="votingAbove90" v-model="selectedRating">
                                    <label class="form-check-label" for="votingAbove90">Above 3 ⭐</label>
                                </div>
                                <!-- <div class="form-check">
                                    <input class="form-check-input" type="radio" value="above90" name="rating"
                                        id="votingAbove70" v-model="selectedRating">
                                    <label class="form-check-label" for="votingAbove70">Above 70%</label>
                                </div> -->
                                <!-- Add more voting radioes here -->
                            </div>

                            <!-- Add your submit button or additional filter options here -->

                        </div>
                    </div>
                </div>

                <div class="col-md-9">
                    <!-- Movie cards section -->
                    <div class="row">
                        <div class="col-md-3" v-for="show in filteredShows" :key="show.id">
                            <div class="card mb-3 card1">
                                <router-link :to="{ name: 'ShowDetails', params: { id: show.id } }">
                                    <img :src="show.image_url" class="card-img-top" alt="Movie Poster">
                                </router-link>
                                <div class="card-body">
                                    <div class="d-flex justify-content-between">
                                        <div class="text-warning" style="font-size: large; font-weight: 700;">
                                            <span class="ml-2">{{ show.rating / show.total_rating || 0 }} ⭐</span>
                                        </div>
                                        <p class="text-muted">{{ show.total_rating }} Votes</p>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <h6 class="card-title">{{ show.name }}</h6>
                                        <p><i class="fas fa-indian-rupee-sign" style="color: #FFCC33;"></i>{{
                                            show.ticket_price }}</p>
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
            </div>
        </div>

    </div>
</template>

<script>
import { useAuthStore } from '../stores/index.js';
import Navigation from '../components/Navigation.vue';
export default {
    components: { Navigation },
    data() {
        return {
            name: null,
            skey: this.$route.query.skey,
            shows: [],
            selectedGenre: '',       // Add selectedGenre variable
            selectedLanguage: '',    // Add selectedLanguage variable
            selectedLocation: '',    // Add selectedLocation variable
            selectedTheater: '',     // Add selectedTheater variable
            selectedRating: '',      // Add selectedRating variable
            theaters: []
        };
    },
    async mounted() {
        const authStore = useAuthStore();
        try {
            this.shows = await authStore.fetchShows();
        } catch (error) {
            console.error(error);
        }
    },
    async created() {
        const authStore = useAuthStore();
        try {
            this.theaters = await authStore.fetchTheaters();
        } catch (error) {
            console.error(error);
        }
    },
    computed: {
        // Filter shows based on query and filter options
        filteredShows() {
            const query = this.skey.toLowerCase().trim();
            return this.shows.filter((show) => {
                // Filter by movie name/title
                const movieName = show.name.toLowerCase();
                if (!query || movieName.includes(query)) {
                    // Genre filter
                    if (this.selectedGenre && show.tags.toLowerCase() !== this.selectedGenre) {
                        return false;
                    }

                    // Language filter
                    if (this.selectedLanguage && show.language.toLowerCase() !== this.selectedLanguage) {
                        return false;
                    }

                    // Location filter
                    if (this.selectedLocation && show.location.toLowerCase() !== this.selectedLocation) {
                        return false;
                    }

                    // Theater filter
                    if (this.selectedTheater && show.theatre_id !== (this.selectedTheater)) {
                        return false;
                    }

                    // Voting filter
                    if (this.selectedRating) {
                        // const votePercent = (show.rating / show.total_rating);
                        if (this.selectedRating === 'above3' && show.rating / show.total_rating <= 3) {
                            return false;
                        } else if (this.selectedRating === 'above4' && show.rating / show.total_rating <= 4) {
                            return false;
                        } 
                        // else if (this.selectedRating === 'above90' && votePercent <= 90) {
                        //     return false;
                        // }
                    }
                    // If all filters pass, include the show
                    return true;
                }
                // else {
                //   // Exclude shows that don't match the query
                //   return false;
                // }
            });
        },
    },
    watch: {
        '$route.query.skey': function (newSkey, oldSkey) {
            // Update the 'skey' property when the query parameter changes
            this.skey = newSkey;
        },
        skey: function (newSkey, oldSkey) {
            // Trigger a re-computation of the filteredShows whenever 'skey' changes
            this.$nextTick(() => {
                this.$forceUpdate();
            });
        }
    },
    methods: {
        formatMovieShowTime(show_date) {
            const showDate = new Date(show_date);
            const day = showDate.toLocaleString('en-GB', { day: '2-digit' });
            const month = showDate.toLocaleString('en-GB', { month: 'short' });
            const time = showDate.toLocaleString('en-GB', { hour: '2-digit', minute: '2-digit' });
            return `⌚${time} 📆${day} ${month}`;
        },
        clear(){
            this.selectedGenre = '';
            this.selectedLanguage = '';
            this.selectedLocation = '';
            this.selectedTheater = '';
            this.selectedRating = '';
        }
    }
};

</script>

<style scoped>
.card-img-top {
    height: 40vh;
    object-fit: cover;

    
}

.card1 {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: 0.5s ease all;

    &:hover {
        transform: rotateZ(-1deg) scale(1.01);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
            0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

}
</style>