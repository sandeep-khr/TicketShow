<template>
    <div class="">
      <div class="mb-3 d-flex justify-content-between">
        <input
          id="datepicker"
          type="date"
          class="form-control me-4"
          v-model="selectedDate"
          :min="minDate"
        />
        <input
          id="timepicker"
          type="time"
          class="form-control"
          v-model="selectedTime"
          :step="timeStep"
        />
      </div>
      <div class="mb-3">
        
      </div>
    </div>
</template>
  
<script>
export default {
    data() {
      return {
        selectedDate: null,
        selectedTime: null,
      };
    },
    computed: {
      minDate() {
        const today = new Date().toISOString().split('T')[0];
        return today;
      },
      timeStep() {
        // Customize this if you want to set a different time step (e.g., '900' for 15-minute intervals)
        return '60'; // 1-minute intervals
      },
    },
  };
</script>
  