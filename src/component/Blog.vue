<template> 
    <div id="App">
        <div v-if="error.msg">
            {{error.msg}}
        </div>
        <div v-else>
            <div v-for="row in info" class="row">
                    <div class="col-4">
                        <div class="card">
                            <div class="card-body shadow-lg">
                                <h1>{{row.title}}</h1>
                            <p>{{row.content_text}}</p>
                            </div>
                        </div>
                    </div>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios'
     export default { 
         name: "Blog",
         data(){ 
             return { 
                 info: {},
                 search: window.location.search, 
                 error: {}, 
             }
         },
         mounted(){ 
                 const slug = this.search.replace('?=', '')
                 if(this.search == '') { 
                     axios.get('/api-blog').then(data =>{ 
                      this.info = data.data
                     })
                 }else{ 
                     axios.get(`/api-blog/${slug}/`).
                     then(response => (this.info = [response.data]))
                     .catch(error =>(this.error = error.response.data))
                 }
         }
     }
</script>
