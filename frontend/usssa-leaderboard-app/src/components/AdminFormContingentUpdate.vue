<template>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Country</th>
                <th>National Federation</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(inputContingent, idx) in inputContingents" :key="idx">
                <td>
                    <input 
                        placeholder="Enter Team or Contingent Name" 
                        v-model="inputContingent.name"
                        size="50"
                    >
                </td>
                <td>
                    <select v-model="inputContingent.country">
                        <option disabled value="">select country</option>
                        <option v-for="country in Object.entries(countryNames)"
                            :key="country[0]"
                            :value="country[0]"
                        >{{ country[1]}} - {{country[0]}}</option>
                    </select>
                </td>
                <td>
                    <input type="checkbox" id="nationalFederation" value="true" v-model="inputContingent.is_national_federation">
                </td>
                <td>
                    <button @click="addTeamRow">+</button>
                </td>

            </tr>

        </tbody>


    </table>

    <button @click="submit">Submit</button>


    <div id="currentRoster">
    <h4>Entered Teams</h4>
        <table>
            <thead>
                <tr>
                    <th>Contingent</th><th>Country</th><th>Is National Federation</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="contingent in contingents"
                    :key="contingent.name">
                    <td>{{ contingent.name }}</td>
                    <td>{{ contingent.country }}</td>
                    <td v-if="contingent.is_national_federation">☑️</td>
                    <td v-else>❌</td>
                
                </tr>

            </tbody>
        </table>
    </div>




</template>

<script>
import axios from 'axios'
import countries from '../assets/country_names.json'

export default {
    name: "AdminFormContingentUpdate",
    data() {
        var emptyContingent = { 
            name: '', country: '', is_national_federation: false 
        }
        return  {
            emptyContingent: Object.assign({}, emptyContingent),
            inputContingents: [ 
                Object.assign({}, emptyContingent)
            ],
            numRows: 1,
            selectedCategory: {
                name: '',
                fields: []
            },
            goldContingent: '',
            silverContingent: '',
            bronzeContingent: {},
            fieldSelections: {
                values: []
            },
            countryNames: countries
        }
    },
    props: {
        slug: String,
        categories: Array,
        category_results: Array,
        categoryIdx: Number,
        contingents: Array,
        fieldIdx: Number,
    },
    computed: {
        formIsValid() {
            return true
        },
    },
    methods: {
        addTeamRow() {
            this.inputContingents.push(
                Object.assign({}, this.emptyContingent)
            )
        },
        submit() {
            // build payload, 

            var contingentsData = {
                contingents: this.inputContingents
            }

            console.log("payload")
            console.log(contingentsData)
            this.postContingents(contingentsData)
            this.inputContingents = [Object.assign({}, this.emptyContingent)]
        },
        async postContingents(resultsData) {
            await axios.post(`http://127.0.0.1:8000/leaderboards/${this.slug}/contingents/batch`, resultsData).then(response => {
                console.log(response.data);
                // TODO event bus the leaderboard
                // this.category_results = response.data.category_results
                return response.data;
            });
        }

  }
}
</script>

<style scoped>
.formWarning {
    color: darkred;

}

.formRow {
    display: table-row;
}

.formLabel {
	display: table-cell;
    padding: 5px;
}

.formInput {
	display: table-cell;
    align-items: flex-start;
}


.formOptionList {
    column-count: 3
}

td#currentRoster {
    border-width: 1px;
}

div#currentRoster {
    border-color: black;
    border-style: 1px dashed;

}
</style>