var app = new Vue({
    el: '#app',
    
    data: {
    	timedate:[],
        dates: [],
    },
    
    methods:{
        clickHandler:  function(){
        	axios.get('./api/datetime/')
                .then(response => {
                    this.timedate = response.data
                })
                .catch(err => {
                    console.error(err)
                })
        }
    },

    created: function(){
        axios.get('/api/')
            .then(response => {
                this.dates = response.data
            })
            .catch(err => {
                console.error(err)
            })
    }
})