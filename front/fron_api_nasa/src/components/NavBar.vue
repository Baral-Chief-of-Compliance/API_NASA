<template>
    <div class="content">
        <img class="logo" src="../assets/NASA_Logo_1959.svg" width="150" height="150" alt="image format png" />
        <div class="links">
            <router-link class='link' to="/">photo of the day</router-link>
            <router-link class='link' to="/find_a_photo">find a photo</router-link>
            <router-link class='link' to="/archive">archive</router-link> 
        </div>

    </div>
</template>
  
  <style scoped>
    .content{
        display: flex;
        flex-direction: row;
        padding-right: 20%;
        padding-left: 20%;
        background-color: black;
    }

    .logo{
        margin-right: 45px;
    }

    .links{
        display: flex;
        flex-direction: row;
        padding-top: 75px;
        font-weight: 24px;
        padding-bottom: 50px;
    }

    .link{
        margin-left: 45px;
        margin-right: 45px;
    }

    .link{
        text-decoration: none;
        color: white;
    }

    .link:hover{
        color: #0000ff;
    }
  </style>