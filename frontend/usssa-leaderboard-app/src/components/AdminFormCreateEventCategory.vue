<template>
    <div class="category">
        <label>Category: </label>
        <div class="categoryInput"></div>
            <input 
                :v-model="category.name"
                placeholder="Enter category name" size="25">

            <div class="field" 
                v-for="field, fieldIdx in category.fields"
                :key="fieldIdx">

                <div class="fieldInput">
                    <label>Field: </label>
                    <input
                        v-model="field.name"
                        placeholder="Enter field name" size="25">

                    <div class="optionDiv">
                        <div class="optionLabel"></div>

                                <label>Options: </label>
                        </div>
                        <div class="optionInput">
                            <input 
                                v-for="option, optionIdx in category.fields[fieldIdx].options"
                                :key="optionIdx"
                                v-model="category.fields[fieldIdx].options[optionIdx]"
                                placeholder="option" size="25">
                        </div>
                        <button @click="addOption(field)">+</button>
                    </div>
                </div>
                <button @click="addField()">+</button>
            </div>

</template>


<script>

export default {
  name: 'AdminFormCreateEvent',
  props: {
  },
  data() {
    return {
        category : this.createCategory()
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
    addField() {
        this.category.fields.push(this.createField())
    },
    addOption(field) {
        console.log(field)
        field.options.push('')
        console.log(this.category.fields[0])
    }

  },
  components: {
    //VueNumericInput
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

.category {
    display: flex;
    flex-direction: row;
    align-self: start;
}

.categoryInput {
    text-align: left;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
}

.field button {
    align-self: start;

}

.field {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-self: start;

}

.fieldInput {

    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    align-self: start;
}

.optionDiv {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    align-self: start;
}


.optionLabel {
    display: flex;
    flex-direction: row;


}

.optionInput {
    display: flex;
    flex-direction: column;
}


.rowLabel {

}

.rowInput {
    align-items: flex-start

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

input {
    display: block;
    align-self: start;

}
button {
    display: inline-block;
    align-self: start

}
</style>
