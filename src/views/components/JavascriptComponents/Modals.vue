<template>
    <!-- Modals -->
        <div class="input-group-append">
            <a id="query" type="primary" class=" mb-3" @click="modals.modal1 = true" style="color: #1fa2ff;cursor: pointer">
                More
            </a>
            <modal :show.sync="modals.modal1">
              <div v-highlight>
                Command: <code v-highlight style="color: #bd081c;font-size: 15px">{{ data1["Command"] }}<br /></code>
                MP Summary: <span style="color: #28a745">{{ data1["MP Summary"] }}<br /></span>
                Most Similar TLDR Task-Script Pair: <span style="color: #28a745">{{ data1["Most Similar TLDR Task"] }}<br /></span>
                <pre><code v-highlight class="bsah">{{ data1["Most Similar TLDR Script"] }}<br /></code></pre>
                <span style="font-size: 16px;font-weight: bold">## Top-3 Similar Questions with the Accepted Scripts ##</span>
                <br />
                <div v-for="(a, index) in data1['Top-3 Similar Questions']" :key="index">
                  Question: <a @click="getUrl1(a.split(':')[0])" style="cursor: pointer;color: #1da1f2"><code>{{a.split(':')[1]}}<br /></code></a>
                    <pre v-highlight><code class="bash">{{data1['Top-3 Scripts'][index].slice(data1['Top-3 Scripts'][index].indexOf(":")+1).replace(' ', '')}}<br /></code></pre>
                </div>
                <span style="font-weight: bold;font-size: 16px">## Explanations about Options ##<br /></span>
                <div v-for="(value, key, index) in data1['Explanations about Options']" :key="index">
                  <code>{{key}}: </code>
                  <span>{{value}}<br /></span>
                </div>
              </div>
                <template slot="footer">
                    <base-button type="link" class="ml-auto" @click="modals.modal1 = false">Close
                    </base-button>
                </template>
            </modal>
        </div>
</template>
<script>
import Modal from "@/components/Modal.vue";
export default {
  props: ['data1'],
  components: {
    Modal
  },
  data() {
    return {
      queryUrl_dict1 : {"ul":"https://unix.stackexchange.com/questions/","so":"https://stackoverflow.com/questions/","su":"https://superuser.com/questions/","au":"https://askubuntu.com/questions/"},
      modals: {
        modal1: false,
        modal2: false,
        modal3: false
      },
      url : 'www.baidu.com'
    }
  },
  methods:{
     getUrl1: function (e) {
       e = e.split("_")
       window.open(this.queryUrl_dict1[e[0]] + e[1] + "/")
     },
    abc : function (){
       console.log(this.url)
    }
   }
};
</script>
<style>
</style>
