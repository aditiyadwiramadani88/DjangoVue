<template>
    <div id="All">
        <a href="?create" class="btn btn-primary mt-2 mb-2">Add Article</a>
         <table class="table table bordered">
             <tr>
                 <th>Title</th>
                 <th colspan="3" class="text-center">Action</th>
             </tr>
             <tr  v-for="row in info">
                <td>{{row.title}}</td>
                <td><a v-bind:href="'?='+row.slug" class="btn btn-primary">View</a></td>
                <td><a v-bind:href="'?edit='+row.id" class="btn btn-primary">Edit</a></td>
                <td><a v-bind:href="'?delete='+row.id" class="btn btn-danger">Delete</a></td>
             </tr>
         </table>
    </div>
</template>
<script>
    import axios from 'axios'
        export default {
            name: "All",
            data() {
                return {
                    info: {},
                }
            },
            mounted() {
                const token = localStorage.getItem('token')
                    axios.get('/api', { headers: {'Authorization': 'Bearer '+token}}).then(data => {
                        this.info = data.data
                    }).catch(err => { 
                       if(err.response.data.detail) location.href = '?login';
                    })
            }
        }
</script>