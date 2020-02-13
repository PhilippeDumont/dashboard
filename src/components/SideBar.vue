<template>
    <v-container>
        <div class="sideBar">
                <ul>
                    <li v-for="item in items"
                        :key="item.title"
                        class="item">
                        <div>
                            <v-icon color="white" size="50">{{ item.icon }}</v-icon>
                            <br/>
                            {{ item.title }}
                        </div>
                    </li>
                    <li id="edit" class="item">
                        <v-icon color="white" size="50">mdi-pencil</v-icon>
                        <br />
                        Edit
                    </li>
                    <li class="item">
                        <v-icon color="white" size="50">mdi-settings</v-icon>
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
                items: [
                    { title: 'Home', icon: 'mdi-home' },
                    //{ title: 'Create a project', icon: 'mdi-plus' },
                    { title: 'Level 1', icon: 'mdi-poll' },
                    { title: 'Level 2', icon: 'mdi-cube-outline' },
                    { title: 'Level 3', icon: 'mdi-account' },
                    { title: 'Level 4', icon: 'mdi-help-box' },
                ],
            }
        },
    }
</script>


<style scoped>
    #edit{
        margin-top: 190px;
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
        min-width: 100px;
        overflow: auto;
        position: fixed;
        top: 0;
        width: 100px;
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

    @media screen and (max-height: 760px){
        #edit{
            margin-top: 0;
        }
    }
</style>