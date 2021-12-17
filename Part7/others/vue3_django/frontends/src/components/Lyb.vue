<template>
<div class="row">
  <div class="col-md-8">
    <table class="table table-bordered">
      <thead>
        <tr>
          <th>标题</th>
          <th>作者</th>
          <th>内容</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in ly_list" :key="item.url">
          <td>{{ item.title }}</td>
          <td>{{ item.author }}</td>
          <td>{{ item.content }}</td>
          <td>
            <button class = "btn btn-success" title="编辑">
              <i class="glyphicon glyphicon-pencil"></i>
            </button>
            <button class = "btn btn-danger" title="删除">
              <i class="glyphicon glyphicon-trash"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <div class="col-md-4"></div>
</div>
</template>

<script>

import {axios} from 'axios'
import {reactive,onMounted,toRefs} from 'vue'
export default {
  name: 'Lyb',
  setup(){
    let base_url = 'http://127.0.0.1:8000/api/lyb/';
    const state = reactive({
      ly_list:[],
    })
    const getLyb = ()=>{
      axios.get(base_url).then(res=> {
        state.ly_list = res.data;
      }).catch(err=>{
        console.log(err);
      })
    }

    onMounted(()=>{
       getLyb();
    })

    return{
      ...toRefs(state)
    }
  }
}
</script>
