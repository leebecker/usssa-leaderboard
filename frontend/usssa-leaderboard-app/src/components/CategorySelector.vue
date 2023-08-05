<template>
    <h1>{{ selectedCategory.name }}::<span v-for="v in fieldSelections.values" :key="v">{{ v }}.</span> </h1>
    <h2> {{ goldContingent }}</h2>
    <h2> {{ silverContingent }}</h2>
    <h2> {{ bronzeContingent }}</h2>
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
    <p/>

    <h4>Choose Gold Contingent</h4>
    <div v-for="(contingent) in contingents" :key="contingent.id">
        <input type="radio" v-model="goldContingent" :id="contingent.id" name="gold" :value="contingent.id" />
        <label>{{ contingent.name }} </label>
    </div>
    <p/>

    <h4>Choose Silver Contingent</h4>
    <div v-for="(contingent) in contingents" :key="contingent.id">
        <input type="radio" v-model="silverContingent" :id="contingent.id" name="silver" :value="contingent.id" />
        <label>{{ contingent.name }} </label>
    </div>
    <p/>

    <h4>Choose Bronze Contingents</h4>
    <div v-for="(contingent) in contingents" :key="contingent.id">
        <input type="checkbox" v-model="bronzeContingent[contingent.id]" :id="contingent.id" name="silver" :value="contingent.id" />
        <label>{{ contingent.name }} </label>
    </div>
    <p/>



</template>

<script>

export default {
    data() {
        return  {
            selectedCategory: '',
            goldContingent: '',
            silverContingent: '',
            bronzeContingent: {},
            fieldSelections: {
                values: []
            }
        }
    },
    props: {
        categories: Array,
        category_results: Array,
        categoryIdx: Number,
        contingents: Array,
        fieldIdx: Number
    },
    computed: {
        currentCategory() {
            console.log(this.selectedCategory)
            return this.categories[this.categoryIdx]
        },


    }
}
</script>
