<template>
  <div>
    <h3>{{leaderboard_slug}} Admin</h3>
  </div>
  <AdminNavigationEditEvents
    :slug="leaderboard_slug"
  />
</template>
<script>
// @ is an alias to /src
import AdminNavigationEditEvents from '@/components/AdminNavigationEditEvents.vue'

export default {
  name: 'AdminEventView',
  components: {
    AdminNavigationEditEvents
  },
  data() {
    return {
      leaderboard_slug: this.$route.params.slug
    }
  }
}
</script>
