<template>Create Event 
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
            <h4>Categories</h4>
        </div>
        <div class="addCategory">

          <div class="formInput">
              <div class="formList"
                v-for="category, categoryIdx in categories" 
                :key="categoryIdx" >
                <label>Category Name: </label>
                <input 
                  v-model="categories[categoryIdx].name"
                  placeholder="Enter category name" size="50">
                <button @click="addCategory">Add Category</button>

                <div class="formList"
                  v-for="field, fieldIdx in category.fields" :key="fieldIdx">
                  <label>Field: </label>
                  <input
                    v-model="category.fields[fieldIdx].name"
                    placeholder="Enter field name" size="50">
                  <button @click="addField">Add Field</button>

                  <div class="formList"
                    v-for="option, optionIdx in field.options" :key="optionIdx"
                  >
                    <label >Option: </label>
                    <input 
                      placeholder="Enter option name" size="50">
                    <button @click="addOption">Add Option</button>
                  </div>
                </div>
              </div>
          </div>
      </div>
    </div>

    <h2>{{ foo }}</h2>

</template>


<script>

export default {
  name: 'AdminFormCreateEvent',
  props: {
  },
  data() {

    var emptyFieldDef = {
        name: '',
        options: ['']
    }
    var emptyCategoryDef = {
      name: '',
      fields: [Object.assign({}, emptyFieldDef)]
    }
    return {
      award_values: {
        gold: 100,
        silver: 70,
        bronze: 40
      },
      emptyCategory: emptyCategoryDef,
      emptyField: emptyFieldDef,
      categories: [ Object.assign({}, emptyCategoryDef) ],
    }
  },
  computed: {
    foo() {
      //if (this.categories) {
        console.log(this.currentCategory)
        console.log(this.currentField)
      //}
      return "v"

    },
    currentCategory() {
      var idx = this.categories.length - 1
      console.log("Curr Category", idx)
      console.log(this.categories[idx])
      return this.categories[idx]
    },
    currentField() {
      var idx = this.currentCategory.fields.length -1
      console.log("Curr Field", idx)
      console.log(this.currentCategory.fields[idx])
      return this.currentCategory.fields[idx]
    },
    currentOptionIdx() {
      console.log("curr field")
      console.log(this.currentField)
      var idx = this.currentField.options.length - 1
      return this.currentField.options[idx]
    }

  },
  methods: {
    addCategory() {
      this.categories.push(
        Object.assign({}, this.emptyCategory)

      )

    },
    addField() {
      this.currentCategory.fields.push(
        Object.assign({}, this.emptyField)
      )

    },
    addOption() {
      this.currentField.options.push('')
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
</style>

