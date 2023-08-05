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
            <h4>Gold Contingent</h4>
        </div>
        <div class="formInput">
            <div class="formOptionList">
                <div v-for="(contingent) in contingents" :key="contingent.id">
                    <input type="radio" v-model="goldContingent" :id="contingent.id" name="gold" :value="contingent.id" />
                    <label>{{ contingent.name }} </label>
                </div>
            </div>
        </div>
        <p/>
    </div>

    <div class="formRow">
        <div class="formLabel">
            <h4>Silver Contingent</h4>
        </div>
        <div class="formInput">
            <div class="formOptionList">
                <div v-for="(contingent) in contingents" :key="contingent.id">
                    <input type="radio" v-model="silverContingent" :id="contingent.id" name="silver" :value="contingent.id" />
                    <label>{{ contingent.name }} </label>
                </div>
            </div>
        </div>
    </div>

    <div class="formRow">
        <div class="formLabel">
        <h4>Bronze Contingents</h4>
        </div>

        <div class="formInput">
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



</template>

<script>

export default {
    data() {
        return  {
            selectedCategory: {
                name: '',
                fields: []
            },
            goldContingent: '',
            silverContingent: '',
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
            var numberBronze = Object.entries(this.bronzeContingent).filter(o => o[1]).length
            return (
                this.selectedCategory &&
                this.selectedCategory.name &&
                this.fieldSelections.values.length == this.selectedCategory.fields.length &&
                !this.isSelectedCategoryAlreadySubmitted && 
                this.goldContingent && 
                this.silverContingent &&
                numberBronze > 0
            )
        },
        scoredCategories() {
            return this.category_results.map(this.categoryResultToKey)
        }


    },
    methods: {
        submit() {
            // build payload, 

            var bronzeIds = Object.entries(this.bronzeContingent)
                .filter((o) => o[1] && o[1] != null).map((o) => o[0])

            var postPayload = {
                "category": {
                    "name": this.selectedCategory.name,
                    "fields": this.fieldSelections.values
                },
                "gold_contingent_id": this.goldContingent,
                "silver_contingent_id": this.silverContingent,
                // convert this to array
                "bronze_contingent_id": bronzeIds
            }

            console.log("payload")
            console.log(postPayload)
        },
        categoryResultToKey(categoryResult) {
            return [categoryResult.category.name]
                .concat(categoryResult.category.fields)
                .join('-')
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
    padding: 20px;
}

.formInput {
	display: table-cell;
    align-items: flex-start;
}


.formOptionList {
    column-count: 3
}
</style>