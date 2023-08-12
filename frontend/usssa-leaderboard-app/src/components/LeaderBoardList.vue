<template>
    <div class="leaderboardList">
        <table>
            <thead>
                <tr><th>Event</th><th>Links</th><th></th></tr>
            </thead>
            <tbody>
        <tr v-for="leaderboard in leaderboards" :key="leaderboard.slug">
            <td>{{ leaderboard.description }}</td>
            <td>
                <router-link :to="{ name: 'leaderboard', params: { slug: leaderboard.slug }}">
                    📶
                </router-link>

            </td>
            <td>
                <span v-if="enableAdmin">
                    <router-link :to="{ name: 'adminEvent', params: { slug: leaderboard.slug }}">
                    ⚒️
                    </router-link>
                </span>
                <span v-else>

                </span>
            </td>
        </tr>
            </tbody>
        </table>
    </div>

    

</template>



<script>
  import axios from 'axios'
  //import LeaderboardTableRow from './LeaderboardTableRow.vue'

  export default {
    name: 'LeaderBoardList',
    props: {
        enableAdmin: Boolean
    },
    data() {
        return {
            // initialize to an empty list
            leaderboards: [],
        };
    },
    methods: {
        async getLeaderBoards() {
            var api_url = process.env.VUE_APP_LEADERBOARD_API_URL
            await axios.get(`${api_url}/leaderboards`).then(response => {
                this.leaderboards = response.data.leaderboards;
                console.log(this.leaderboard)
                return response.data;
            });
        }
    },
    async created() {
        await this.getLeaderBoards();
        //console.log(this.leaderboard.contingents)
        console.log(this.leaderboards);
    },
    components: { },
    computed: {
    }
}
</script>

<style scoped>
.leaderboardList {
    text-align: left;

}
.leaderboardList td {
    padding: 10px;
}
</style>