<template>
<div>

<v-container fluid>
    
    <div v-if="isDisabled">
        <v-alert type="info" class="alert">
            <router-link to="/Home" tag="button">
                Are you lost ?<br/>
                You didn't choose a project
            </router-link>
        </v-alert>
        <h3>If you want to create a project: Go to Home !</h3>
    </div>

</v-container>

</div>
</template>

<script>
export default {
    data(){
        return{
            isDisabled: true
        }
    }
}
</script>

<style scoped>

    .alert{
        margin-top: 25%;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        width: 350px;
        font-size: 20px;
    }

    h3{
        text-align: center;
        color: #2196f3;
    }

    h3:hover{
        text-decoration: underline;
    }

</style>
