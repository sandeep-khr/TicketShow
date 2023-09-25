// store/index.js
import { defineStore } from 'pinia';
import router from '../router/index';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: null,
  }),
  persist: true,
  getters:{
    isLoggedIn(state){
      return !!state.token; 
    }
  },

  actions:{
    setToken(token){
      this.token = token;
      localStorage.setItem('authToken', token);
      // sessionStorage.setItem('authToken', token);

    },
    setUser(user) {
      this.user = user;
    },
    clearToken(){
      this.token = null;
      localStorage.removeItem('authToken');
      // sessionStorage.removeItem('authToken');
    },
    async login({ username, password }) {
      try {
        const response = await fetch('http://127.0.0.1:8000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password }),
        });

        if (!response.ok) {
          throw new Error('Invalid username or password');
        }

        const data = await response.json();
        // console.log('data:', data);
        this.setToken(data.access_token);
        const decodedToken = JSON.parse(atob(data.access_token.split('.')[1]));
        // console.log('access_token:', data.access_token)
        // console.log('decodedToken:', decodedToken);
        // console.log('payload:', decodedToken.sub);
        this.setUser(decodedToken.sub)
        // console.log('user:', this.user);
        // console.log('name', this.user.name)
        router.push({ name: 'Home' });

      } catch (error) {
        console.error(error);
        // throw new Error('Failed to login');
        throw error;
      }
    },
    async signup({ username, password, email }) {
      try {
        const response = await fetch('http://127.0.0.1:8000/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ username, password, email }),
        });

        if (response.status == 400) {
          // throw new Error('Failed to sign up');
          throw new Error('All fields are required');
        }
        if (response.status == 409) {
          // throw new Error('Failed to sign up');
          throw new Error('Username already exists');
        }

        router.push({ name: 'Login' });

      } catch (error) {
        console.error(error);
        // throw new Error('Failed to sign up');
        throw error;
      }
    },
    async addAdmin(username){
      try {
        const response = await fetch('http://127.0.0.1:8000/add_admin', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify({ "username": username}),
        });

        const data = await response.json();
        return data;

      } catch (error) {
        console.error(error);
        throw new Error('Failed to add admin');
      }
    },
    async logout() {
      this.clearToken();
      this.setUser(null);
      router.push({ name: 'Login' });
    },
    // Action to fetch all theaters
    async fetchTheaters() {
      try {
        const response = await fetch('http://127.0.0.1:8000/theater', {
          // headers: {
          //   Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          // },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch theaters');
        }

        const data = await response.json();
        // console.log('data:', data);
        return data;
        
      } catch (error) {
        console.error(error);
        throw new Error('Failed to fetch theaters');
      }
    },

    // Action to fetch a specific theater by ID
    async fetchTheaterById(theaterId) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/theater/${theaterId}`, {
          // headers: {
          //   Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          // },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch the theater');
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to fetch the theater');
      }
    },

    // Action to create a new theater
    async createTheater(theaterData) {
      try {
        const response = await fetch('http://127.0.0.1:8000/theater', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify(theaterData),
        });

        if (response.status == 400) {
          throw new Error('All fields are required');
        }

        const data = await response.json();
        return data;

      } catch (error) {
        console.error(error);
        // throw new Error('Failed to create theater');
        throw error;
      }
    },
    // Action to update an existing theater
    async updateTheater(theaterId, theaterData) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/theater/${theaterId}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify(theaterData),
        });

        if (!response.ok) {
          throw new Error('Failed to update theater');
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to update theater');
      }
    },
    // Action to delete a theater
    async deleteTheater(theaterId) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/theater/${theaterId}`, {
          method: 'DELETE',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to delete theater');
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to delete theater');
      }
    },

    // Action to fetch all shows (movies)
    async fetchShows() {
      try {
        const response = await fetch('http://127.0.0.1:8000/show', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch shows');
        }

        const data = await response.json();
        console.log('data:', data);
        return data;
        
      } catch (error) {
        console.error(error);
        throw new Error('Failed to fetch shows');
      }
    },

    // Action to fetch a specific show (movie) by ID
    async fetchShowById(showId) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/show/${showId}`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch the show');
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to fetch the show');
      }
    },

    // Action to create a new show (movie)
    async createShow(showData) {
      try {
        const response = await fetch('http://127.0.0.1:8000/show', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify(showData),
        });

        // if (response.status == 400) {
        //   throw new Error('All fields are required');
        // }

        // if (response.status == 404) {
        //   throw new Error('MOVIE NOT FOUND');
        // }
        if (!response.ok) {
          const data = await response.json();
          throw new Error(data.error);
        }

        const data = await response.json();
        console.log('data:', data);
        return data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    },

    // Action to update an existing show (movie)
    async updateShow(showId, showData) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/show/${showId}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify(showData),
        });

        if (!response.ok) {
          throw new Error('Failed to update the show');
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to update the show');
      }
    },

    // Action to delete a show (movie)
    async deleteShow(showId) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/show/${showId}`, {
          method: 'DELETE',
          headers: {
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to delete the show');
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to delete the show');
      }
    },

    // Action to fetch all bookings
    async fetchBookings() {
      try {
        const response = await fetch('http://127.0.0.1:8000/booking', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch bookings');
        }

        const data = await response.json();
        // console.log('data:', data);
        return data;
        
      } catch (error) {
        console.error(error);
        throw new Error('Failed to fetch bookings');
      }
    },

    // Action to book a ticket
    async bookTicket(bookingData) {
      try {
        const response = await fetch('http://127.0.0.1:8000/booking', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify(bookingData),
        });

        if (!response.ok) {
          throw new Error('Failed to book the ticket');
        }

        const data = await response.json();
        console.log('data:', data);
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to book the ticket');
      }
    },

    async vote(showId, voteData) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/show/${showId}/vote`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify(voteData),
        });

        if(response.status == 400){
          const responseData = await response.json();
          if(responseData.error === 'Rating value is missing'){
              throw new Error('Rating value is missing');
          }else if(responseData.error === 'You have already voted for this show'){
              throw new Error('You have already voted for this show');
          }
          // else if(responseData.error === 'You can only vote after the show has ended'){
          //     throw new Error('You can only vote after the show has ended');
          // }
          else{
              throw new Error('Failed to vote');
          }
        }

        if (response.status == 404){
          throw new Error("You haven't watched this film yet.");
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    },

    async comment(showId, commentData) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/show/${showId}/comment`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${localStorage.getItem('authToken')}`,
          },
          body: JSON.stringify(commentData),
        });
        
        if(response.status == 400){
          const responseData = await response.json();
          if(responseData.error === 'Comment value is missing'){
              throw new Error('Comment value is missing');
          }
          // else if(responseData.error === "You can only comment after the show has ended"){
          //   throw new Error("You can only comment after the show has ended");
          // }
          else{
              throw new Error('Failed to comment');
          }
        }

        if(response.status == 404){
          throw new Error("You haven't watched this film yet.");
        }

        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw error;
      }
    },
    
    async export(theaterId){
      try{
        const response = await fetch(`http://127.0.0.1:8000/export_data/${theaterId}`);
        if (!response.ok) {
          throw new Error('Failed to export data');
        }
        const data = await response.json();
        return data;
      } catch (error) {
        console.error(error);
        throw new Error('Failed to export data');
      }
    },
    
  }
});
