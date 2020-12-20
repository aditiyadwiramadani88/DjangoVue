<template>
<div id="add" class="mt-4">
    <div class="card">
        <div class="card-header">
            Add Data 
        </div>
        <div class="card-body">
            
            <form @submit.prevent="create" method="POST">
                <div class="form-group">
                    <input type="text" v-model="title" class="form-control">
                    <small class="text-danger">{{title_error}}</small>
                </div>
                <div class="form-group">
                    <textarea v-model="content_text" class="form-control"></textarea>
                    <small class="text-danger">{{text_error}}</small>
                </div>
                <button type="submit" class="btn btn-primary">Add Article</button>
            </form>
        </div>
    </div>
    </div>
</template>
<script>
    import axios from 'axios'
export default { 
    name: "Add",
    data(){ 
        return { 
            title: null, 
            content_text: null, 
            title_error: null, 
            text_error: null,
        }
    }, 
    methods: {
        create(e){
            const token = localStorage.getItem('token')
           axios({
                method: 'post',
                url: '/api',
                data: {title: this.title, content_text: this.content_text},
             headers: { 'Authorization': 'Bearer ' +token}
            }).then(response => { 
                alert('sucess create Article')
                location.href = '?all'
            }).catch(response => { 
                  e.preventDefault()
                  const data =  response.response.data
                  if(data.title) this.title_error = data.title[0];                  
                   if(data.content_text) this.text_error = data.content_text[0];
                   if (data.detail) location.href = '?login';
                
            })
        }
    }
}
</script>