<template>
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink v-if="showAdmin" :to="adminPath">Admin</RouterLink> |
    <a @click="authStore.logout()" class="nav-item nav-link">Logout</a>
  </nav>
  <RouterView/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.RouterLink-exact-active {
  color: #42b983;
}

</style>

<script>
import { useAuthStore } from '@/stores';



export default {
  data() {
    // modify .env.development.local or .env to update this value
    var showAdmin = JSON.parse(process.env.VUE_APP_LEADERBOARD_SHOW_ADMIN_ACCESS);
    var adminObfuscationSuffix = process.env.VUE_APP_LEADERBOARD_ADMIN_OBFUSCATION_SUFFIX;
    const authStore = useAuthStore();
    return {
      authStore: authStore,
      showAdmin: showAdmin,
      adminObfuscationSuffix: adminObfuscationSuffix,
      adminPath: `/admin-${adminObfuscationSuffix}`
    }
  }

}
</script>
