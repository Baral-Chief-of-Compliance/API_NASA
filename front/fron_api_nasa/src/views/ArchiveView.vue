<template>
    <div class="content" >
        <li v-for="date in allDates">
            <router-link class='link' v-bind:to="'/photo/'+date.split('-')[0]+'-'+date.split('-')[1]+'-'+date.split('-')[2]">{{date}}</router-link>
        </li>
    </div>
</template>

<script>
import axios from 'axios'


export default{

    data(){
        return{
            allDates: null
        };
    },
    mounted() {
            axios
                .get('http://127.0.0.1:5000/archiv_nasa/api/v1.0/all_dates')
                .then ( response => (this.allDates = response.data))
            
    }

}   

</script>

<style scoped>
    .content{
        margin-right: 20%;
        margin-left: 20%;
        padding-top: 25px;
    }

    .content li{
        padding-top: 25px;
    }

    .link{
        text-decoration: none;
        color: white;
        font-size: 30px;
    }
    .link:hover{
        color: #0000ff;
    }
</style>