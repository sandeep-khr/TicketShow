<template>
  
    <div class="container">
      <AdminNavigation @edit="editt" />
      <div v-show="theaters.length > 0">
        <TheaterCard v-for="(theater, index) in theaters" :key="index" :theater="theater" :edit="edit"/>
      </div>
      <NoTheater/>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useAuthStore } from '../stores/index';
  import AdminNavigation from '../components/AdminNavigation.vue';
  import NoTheater from '../components/NoTheater.vue';
  import TheaterCard from '../components/TheaterCard.vue';
  
  export default {
    components: {
      AdminNavigation,
      NoTheater,
      TheaterCard,
    },
    setup() {
      const authStore = useAuthStore();
      const theaters = ref([]);
  
      // Fetch theaters when the component is mounted
      onMounted(async () => {
        try {
          theaters.value = await authStore.fetchTheaters();
        } catch (error) {
          console.error(error);
        }
      });
  
      return {
        theaters,
      };
    },
    data() {
      return {
        edit: null,
      };
    },
    methods: {
      editt(value) {
        this.edit = value;
      }
    },
  };
  </script>
  