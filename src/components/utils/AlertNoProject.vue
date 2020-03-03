<template>
    <div>
        <v-alert type="info" class="alert">
            <router-link to="/Home" tag="button">
                Are you lost ?<br />
                You didn't choose a project
            </router-link>    
        </v-alert>
        <h3>If you want to create a project: Go to Home !</h3>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    .alert{
        width: 350px;
        font-size: 20px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);     
    }

    h3{
        color: #2196f3;
        position: absolute;
        top: 60%;
        left: 50%;
        transform: translate(-50%, -50%);

    }
</style>