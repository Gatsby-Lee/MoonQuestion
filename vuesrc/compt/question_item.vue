import Vue from 'vue';

Vue.component('question-item', {
    props: ['question'],
    template: '<li>{{ question[1] }}</li>'
})
