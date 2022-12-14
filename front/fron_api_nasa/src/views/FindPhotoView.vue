<template>
    <div class="content">
        <div class="search-block">
            <input v-model="date" type="date">
            <button @click="get_date">find photo of the day</button>
        </div>

        <div class="title">
            <div>
                {{ data_about_day.date }}
            </div>
            <div>
                {{ data_about_day.title }}
            </div>
        </div>

        <div class="img">
            <img v-bind:src=data_about_day.hdurl alt="">
        </div>
        <div  class="explanation">
            {{ data_about_day.explanation }}
        </div>

       
    </div>
    <div> {{ data_about_day }}</div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

// let data_about_day = ref(null)

export default{
    methods:{
        get_date(){
            this.date_of_day = this.date
            
            axios
            .get('http://127.0.0.1:5000/archiv_nasa/api/v1.0/photo_of_define_day/'+this.date_of_day.split('-')[0]+'-'+this.date_of_day.split('-')[1]+'-'+this.date_of_day.split('-')[2])
                .then ( response => (this.data_about_day = response.data))
        }
    },
    data(){
        return{
            date_of_day: null,
            data_about_day: ''
        }
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

    input{
        color-scheme: dark;
    }

    button{
        background-color: white;
    }
</style>
