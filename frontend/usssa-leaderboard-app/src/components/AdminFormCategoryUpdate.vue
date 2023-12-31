<template>
    <div class="formRow">
        <div class="formLabel">
            <h4>Category</h4>
        </div>
        <div class="formInput">
            <select v-model="selectedCategory">
                <option disabled value="">select category</option>
                <option v-for="category in categories"
                    :key="category.name"
                    :value="category">
                    {{ category.name }}</option>
            </select>

            <select v-for="(field, fieldIdx) in selectedCategory.fields" :key="field.name" v-model="fieldSelections.values[fieldIdx]">
                <option disabled value="">select {{ field.name }}</option>
                <option v-for="fieldOption in field.options" :key="fieldOption">{{ fieldOption }}</option>
            </select>

            <p v-if="isSelectedCategoryAlreadySubmitted" class="formWarning">
                Selected Category has already been submitted
            </p>
        </div>
    </div>

    <div class="formRow">
        <div class="formLabel">
            <h4>&#129351; Gold Contingent</h4>
        </div>
        <div class="formInput">
            <div class="formOptionList">
                <div v-for="(contingent) in contingents" :key="contingent.id">
                    <input type="checkbox" v-model="goldContingent[contingent.id]" :id="contingent.id" name="gold" :value="contingent.id" />
                    <label for="contingent.id">{{ contingent.name }} </label>
                </div>
            </div>
        </div>
        <p/>
    </div>

    <div class="formRow">
        <div class="formLabel">
            <h4>&#129352; Silver Contingent</h4>
        </div>
        <div class="formInput">
            <div class="formOptionList">
                <div v-for="(contingent) in contingents" :key="contingent.id">
                    <input type="checkbox" v-model="silverContingent[contingent.id]" :id="contingent.id" name="silver" :value="contingent.id" />
                    <label>{{ contingent.name }} </label>
                </div>
            </div>
        </div>
    </div>

    <div class="formRow">
        <div class="formLabel">
        <h4>&#129353; Bronze Contingents</h4>
        </div>

        <div class="formInput">
            <p v-if="numberBronze > 2" class="formWarning">
                Maximum 2 bronze medals per category
            </p>
            <div class="formOptionList">
                <div v-for="(contingent) in contingents" :key="contingent.id">
                    <input type="checkbox" v-model="bronzeContingent[contingent.id]" :id="contingent.id" name="silver" :value="contingent.id" />
                    <label>{{ contingent.name }} </label>
                </div>
            </div>
        </div>
    </div>


    <div v-if="formIsValid">
        <button @click="submit">Submit</button>
    </div>


    <hr>
    <div class="submittedCategories">
        <h3>Already submitted categories</h3>

        <ul>
            <li v-for="category in scoredCategories"
                :key="category"
            >{{ category }}</li>
        </ul>

    </div>


</template>

<script>
import { useLeaderboardsStore } from '@/stores'

const leaderboardsStore  = useLeaderboardsStore();

export default {
    name: "AdminFormCategoryUpdate",
    data() {
        return  {
            selectedCategory: {
                name: '',
                fields: []
            },
            goldContingent: {},
            silverContingent: {},
            bronzeContingent: {},
            fieldSelections: {
                values: []
            }
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
        numberBronze() {
            return Object.entries(this.bronzeContingent)
                .filter(o => o[1])
                .length
        },
        currentCategory() {
            return this.categories[this.categoryIdx]
        },
        isSelectedCategoryAlreadySubmitted() {
            var selectedCategoryKey = [this.selectedCategory.name]
                .concat(this.fieldSelections.values)
                .join('-')

            return (
                this.scoredCategories.includes(selectedCategoryKey)
            )
        },
        formIsValid() {
            return (
                this.selectedCategory &&
                this.selectedCategory.name &&
                this.fieldSelections.values.length == this.selectedCategory.fields.length &&
                !this.isSelectedCategoryAlreadySubmitted && 
                this.goldContingent && 
                this.silverContingent &&
                this.numberBronze > 0 &&
                this.numberBronze <= 2
            )
        },
        scoredCategories() {
            console.log("category_results")
            if (this.category_results != null) {
                return this.category_results.map(this.categoryResultToKey)
            } else {
                return []
            }
        }


    },
    methods: {
        checkboxInputToIds(input) {
            return Object.entries(input)
                .filter((o) => o[1] && o[1] != null).map((o) => o[0])
        },
        submit() {
            // build payload, 

            /*
            var goldIds = Object.entries(this.bronzeContingent)
                .filter((o) => o[1] && o[1] != null).map((o) => o[0])

            var silverIds = Object.entries(this.bronzeContingent)
                .filter((o) => o[1] && o[1] != null).map((o) => o[0])

            var bronzeIds = Object.entries(this.bronzeContingent)
                .filter((o) => o[1] && o[1] != null).map((o) => o[0])
                */

            var resultsData = {
                "category": {
                    "name": this.selectedCategory.name,
                    "fields": this.fieldSelections.values
                },
                "gold_contingent_id": this.checkboxInputToIds(this.goldContingent),
                "silver_contingent_id": this.checkboxInputToIds(this.silverContingent),
                "bronze_contingent_id": this.checkboxInputToIds(this.bronzeContingent)
            }

            console.log("payload")
            console.log(resultsData)
            leaderboardsStore.addCategoryResults(this.slug, resultsData)
        },
        categoryResultToKey(categoryResult) {
            return [categoryResult.category.name]
                .concat(categoryResult.category.fields)
                .join('-')
        },
  }
}
</script>

<style scoped>
.formWarning {
    color: darkred;

}

.formRow {
	display: table-row;
    text-align: left;
}

.formLabel {
	display: table-cell;
    padding: 20px;
}

.formInput {
	display: table-cell;
    align-items: flex-start;
}


.formOptionList {
    column-count: 3;
}

.submittedCategories {
    text-align: left;

}
</style>