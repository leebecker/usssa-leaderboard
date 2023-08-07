<template>
  <div class="about">
    <h1>Leaderboard Admin</h1>
  </div>
  <AdminUpdateForm
    slug="t5-championship-2023"
  />
</template>
<script>
// @ is an alias to /src
import AdminUpdateForm from '@/components/AdminUpdateForm.vue'

export default {
  name: 'HomeView',
  components: {
    AdminUpdateForm
  }
}
</script>
