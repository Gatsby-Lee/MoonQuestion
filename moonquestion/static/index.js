console.log('My index.js')

Vue.component('question-item', {
    props: ['question'],
    template: '<li>{{ question[1] }}</li>'
})

var app = new Vue({
    el: '#app',
    data: {
        questions: []
    },
    mounted: function () {
        this.get_questions();
    },
    methods: {
        get_questions: function (resource) {
            this.$http.get('/q/')
                .then((response) => {
                    this.questions = response.data['qlist'];
                })
                .catch((err) => {
                    console.error('failed');
                })
        },
    },
})
