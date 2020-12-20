<template> 
    <div id="App" class="container-fluid">
        <div v-if="search == '?create'">
            <Add></Add>
        </div>
        <div v-if="search == '?all'">
            <All></All>
        </div>
        <div v-if="search == '?login'">
            <Login></Login>
        </div>
        <div v-if="edit">
            <Edit></Edit>
        </div>
        <div v-else>
             <Blog></Blog>
        </div>
        </div>
    </template>
    <script>
        import Edit from "./Edit.vue"
        import Blog from "./Blog.vue"
        import Add from './Add.vue'
        import All from './All.vue'
        import Login from './Login.vue'
        import axios from 'axios'
        export default { 
            name: "App",
            data(){ 
                return { 
                    search: window.location.search, 
                    edit: null
                }
            },
             mounted() {
                 const del = this.search.replace('?delete=', '')
                 const patt = /delete/i
                 const result = this.search.match(patt)
                 const edit =  /edit/i
                 this.edit = this.search.match(edit)
                 

                   const token = localStorage.getItem('token')
                 if(result){ 
                     axios.delete('/api/'+del, {headers: { 'Authorization': 'Bearer ' + token }})
                     .then(response =>{ 
                         alert(response.data.msg)
                         location.href = '?all'
                     }).catch(err => [ 

                     ])
                 }
             },
               components: { Edit, Blog,Add,  All, Login},
        }
    </script>



