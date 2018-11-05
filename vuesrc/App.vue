// Root Component
<template>

<div class="input-group mb-3">
  <div class="input-group-append">
    <button class="btn btn-outline-secondary" type="button">New</button>
  </div>
  <input type="text" class="form-control" placeholder="Question" aria-label="Recipient's username" aria-describedby="basic-addon2">

  <div>
    <ul>
    <question-item v-for="item in questions" v-bind:question="item" v-bind:key="item.id">
    </question-item>
    </ul>
  </div>
</div>

</template>
