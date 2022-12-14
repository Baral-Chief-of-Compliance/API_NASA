<template>
    <div class="content">
        <div class="title">
            <div>
                {{ year }}-{{ month }}-{{ day }}
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

</template>

<script>
import axios from 'axios'


export default{
    data(){
        return{
            data_about_day: null
        };
    },
    computed:{
        year(){
            return this.$route.params.year
        },

        month(){
            return this.$route.params.month
        },

        day(){
            return this.$route.params.day
        }
    },
    created(){
        axios
                .get('http://127.0.0.1:5000/archiv_nasa/api/v1.0/photo_of_define_day/'+this.year+'-'+this.month+'-'+this.day)
                .then ( response => (this.data_about_day = response.data))
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