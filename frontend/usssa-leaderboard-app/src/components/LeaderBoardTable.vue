<template>
    {{ columns[columnSortIdx] }} {{ cycleColumns }}
    <h1>{{ leaderboard.name }} </h1>

    <label for="cycleColumns">Cycle Columns</label>
    <input type="checkbox" v-model="cycleColumns" name="cycleColumns" />
    <div class="leaderboard">
      <div class="divTable">
        <div class="divTableHeadRow">
          <div class="divTableHead">
            <span class="fullTitle">Rank 🔢</span>
            <span class="abbrTitle">🔢</span>
          </div>
          <div class="divTableHead">Contingent 👥</div>
          <div class="divTableHead">
            <span class="fullTitle">Country 🌎</span>
            <span class="abbrTitle">🌎</span>
          </div>
          <div class="divTableHeadGold">
            <span class="fullTitle">Gold</span>
            <span class="abbrTitle">G</span>
          </div>
          <div class="divTableHeadSilver">
            <span class="fullTitle">Silver</span>
            <span class="abbrTitle">S</span>
          </div>
          <div class="divTableHeadBronze">
            <span class="fullTitle">Bronze</span>
            <span class="abbrTitle">B</span>
          </div>
          <div class="divTableHead">
            <span class="fullTitle">Medal Count 🏅</span>
            <span class="abbrTitle">🏅</span>
          </div>
          <div class="divTableHead">
            <span class="fullTitle">Total Points 🏆</span>
            <span class="abbrTitle">🏆</span>
          </div>
        </div>
        <div class="divTableBody">
            <LeaderboardTableRow v-for="(standing, index) in leaderboardEntries" 
            :key="standing.contingent_id"
            :rowIndex="index"
            :standing="standing"
            :contingent="leaderboard.idToContingent[standing.contingent_id]" />
        </div>
      </div>

        <!-- <div class="divLogo">
          <img :src="require(`@/assets/T5-chalice-logo-large.png`)"/>
        </div> -->
      </div>

    <div>
      <h3>Reporting {{ leaderboard.category_results.length}} / {{ totalEventCategories }} categories. </h3>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import _ from 'lodash';
  import LeaderboardTableRow from './LeaderboardTableRow.vue'

  export default {
    name: 'LeaderBoardTable',
    props: {
        slug: String
    },
    data() {
        return {
            // initialize to an empty list
            cycleColumns: true,
            leaderboard: {
              contingents: [],
              standings: [],
              categories: [],
              category_results: [],
              idToContingent: []
            },
            columns: [
              {name:'rank', order: 'asc'},
              {name:'gold', order: 'desc'},
              {name:'silver', order: 'desc'},
              {name:'bronze', order: 'desc'},
              {name:'medals', order: 'desc'},
              {name:'points', order: 'desc'},
            ],
            columnSortIdx: 0
        };
    },
    methods: {
        async getLeaderBoard() {
            var service_url = process.env.VUE_APP_LEADERBOARD_API_URL;
            console.log("TACOS AYAYAYA")
            console.log(service_url)
            console.log(`${service_url}/leaderboards/${this.slug}`)
            await axios.get(`${service_url}/leaderboards/${this.slug}`).then(response => {
                this.leaderboard = response.data;
                if (this.leaderboard.categories == null) {
                  this.leaderboard.categories = []
                }
                if (this.leaderboard.category_results == null) {
                  this.leaderboard.category_results = []
                }
                if (this.leaderboard.contingents == null) {
                  this.leaderboard.contingents = []
                }
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
        setInterval(() => {
          // cycle through columns 
          this.columnSortIdx = (this.columnSortIdx + 1) % this.columns.length
        }, 2000);
    },
    components: { LeaderboardTableRow},
    computed: {

      leaderboardEntries() {
        var sortByColumn = this.columns[this.columnSortIdx]

        if (this.cycleColumns) {
          return _.orderBy(this.leaderboard.rankings, (r) => [r[sortByColumn.name]], [sortByColumn.order])
        } else {
          return this.leaderboard.rankings
        }
      },
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
  .leaderboard {
    font-size: large;
    width: 100%;
  }

  .leaderboard:after {
    /*display: flex;
    flex-wrap: wrap;*/
    display: table;
    clear: both;

  }


.divTable {
  float: left;
  width: 100%;
  margin: 2px;
}

.divLogo {
  float: left;
}

.fullTitle {
  display: inline;
}
.abbrTitle {
  display: none;
}
/*
.divTableLeft{
	display: table;
	width: 45%;
  margin: 5px;
}
.divTableRight{
	display: table;
	width: 50%;
  margin: 5px;
}
*/

@media screen and (max-width: 700px) {
    .leaderboard {
      font-size: small;
    }

  .fullTitle {
    display: none;
  }
  .abbrTitle {
    display: inline;
  }
  .divLogo {
    /*transform: scale(0.5, 0.5);
    flex-wrap: wrap;*/
    display: none;

  }
}

@media screen and (max-width: 1440px) {
    .leaderboard {
      font-size: small;
    }
    .divTable {
      width: 100%;
    }
    .divLogo {
      width: 100%;
    }
    
    #secondHeader, #secondGold, #secondSilver, #secondBronze{
      opacity: 0.0;
      color: #FFFFFF;
      background-color: #FFFFFF;
      height: 5px;
    }
}

@media screen and (max-width: 1200px) {
    .leaderboard {
      font-size: medium;
    }
    /*
    .divTable {
      width: 100%;
    }
    */
    
    #secondHeader, #secondGold, #secondSilver, #secondBronze{
      opacity: 0.0;
      color: #FFFFFF;
      background-color: #FFFFFF;
      height: 5px;
    }
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
  vertical-align: top;
}

.divTableHeadContingent {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  vertical-align: top;
  text-align: left;
}

.divTableHeadGold {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  color: #000000;
  background-color: #D4AF37;
  vertical-align: top;
}

.divTableHeadSilver {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  color: #000000;
  background-color: #C0C0C0;
  vertical-align: top;
}

.divTableHeadBronze {
	border: 1px solid #999999;
	display: table-cell;
	padding: 3px 10px;
  color: #000000;
  background-color: #B08D57;
  vertical-align: top;
}
.divTableBody {
	display: table-row-group;
}
  </style>
  