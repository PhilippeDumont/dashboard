<template>
    <v-container>
        <div class="sideBar">
            <ul>
                <li class="item">
                    <svg viewBox="0 0 24 24">
                        <path fill="currentColor" d="M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z" />
                    </svg>
                    <br />
                    Home
                </li>
                <li class="item">
                    <svg viewBox="0 0 24 24">
                        <path fill="currentColor" d="M3,22V8H7V22H3M10,22V2H14V22H10M17,22V14H21V22H17Z" />
                    </svg>
                    <br />
                    Level 1
                </li>
                <li class="item">
                    <svg viewBox="0 0 24 24">
                        <path fill="currentColor" d="M21,16.5C21,16.88 20.79,17.21 20.47,17.38L12.57,21.82C12.41,21.94 12.21,22 12,22C11.79,22 11.59,21.94 11.43,21.82L3.53,17.38C3.21,17.21 3,16.88 3,16.5V7.5C3,7.12 3.21,6.79 3.53,6.62L11.43,2.18C11.59,2.06 11.79,2 12,2C12.21,2 12.41,2.06 12.57,2.18L20.47,6.62C20.79,6.79 21,7.12 21,7.5V16.5M12,4.15L6.04,7.5L12,10.85L17.96,7.5L12,4.15M5,15.91L11,19.29V12.58L5,9.21V15.91M19,15.91V9.21L13,12.58V19.29L19,15.91Z" />
                    </svg>
                    <br />
                    Level 2
                </li>
                <li class="item">
                    <svg viewBox="0 0 24 24">
                        <path fill="currentColor" d="M12,4A4,4 0 0,1 16,8A4,4 0 0,1 12,12A4,4 0 0,1 8,8A4,4 0 0,1 12,4M12,14C16.42,14 20,15.79 20,18V20H4V18C4,15.79 7.58,14 12,14Z" />
                    </svg>
                    <br />
                    Level 3
                </li>
                <li class="item">
                    <svg viewBox="0 0 24 24">
                        <path fill="currentColor" d="M10,19H13V22H10V19M12,2C17.35,2.22 19.68,7.62 16.5,11.67C15.67,12.67 14.33,13.33 13.67,14.17C13,15 13,16 13,17H10C10,15.33 10,13.92 10.67,12.92C11.33,11.92 12.67,11.33 13.5,10.67C15.92,8.43 15.32,5.26 12,5A3,3 0 0,0 9,8H6A6,6 0 0,1 12,2Z" />
                    </svg>
                    <br />
                    Level 4
                </li>
                <li id="edit" class="item">
                    <svg viewBox="0 0 24 24">
                        <path fill="currentColor" d="M20.71,7.04C21.1,6.65 21.1,6 20.71,5.63L18.37,3.29C18,2.9 17.35,2.9 16.96,3.29L15.12,5.12L18.87,8.87M3,17.25V21H6.75L17.81,9.93L14.06,6.18L3,17.25Z" />
                    </svg>
                    <br />
                    Edit
                </li>
                <li class="item">
                    <svg viewBox="0 0 24 24">
                        <path fill="currentColor" d="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z" />
                    </svg>
                    <br />
                    Settings
                </li>
            </ul>
        </div>
    </v-container>
</template>


<script>

    export default {
        data() {
            return {
            }
        },
    }
</script>


<style scoped>
    #edit{
        margin-top: 140px;
    }

    .item:hover{
        background-color: blueviolet;
        filter: grayscale(50%);
    }

    .item:active{
        box-shadow: 6px 6px 18px 2px rgba(0, 0, 0, 0.23);
        transform: scale(0.95);
    }

    .sideBar{
        background-color: #013F52;
        color: white;
        cursor: pointer;
        height: 100%;
        left: 0;
        overflow: auto;
        position: fixed;
        top: 0;
        width: auto;
    }

    .sideBar ul{
        padding: 0;
    }

    .sideBar ul li{
        border-radius: 8px;
        list-style: none;
        margin: 10px;
        text-align: center;
    }

    svg{
        width: 50px;
        height: 50px;
    }

    ::-webkit-scrollbar {
      height: 6px;
      width: 6px;
    }

    ::-webkit-scrollbar-button {
      height: 0px;
      width: 0px;
    }

    ::-webkit-scrollbar-corner {
      background: transparent;
    }

    ::-webkit-scrollbar-thumb {
      background: blueviolet;
      border: 0px none blueviolet;
      border-radius: 50px;
    }

    ::-webkit-scrollbar-thumb:hover {
      background: blueviolet;
      filter: grayscale(50%);
    }

    ::-webkit-scrollbar-thumb:active {
      background: blueviolet;
    }

    ::-webkit-scrollbar-track {
      background: #013F52;
      border: 0px none #013F52;
      border-radius: 50px;
    }

    ::-webkit-scrollbar-track:hover {
        background: #013F52;
    }

    ::-webkit-scrollbar-track:active {
        background: #013F52;
    }

    @media screen and (min-height: 480px) and (max-height: 720px){
        #edit{
            margin-top: 0;
        }
    }

    @media screen and (min-height: 720px) and (max-height: 1080px){
        #edit{
            margin-top: 80px;
        }
    }

    @media screen and (min-height: 1080px) and (max-height: 2160px){
        #edit{
            margin-top: 120px;
        }
    }

    @media screen and (min-width: 1920px) and (max-width: 3840px){
        .sideBar ul li{
            font-size: 30px;
        }

        svg{
            height: 70px;
            width: 70px;
        }
    }
    
    @media screen and (min-height: 2160px) and (max-height: 4320px){
        #edit{
            margin-top: 500px;
        }
    }

    @media screen and (min-width: 3840px) and (max-width: 7680px){
        .sideBar ul li{
            font-size: 50px;
        }

        svg{
            height: 130px;
            width: 130px;
        }
    }

    
</style>