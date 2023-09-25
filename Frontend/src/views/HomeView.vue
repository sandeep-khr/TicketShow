<template>
    <div>
        <Navigation @location="elocation"></Navigation>
        <Carousel></Carousel>
        <Shows :location="location"></Shows>
    </div>
</template>

<script>
import Navigation from '../components/Navigation.vue';
import Carousel from '../views/Carousel.vue';
import Shows from '../views/Shows.vue';
    export default {
    components: { Carousel, Shows, Navigation },
    data() {
        return {
            location: null,
        }
    },
    methods: {
        elocation(value) {
            this.location = value;
        }
    }
}
</script>

<style scoped>

</style>