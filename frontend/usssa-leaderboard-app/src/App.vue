<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link v-if="showAdmin" :to="adminPath">Admin</router-link>
  </nav>
  <router-view/>
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

nav a.router-link-exact-active {
  color: #42b983;
}

</style>

<script>

export default {
  data() {
    // modify .env.development.local or .env to update this value
    var showAdmin = JSON.parse(process.env.VUE_APP_LEADERBOARD_SHOW_ADMIN_ACCESS);
    var adminObfuscationSuffix = process.env.VUE_APP_LEADERBOARD_ADMIN_OBFUSCATION_SUFFIX;
    return {
      showAdmin: showAdmin,
      adminObfuscationSuffix: adminObfuscationSuffix,
      adminPath: `/admin-${adminObfuscationSuffix}`
    }
  }

}
</script>
