<template>
    <h1>{{ leaderboard.name }} </h1>
    <div class="leaderboard">
      <div class="div-table">
        <div class="divTableHeadRow">
          <div class="divTableHead">Rank</div>
          <div class="divTableHead">Contingent</div>
          <div class="divTableHead" color->Country</div>
          <div class="divTableHeadGold">Gold</div>
          <div class="divTableHeadSilver">Silver</div>
          <div class="divTableHeadBronze">Bronze</div>
          <div class="divTableHead">Total Points</div>
        </div>
          <div class="divTableBody">
            <LeaderboardTableRow v-for="(standing, index) in leaderboard.rankings" 
            :key="standing.contingent_id"
            :rowIndex="index"
            :standing="standing"
            :contingent="leaderboard.idToContingent[standing.contingent_id]" />
          </div>
        </div>
      <h3>Reporting {{ leaderboard.category_results.length}} / {{ totalEventCategories }} categories. </h3>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import LeaderboardTableRow from './LeaderboardTableRow.vue'

  export default {
    name: 'LeaderBoardTable',
    props: {
        slug: String
    },
    data() {
        return {
            // initialize to an empty list
            leaderboard: {
              contingents: [],
              standings: [],
              categories: [],
              category_results: []
            }
        };
    },
    methods: {
        async getLeaderBoard() {
            await axios.get(`http://127.0.0.1:8000/leaderboards/${this.slug}`).then(response => {
                this.leaderboard = response.data;
                this.leaderboard.idToContingent = Object.fromEntries(
                  this.leaderboard.contingents.map(c => [c.id, c])
                );
                console.log(this.leaderboard)
                return response.data;
            });
        }
    },
    async created() {
        await this.getLeaderBoard();
        //console.log(this.leaderboard.contingents)
        console.log(this.leaderboard);
    },
    components: { LeaderboardTableRow},
    computed: {
      totalEventCategories() {
        // Compute total number of event categories by
        // summing all combinations of (event, class, gender)
        var totalEvents = 0;
        this.leaderboard.categories.forEach(categoryDef => {
          var c = 1;
          Object.entries(categoryDef).forEach(categoryProp => {
            c *= categoryProp.length;
          })
          totalEvents += c
        });
        return totalEvents;
      }

    }
}
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }

  .div-table{
	display: table;
	width: 90%;
}

.divTableHeadRow {
	background-color: #00007F;
	display: table-header-group;
	font-weight: bold;
  color: #FFFFFF;
}

.divTableHead {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  font-size: x-large;
  vertical-align: middle;
}

.divTableHeadGold {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  color: #000000;
  background-color: #D4AF37;
  font-size: x-large;
  vertical-align: middle;
}

.divTableHeadSilver {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  color: #000000;
  background-color: #C0C0C0;
  font-size: x-large;
  vertical-align: middle;
}

.divTableHeadBronze {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  color: #000000;
  background-color: #B08D57;
  font-size: x-large;
  vertical-align: middle;
}
.divTableBody {
	display: table-row-group;
}
  </style>
  