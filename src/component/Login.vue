<template>
    <div id="login" class="d-flex justify-content-center mt-4">
        <div class="card w-50">
        <div class="card-header">
            <h1 class="text-center">Login</h1>
        </div>
        <div class="card-body">
            <form @submit.prevent="login">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" v-model="username" class="form-control" id="username">
                    <small class="text-danger">{{err_username}}</small>
                </div>
                <div class="form-group">
                    <label for="password">password</label>
                    <input type="password" v-model="password" class="form-control" id="password"> 
                    <small class="text-danger">{{err_password}}</small> 
                </div>
                <button type="submit" class="btn btn-primary">Login</button>
            </form>
        </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
    export default{ 
        name: 'Login',
        data(){ 
             return { 
                 username: null, 
                 password: null, 
                 err_username: null, 
                 err_password: null
             }
            },
        methods : { 
            login(e){ 
            axios.post('/api/token', {
                    username: this.username, 
                    password: this.password
                }).then(data => {
                    const data2 = data.data
                    localStorage.setItem('token', data2.access)
                    location.href = '?all'

                }).catch(err => {
                        e.preventDefault()
                        const data = err.response.data
                        if(data.username) this.err_username = data.username[0];
                        if(data.password) this.err_password= data.password[0];

                }) 
        }
        }
         
    }
</script>