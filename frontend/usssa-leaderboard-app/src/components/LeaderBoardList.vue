<template>

    <div class="leaderboardList">
        <table>
            <thead>
                <tr>
                    <th>Event</th>
                    <th>Leaderboards</th>
                    <th>Event Results</th>
                </tr>
            </thead>
            <tbody>
        <tr v-for="leaderboard, i in leaderboards" :key="leaderboard.slug" :class="{even: i % 2 == 0}">
            <td class="eventCol">{{ leaderboard.description }}</td>
            <td>
                <router-link :to="{ name: 'leaderboard', params: { slug: leaderboard.slug }}">
                    🏆
                </router-link>
            </td>
            <td>
                <router-link :to="{ name: 'leaderboard', params: { slug: leaderboard.slug }}">
                    🥇🥈🥉
                </router-link>
            </td>
            <td v-if="enableAdmin">
                <span>
                    <router-link :to="{ name: 'adminEvent', params: { slug: leaderboard.slug }}">
                    ⚒️
                    </router-link>
                </span>
            </td>
        </tr>
            </tbody>
        </table>
    </div>

    

</template>



<script>
  import axios from 'axios'

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
                return response.data;
            });
        },
        rotateLeaderboardSortKey() {
            this.columnSortIdx = (this.columnSortIdx + 1) % this.columns.length
        }
    },
    async created() {
        await this.getLeaderBoards();
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

table {


}

thead {
    background-color: darkblue;
    color: white;

}

tbody tr {
    background-color: #E0E0E0;

}

th, td {
    padding: 10px;
    text-align: center; 
    margin: auto;
}



.even {
    background-color: white;

}

.eventCol {
    text-align: left;
    margin: none;
}



</style>