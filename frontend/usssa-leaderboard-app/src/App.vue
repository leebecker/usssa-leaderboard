<template>
  <!--<img alt="Vue logo" src="./assets/logo.png">-->
  <LeaderBoardTable
    slug="t5-championship-2023"
  />

</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import LeaderBoardTable from './components/LeaderBoardTable.vue'

export default {
  name: 'App',
  components: {
    LeaderBoardTable,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
