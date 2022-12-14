<template>
    <div class="content">

        <div class="title">
            <div>
                {{ data_current_day.date }}
            </div>
            <div>
                {{ data_current_day.title }}
            </div>
        </div>

        <div class="img">
            <img v-bind:src=data_current_day.hdurl alt="">
        </div>
        <div  class="explanation">
            {{ data_current_day.explanation }}
        </div>

    </div>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return{
            data_current_day: null
        }
    },
    created(){
        axios
            .get('http://127.0.0.1:5000/archiv_nasa/api/v1.0/photo_of_the_day/')
            .then(response => (this.data_current_day = response.data))
    }
}
</script>

<style scoped>

.content{
        color: white;
        margin-left: 17%;
        padding-top: 50px;
        }

    .title{
        font-size: 30px;
    }
    .img{
        padding-top: 25px;
    }
    .img img{
        /* object-fit: cover;
        width: 1000px;
        height: 600px; */
        display: block;
        max-width:1000px;
        max-height:600px;
        width: auto;
        height: auto;
    }

    .explanation{
        margin-top: 25px;
        margin-right: 20%;
    }
</style>
