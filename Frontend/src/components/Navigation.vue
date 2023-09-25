<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light rounded-bottom" style="opacity: 1; font-weight: 500;">
            <div class="container-fluid">
            <router-link to="/"><img src="../assets/images/logo.png" alt="" style="height: 40px;"></router-link>
            <router-link to="/" class="navbar-brand">TicketShow</router-link>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <input v-model="skey" class="msearch" type="search" placeholder="Search for movies ..." aria-label="Search">
                        <button class="btn btn-outline-secondary ms-1" type="submit" @click="search">Search</button>
                    </li>
                </ul>
                <div class="text-muted">
                    <i class="fas fa-location-dot" style="height: 20px;"></i>
                    <select class="select mx-2" v-model="location">
                        <option value="patna">Patna</option>
                        <option value="delhi">Delhi</option>
                        <option value="chennai">Chennai</option>
                        <option value="mumabi">Mumbai</option>
                    </select>
                </div>

                <div v-if="isloggedIn" class="nav-item dropdown d-flex">
                    <div >
                        <ul class="navbar-nav">
                            <li class="nav-item ">
                                <!-- <a class="nav-link" href="movies.html"><i class="fa-solid fa-ticket mx-1"></i>Tickets</a> -->
                                <router-link to="/bookings" class="nav-link"><i class="fa-solid fa-ticket mx-1"></i>Tickets</router-link>
                            </li>
                            <!-- <li class="nav-item">
                            <a class="nav-link" href="#" data-toggle="modal" data-target="#notificationsModal">
                                <i class="fas fa-bell"></i>
                            </a>
                        </li> -->
                        </ul>
                    </div>
                    <span class="p-2 text-muted">{{username}}</span>
                    <div class="nav-link profile-icon" id="navbarDropdown" role="button" data-bs-toggle="dropdown"
                        aria-expanded="false" v-text="initials">
                    </div>
                    <ul class="dropdown-menu ms-5" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="#"></a></li>
                        <li v-show="ifAdmin"><router-link class="dropdown-item" to="/admin">Admin</router-link></li>
                        <li v-if="isloggedIn"><p class="dropdown-item" @click="logoutUser">Log Out</p></li>
                        <li v-else><router-link class="dropdown-item" to="/login">Login</router-link></li>
                        <hr>
                        <li><router-link class="dropdown-item" to="/signup">Sign Up</router-link></li>
                        <!-- <li>
                            <hr class="dropdown-divider">
                        </li>
                        <li><a class="dropdown-item" href="#">Something else here</a></li> -->
                    </ul>
                </div>
                <div v-else class="navbar">
                    <ul class="navbar-nav">
                        <li class="nav-item mx-2"><router-link  to="/signup" style="text-decoration: none;" class="text-muted">Sign Up /</router-link></li>
                        <li class="nav-item"><router-link  to="/login" style="text-decoration: none;" class="text-muted">Login</router-link></li>
                    </ul>
                </div>
            </div>
            </div>
        </nav>
    </div>
</template>

<script>
import { useAuthStore } from '../stores/index.js';
export default {
    data() {
        return {
            edit: null,
            location: 'patna',
            skey: '',
        }
    },
    computed: {
        initials() {
            const auth = JSON.parse(localStorage.getItem('auth'));
            const username = auth.user.username;
            return username[0].toUpperCase();
        },
        username() {
            const auth = JSON.parse(localStorage.getItem('auth'));
            return auth.user.username;
        },
        ifAdmin(){
            const auth = JSON.parse(localStorage.getItem('auth'));
            return auth.user.is_admin;
        },
        logoutUser() {
            const authStore = useAuthStore();
            authStore.logout();
        },
        isloggedIn() {
            const authStore = useAuthStore();
            return authStore.isLoggedIn;
        }
    },
    methods: {
        sendEdit() {
            this.$emit('edit', this.edit);
        },
        search(){
            this.$router.push({name: 'search', query: {skey: this.skey}});
        }
    },
    watch: {
        location() {
            this.$emit('location', this.location);
            console.log(this.location);
        }
    }
}
</script>

<style scoped>
select {
    width: 100px;
    padding: 3px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.msearch {
    width: 200px;
    padding: 4px 4px 8px 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.btn {
    font-weight: 500;
}

.profile-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    /* background-color: #3979d2; */
    background: rgb(48, 207, 208);
    background: linear-gradient(90deg, rgba(48, 207, 208, 1) 35%, rgba(51, 8, 103, 1) 100%);
    font-size: 20px;
    font-weight: 700;
    color: #fff;
    display: flex;
    /* use flexbox */
    justify-content: center;
    /* center horizontally */
    align-items: center;

    /* center vertically */
    &:hover {
        cursor: pointer;
        color: rgba(245, 245, 245, 0.805);
    }
}

.navbar-brand {
    font-size: 25px;
    font-weight: 500;
    background: -webkit-linear-gradient(#30CFD0, #330867);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>

