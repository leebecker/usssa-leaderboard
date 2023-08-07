<template>
    <button @click="addCategory">+ Category</button>
    <div v-for="category, categoryIdx in categories" :key="category.name">
    <AdminFormCreateEventCategory
      v-model="categories[categoryIdx]"
    ></AdminFormCreateEventCategory>
    </div>

    <div class="formRow">
        <div class="formLabel">
            <h4>Short Name</h4>
        </div>
        <div class="formInput">
            <input placeholder="Enter short name" size="50">
            <p>(This name is used to generate URLs, e.g. T5 Championship 2023)</p>
        </div>
    </div>
    <div class="formRow">
        <div class="formLabel">
            <h4>Description</h4>
        </div>
        <div class="formInput">
            <input placeholder="Enter display name" size="50">
            <p>(This is the display name, e.g. T5 Liberty Chalice Championship 2023)</p>
        </div>
    </div>

    <div class="formRow">
        <div class="formLabel">
            <h4>Award Values</h4>
        </div>
        <div class="formInput">
            <p>
              Gold: <vue-number-input v-model="award_values.gold" :min="0" :max="100" size="small" inline center controls></vue-number-input>
            </p>
            <p>
              Silver: <vue-number-input v-model="award_values.silver" :min="0" :max="100" size="small" inline center controls></vue-number-input>
            </p>
            <p>
              Bronze: <vue-number-input v-model="award_values.bronze" :min="0" :max="100" size="small" inline center controls></vue-number-input>
            </p>
        </div>
    </div>


    <div class="formRow">
        <div class="formLabel">
            <h4>Categories</h4>
        </div>
        <div class="addCategory">

          <div class="formInput">
              <div class="formList"
                v-for="category, categoryIdx in categories" 
                :key="categoryIdx" >
                <label>{{categoryIdx}}. Category </label>
                <input 
                  v-model="categories[categoryIdx].name"
                  placeholder="Enter category name" size="50">
                <button v-if="!categoryIdx" @click="addCategory">+</button>

                <div class="formList"
                  v-for="field, fieldIdx in category.fields" :key="fieldIdx">
                  <label>Field: </label>
                  <input
                    v-model="category.fields[fieldIdx].name"
                    placeholder="Enter field name" size="50">
                  <button v-if="!categoryIdx && !fieldIdx" @click="addField(category)">+</button>

                  <div class="formList"
                    v-for="option, optionIdx in field.options" :key="optionIdx"
                  >
                    <label >Option: </label>
                    <button v-if="!categoryIdx && !fieldIdx && !optionIdx"
                      @click="addOption(field)">+</button>
                    <input 
                      placeholder="Enter option name" size="50">
                  </div>
                </div>
              </div>
          </div>
      </div>
    </div>
      <button @click="submit">Submit</button>

</template>


<script>


import AdminFormCreateEventCategory from './AdminFormCreateEventCategory.vue'

export default {
  name: 'AdminFormCreateEvent',
  props: {
  },
  data() {

    return {
      award_values: {
        gold: 100,
        silver: 70,
        bronze: 40
      },
      value: 10,
      categories: [ this.createCategory() ],
    }
  },
  computed: {

  },
  methods: {
    createField() {
      return {
        name: '',
        options: ['']
      }
    },
    createCategory() {
      return {
        name: '',
        fields: [this.createField()]
      }
    },
    addCategory() {
      this.categories.push(this.createCategory())
    },
    addField(category) {
      category.fields.push(this.createField())
    },
    addOption(field) {
      field.options.push('')
    },
    submit() {
      console.log("SUBMIT")
      console.log(this.categories)

    }

  },
  components: {
    AdminFormCreateEventCategory
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

.formList {
  margin-left: 20px;

}

.submittedCategories {
    text-align: left;

}
.vue-number-input + .vue-number-input {
  margin-left: 1rem;
}
</style>

