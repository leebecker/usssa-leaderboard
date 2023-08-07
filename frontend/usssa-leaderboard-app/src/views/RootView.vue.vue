<template>
  <LeaderBoardList :enable-admin="false"/>
</template>

<script>
// @ is an alias to /src
import LeaderBoardList from '@/components/LeaderBoardList.vue'

export default {
  name: 'RootView',
  components: {
    LeaderBoardList
  },
  data() {
    return {
    }
  }
}
</script>
