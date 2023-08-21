<template>
    <h1>{{ leaderboard.description }} </h1>

    <div class="leaderboard">
      <div id="tableWrapper">
        <div id="table1">
          <table>
            <colgroup>
              <col v-for="column in columns" :key="column.name" 
                :class="(column.name == sortByColumn.name) ? 'highlightedColumn' : 'unhighlightedColumn'">
            </colgroup>
            <thead id="table1Header">
              <tr v-if="!isSingleTable" id="table1Header1">
                <th colspan=8>Top {{leaderboardEntriesTop.length}}</th>
              </tr>
              <tr id="table1Header2">
                <th v-for="column in columns" :key="column.name" :class="column.name" ref="table1Columns">
                  <div @click="setSortByColumn(column)" :class="{clickSortHeader: isSortableColumn(column.name)}">
                  <span class="fullTitle" :title="column.text" >{{column.text}}
                    <span v-if="(column.name == sortByColumn.name) && (column.order === 'desc')">🔻</span>
                    <span v-else-if="(column.name == sortByColumn.name) && (column.order === 'asc')">🔺</span>
                  </span>
                  <span class="abbrTitle" :title="column.text">{{column.abbr}}
                    <span v-if="(column.name == sortByColumn.name) && (column.order === 'desc')">🔻</span>
                    <span v-else-if="(column.name == sortByColumn.name) && (column.order === 'asc')">🔺</span>
                  </span>
                  </div>
                </th>
              </tr>
            </thead>
            <tbody id="table1Body">
              <tr
              v-for="(entry, index) in leaderboardEntriesTop"
              :key="index"
              :class="{even: index % 2 == 1}">
                <td :class="highlightColumnClass['rank']">{{entry.rank}}</td>
                <td class="contingent" :title="entry.contingent.name">{{entry.contingent.name}}</td>
                <td>
                    <img v-if="entry.isValidCountry" :src="require(`@/assets/flags/84x63/${entry.countryCodeLower}.png`)" :alt="entry.countryCode" class="fullImg">
                    <span v-else class="fullImg"> -- </span>
                    <img v-if="entry.isValidCountry" :src="require(`@/assets/flags/84x63/${entry.countryCodeLower}.png`)" :alt="entry.countryCode" class="smallImg">
                    <span v-else class="smallImg"> -- </span>
                </td>
                <td :class="highlightColumnClass['gold']">{{entry.gold}}</td>
                <td :class="highlightColumnClass['silver']">{{entry.silver}}</td>
                <td :class="highlightColumnClass['bronze']">{{entry.bronze}}</td>
                <td :class="highlightColumnClass['medals']">{{entry.medals}}</td>
                <td :class="highlightColumnClass['points']">{{entry.points}}</td>
            </tr>
          </tbody>
          <tfoot v-if="isSingleTable" id="table1Footer" class="tableFoot">
            <tr>
              <td colspan="3" style="background-color: lightslategrey; color: white">
                Totals {{ leaderboard.category_results.length}} / {{ totalEventCategories }} categories reported:
              </td>
              <td>
                {{ totals.gold}}
              </td>
              <td>
                {{ totals.silver}}
              </td>
              <td>
                {{ totals.bronze}}
              </td>
              <td>
                {{ totals.medals}}
              </td>
              <td>
                {{ totals.points}}
              </td>
            </tr>
          </tfoot>
          </table>
        </div>

        <div v-if="!isSingleTable" id="table2">
          <table>
            <colgroup>
              <col v-for="column in columns" :key="column.name" 
                :class="(cycleColumns && (column.name == sortByColumn.name)) ? 'highlightedColumn' : 'unhighlightedColumn'">
            </colgroup>
            <thead id="table2Header">
              <tr id="table2Header1">
                <th colspan=8>Remaining {{leaderboardEntriesBottom.length}}</th>
              </tr>
              <tr id="table2Header2">
                <th v-for="column in columns" :key="column.name" :class="column.name">
                  <div @click="setSortByColumn(column)" :class="{clickSortHeader: isSortableColumn(column.name)}">
                    <span class="fullTitle" :title="column.text">{{column.text}} 
                      <span v-if="(column.name == sortByColumn.name) && (column.order === 'desc')">🔻</span>
                      <span v-else-if="(column.name == sortByColumn.name) && (column.order === 'asc')">🔺</span>
                    </span>
                    <span class="abbrTitle" :title="column.text">{{column.abbr}} 
                      <span v-if="(column.name == sortByColumn.name) && (column.order === 'desc')">🔻</span>
                      <span v-else-if="(column.name == sortByColumn.name) && (column.order === 'asc')">🔺</span>
                    </span>
                  </div>
                </th>
              </tr>
            </thead>
            <tbody v-if="!isSingleTable" id="table2Body">
              <tr
              v-for="(entry, index) in leaderboardEntriesBottom"
              :key="index"
              :class="{even: index % 2 == 1}">
                <td :class="highlightColumnClass['rank']">{{entry.rank}}</td>
                <td class="contingent">{{entry.contingent.name}}</td>
                <td>
                    <img v-if="entry.isValidCountry" :src="require(`@/assets/flags/84x63/${entry.countryCodeLower}.png`)" :alt="entry.countryCode" class="fullImg">
                    <span v-else class="fullImg"> -- </span>
                    <img v-if="entry.isValidCountry" :src="require(`@/assets/flags/84x63/${entry.countryCodeLower}.png`)" :alt="entry.countryCode" class="smallImg">
                    <span v-else class="smallImg"> -- </span>
                </td>
                <td :class="highlightColumnClass['gold']">{{entry.gold}}</td>
                <td :class="highlightColumnClass['silver']">{{entry.silver}}</td>
                <td :class="highlightColumnClass['bronze']">{{entry.bronze}}</td>
                <td :class="highlightColumnClass['medals']">{{entry.medals}}</td>
                <td :class="highlightColumnClass['points']">{{entry.points}}</td>
            </tr>
          </tbody>
          <tfoot class="tableFoot">
            <tr>
              <td colspan="3" style="background-color: lightslategrey; color: white">
                Totals {{ leaderboard.category_results.length}} / {{ totalEventCategories }} categories reported:
              </td>
              <td>
                {{ totals.gold}}
              </td>
              <td>
                {{ totals.silver}}
              </td>
              <td>
                {{ totals.bronze}}
              </td>
              <td>
                {{ totals.medals}}
              </td>
              <td>
                {{ totals.points}}
              </td>
            </tr>
          </tfoot>
          </table>
        </div>


      </div>

      <div id="controls">
        <label for="cycleColumns">Auto-cycle sort columns</label>
        <input type="checkbox" v-model="cycleColumns" name="cycleColumns" />
      </div>

        <!-- <div class="divLogo">
          <img :src="require(`@/assets/T5-chalice-logo-large.png`)"/>
        </div> -->
      </div>

  </template>
  
  <script>
  import _ from 'lodash';
  import { useLeaderboardsStore } from '@/stores'

  const leaderboardsStore = useLeaderboardsStore()

  class LeaderboardEntry {
    constructor(ranking, leaderboard) {
      this.contingent = leaderboard.idToContingent[ranking.contingent_id];
      this.rank = ranking.rank;
      this.gold = ranking.gold;
      this.silver = ranking.silver;
      this.bronze = ranking.bronze;
      this.medals = ranking.medals;
      this.points = ranking.points;
    }

    get ['countryCode']() {
          return this.contingent.country;
    }

    get ['countryCodeLower']() {
          return this.countryCode.toLowerCase();
    }

    get ['isValidCountry']() {
          return this.contingent.is_national_federation
    }

    get ['isEvenRow']() {
          return this.rowIndex % 2 == 0;
    }
  }

  export default {
    name: 'LeaderBoardTable',
    props: {
        slug: String
    },
    data() {
        const isSingleTableQuery = window.matchMedia("(max-width: 1024px)")
        return {
            // initialize to an empty list
            cycleColumns: false,
            isSingleTableQuery: isSingleTableQuery,
            isSingleTable: isSingleTableQuery.matches,
            leaderboard: {
              contingents: [],
              standings: [],
              categories: [],
              category_results: [],
              idToContingent: []
            },
            columns: [
              {
                name:'rank', 
                text:'Rank 🔢',
                abbr:'🔢',
                order: 'asc'
              },
              {
                name:'contingent',
                text:'Contingent 👥',
                abbr:'Team 👥',
              },
              {
                name:'country', 
                text:'Country 🌎',
                abbr:'🌎',
              },
              {
                name:'gold', 
                text:'Gold',
                abbr:'G',
                order: 'desc'
              },
              {
                name: 'silver', 
                text: 'Silver',
                abbr: 'S',
                order: 'desc'
              },
              {
                name:'bronze', 
                text:'Bronze',
                abbr:'B',
                order: 'desc'
              },
              {
                name: 'medals', 
                text: 'Medals 🏅',
                abbr: '🏅',
                order: 'desc'
              },
              {
                name:'points',
                text: 'Points 🏆',
                abbr: '🏆',
                order: 'desc'
              }
            ],
            columnSortIdx: 0,
            highlightColumnClass: {
              "rank": "unhighlightedColumn",
              "gold": "unhighlightedColumn",
              "silver": "unhighlightedColumn",
              "bronze": "unhighlightedColumn",
              "medals": "unhighlightedColumn",
              "points": "highlightedColumn",
            }
        };
    },
    methods: {
        async getLeaderBoard() {
            this.leaderboard = await leaderboardsStore.getLeaderboard(this.slug)
        },
        getContingent(entry_id) {
            if (entry_id in this.leaderboard.idToContingent) {
              return this.leaderboard.idToContingent[entry_id]
            } else {
              // FIXME return empty contingent?
              return {

              }
            }
        },
        updateSortColumn() {
          if (this.cycleColumns) {
            this.columnSortIdx = (this.columnSortIdx + 1) % this.sortableColumns.length

            this.sortableColumns.forEach((c) => {
              if (this.sortByColumn.name == c.name) {
                this.highlightColumnClass[c.name] = "highlightedColumn"
              } else {
                this.highlightColumnClass[c.name] = "unhighlightedColumn"
              }
            })
          }
        },
        isSortableColumn(name) {
          return this.sortableColumns.filter((c) => c.name == name).length > 0
        },
        setSortByColumn(column) {
          // Determine which of the sortable columns was clicked
          var newColumnIdx = this.sortableColumns.findIndex(element => element.name === column.name)
          if (newColumnIdx > -1) {
            // click matched column, disable auto-cycle columns
            this.cycleColumns = false
            if (newColumnIdx != this.columnSortIdx) {
              // found update column index
              this.columnSortIdx = newColumnIdx;
            } 

            this.sortableColumns.forEach((c) => {
              if (this.sortByColumn.name == c.name) {
                this.highlightColumnClass[c.name] = "highlightedColumn"
              } else {
                this.highlightColumnClass[c.name] = "unhighlightedColumn"
              }

            })

            // FIXME: not flipping ordering because it messes with the meaning of the table headers
            // Flip order
            // this.sortableColumns[this.columnSortIdx].order = (this.sortByColumn.order === "asc") ? "desc" : "asc"
          }
        },
    },
    async created() {
        await this.getLeaderBoard();

        // Retrieve leaderboard every 10 minutes
        setInterval(async () => {
          await this.getLeaderBoard();
        }, 10*60*1000)


        setInterval(() => {
          // switch sort column every 10 seconds
          this.updateSortColumn();
        }, 10*1000);
    },
    components: { },
    computed: {
      sortByColumn() {
        return this.sortableColumns[this.columnSortIdx];
      },
      sortableColumns() {
        return this.columns.filter((c) => c.order)
      },
      totals() {
        var totalEntry = new LeaderboardEntry(
          {
            contingent_id: "totals",
            rank: 0,
            gold: 0,
            silver: 0,
            bronze: 0,
            medals: 0,
            points: 0,
          }, 
          this.leaderboard
        );

        this.leaderboardEntries.forEach((entry) => {
          this.sortableColumns.forEach((col) => {
            totalEntry[col.name] += entry[col.name];
          })
        })

        return totalEntry;

      },
      leaderboardEntries() {
        var entries = []
        if (this.leaderboard.rankings) {
          entries = this.leaderboard.rankings.map((r) => new LeaderboardEntry(r, this.leaderboard));
        }

        return _.orderBy(entries, (e) => e[this.sortByColumn.name], [this.sortByColumn.order])
      },
      leaderboardEntriesTop() {
        if (this.isSingleTable) {
          return this.leaderboardEntries
        } else {
          var endIdx = Math.round(this.leaderboardEntries.length / 2)
          return this.leaderboardEntries.slice(0, endIdx)
        }
      },
      leaderboardEntriesBottom() {
        if (this.isSingleTable) {
          return []
        } else {
          var endIdx = Math.round(this.leaderboardEntries.length / 2) - this.leaderboardEntries.length;
          return this.leaderboardEntries.slice(endIdx)
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

    },
    mounted() {
        // watch for mobile event value
        this.isSingleTableQuery.addEventListener('change', () => {
          this.isSingleTable = this.isSingleTableQuery.matches
        })
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
  font-size: x-large;
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


table {
  border-collapse: collapse;
  border-radius: 5px;
}

td {

}


thead {
	font-weight: bold;
  color: #FFFFFF;
  background-color: #00007F;
  min-width: 400px;
  /* min-height: 80px;
  max-height: 100px; */
}

#table1, #table2 {
  flex: 1;
  width: 100%;
  justify-content: center;
  margin-left: auto;
  margin-right: auto;
  padding: 0px;
  vertical-align: top;
}

#table1 {
}

#table2 {
}

#table1Header1 {
	background-color: darkblue;
  height: 20px;
}

#table2Header1 {
  background-color: #a40000;
  height: 20px;
}

#table1Header2 {
	background-color: steelblue;
  height: 50px;
  /* border-bottom: 2px solid #383838; */
} 

#table2Header2 {
	background-color: #cd5c5c;
  height: 50px;
  /* border-bottom: 2px solid #383838; */

}

tfoot {
  background-color: lightslategray;
  color: white;
  border-top: 2px solid #383838;
}

tbody {
  background-color: #E0E0E0;
  min-width: 400px;
}

tbody tr {
  height: 100px;
  min-height: 100px;
  max-height: 100px;
  vertical-align: middle;
  border-right: 1px solid white;
  /* border-left: 1px solid #383838; */
}

div.clickSortHeader {
  cursor: pointer;
}

tr.even {
  background-color: white;
}

th {
  padding-left:15px;
  padding-right:15px;
  padding-bottom: 0px;
  vertical-align: middle;
}

#table1Header1 th:first-of-type {
  border-top-left-radius: 15px;
}

#table1Header1 thead:first-of-type {
  border-top-left-radius: 15px solid #383838;

}

#table2Header1 th:first-of-type {
  border-top-right-radius: 15px;
}




th.gold {
  background-color: #D4AF37;
}

th.silver {
  background-color: #C0C0C0;
}

th.bronze {
  background-color: #B08D57;
}

td {
  vertical-align: middle;
}

td.contingent {
  min-width: 50px;
  max-width: 200px;
  margin-top: 15%;
  display: -webkit-box;
  -webkit-line-clamp: 2;
          line-clamp: 2;
  -webkit-box-orient: vertical;
  /* text-overflow:ellipsis;  only needed if not using webkit*/
  overflow: scroll;
}

.leaderboard {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
}

#tableWrapper {
  display: flex;
  justify-content: center;
  flex-direction: row;
  margin: auto;
}

.unhighlightedColumn {

}

.highlightedColumn {
  background-color: #b0c4de7f;
}

.fullImg {
    display: inline;
      transform: scale(0.5, 0.5);
}
.smallImg {
    display: none;
      transform: scale(0.25, 0.25);

}

/* Adjust for different screen sizes */
@media screen and (max-width: 1920px) {
    .leaderboard {
      font-size: medium;
    }

    #tableWrapper {
      justify-content: center;
      flex-direction: row;
      margin: auto;
    }

    .fullTitle {
      display: inline;
    }
    .abbrTitle {
      display: none;
  }
}

@media screen and (max-width: 1440px) {
    .leaderboard {
      font-size: medium;
    }

    #tableWrapper {
      justify-content: center;
      flex-direction: row;
      margin: auto;
    }

    .fullTitle {
      display: none;
    }
    .abbrTitle {
      display: inline;
  }
}


@media screen and (max-width: 1024px) {
    .leaderboard {
      font-size: medium;
    }

    #tableWrapper {
      justify-content: center;
      flex-direction: column;
      margin: auto;
    }

    tbody tr {
      height: 40px;
      min-height: 40px;
      max-height: 100px;
      vertical-align: middle;
      border-right: 1px solid white;
      /* border-left: 1px solid #383838; */
    }

    td.contingent {
      min-width: 50px;
      max-width: 150px;
      height: 20px;
      vertical-align: top;
      /* display: -webkit-box;
      -webkit-line-clamp: 2;
              line-clamp: 2;
      -webkit-box-orient: vertical; */
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }

    .fullTitle {
      display: none;
    }
    .abbrTitle {
      display: inline;
  }
}

/* @media screen and (max-width: 1440px) {
    .leaderboard {
      font-size: small;
    }
}

@media screen and (max-width: 1200px) {
    .leaderboard {
      font-size: medium;
    }
} */

  </style>
  