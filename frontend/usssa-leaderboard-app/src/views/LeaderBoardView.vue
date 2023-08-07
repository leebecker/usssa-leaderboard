<template>
  <LeaderBoardTable
    :slug="leaderboard_slug"
  />
</template>

<script>
// @ is an alias to /src
import LeaderBoardTable from '@/components/LeaderBoardTable.vue'

export default {
  name: 'LeaderBoardView',
  components: {
    LeaderBoardTable
  },
  data() {
    return {
      leaderboard_slug: this.$route.params.slug
    }
  }
}
</script>
