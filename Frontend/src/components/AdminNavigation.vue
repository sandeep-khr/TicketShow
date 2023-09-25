<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <router-link to="/"><img src="../assets/images/logo.png" alt="" style="height: 40px;"></router-link>
                <router-link to="/" class="navbar-brand">TicketShow</router-link>

                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <!-- <router-link class="nav-link active" aria-current="page" to="#">Theaters</router-link> -->
                        </li>
                        <!-- <p>{{ edit }}</p> -->
                        <li class="nav-item">
                            <!-- <router-link class="nav-link active" aria-current="page" to="#">Shows</router-link> -->
                        </li>
                        <li class="nav-item text-muted" style="font-size: large;">
                            <!-- <router-link class="nav-link active" aria-current="page" to="#">Summary</router-link> -->
                        </li>
                    </ul>
                    <label class="m-2">Toggle <span class="text-muted">Edit/Delete</span></label>
                    <input v-model="edit" @change="sendEdit" class="mt-2" type="checkbox" name="one">
                    <div class="nav-item dropdown d-flex">
                        <div style="margin-right: 60px;"></div>
                        <span class="p-2">Admin</span>
                            <div class="nav-link profile-icon" id="navbarDropdown" role="button"
                                data-bs-toggle="dropdown" aria-expanded="false" v-text="initials">
                            </div>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li @click="addAdmin"><p class="dropdown-item text-secondary">Add Admin</p></li>
                                <li ><p class="dropdown-item text-danger" @click="logoutUser" style="">Log Out</p></li>
                            </ul>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
import { useAuthStore } from '../stores';
export default {
    data() {
    return {
      edit: null
    }
  },
  computed: {
    initials() {
        const auth = JSON.parse(localStorage.getItem('auth'));
        const username = auth.user.username;
        return username[0].toUpperCase();
    },
    logoutUser() {
            const authStore = useAuthStore();
            authStore.logout();
    },

  },
  methods: {
    sendEdit() {
      this.$emit('edit', this.edit);
    },
    addAdmin() {
      this.$router.push('/add-admin');
      

    }
  },
}
</script>

<style scoped>
.profile-icon {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  
  background: rgb(48,207,208);
  background: linear-gradient(90deg, rgba(48,207,208,1) 35%, rgba(51,8,103,1) 100%);
  font-size: 20px;
  font-weight: 700;
  color: #fff;
  display: flex; 
  justify-content: center; 
  align-items: center; 
  &:hover {
    cursor: pointer;
    color: rgba(245, 245, 245, 0.805);
  }
}

input {
  --s:25px; 
  
  height:var(--s);
  aspect-ratio:2/1;
  padding:calc(var(--s)/5);
  border-radius:var(--s);
  background:
    radial-gradient(farthest-side,#fafafa 85%,#0005,#0000) left/var(--s) 100% no-repeat,
    linear-gradient(90deg,#207fb6 50%,#939393 0) right/200% 100% content-box;
  transition:0.5s;
  -webkit-appearance:none;
  -moz-appearance:none;
  appearance:none;
  cursor:pointer;
}
input:checked {
  background-position:right,left;
}
.navbar-brand{
    font-size: 25px;
    font-weight: 500;
    background: -webkit-linear-gradient(#30CFD0, #330867);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
}

.dropdown-item{
  &:hover {
    background-color: #f8f9fa;
    color: #000;
  };
  cursor: pointer;
}
</style>

