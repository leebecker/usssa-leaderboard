<script>
import { computed, defineComponent } from 'vue'

export default defineComponent({
  name: 'AdminFormCreateEventCategory',
  emits: ['update:modelValue'],
  props: {
        modelValue: {
            type: Object,
            default: () => (this.createCategory()
            // {
            //     'name': '',
            //     'fields': [{name: '', options:['']}]
            // })
            )
        }
  },
  setup(props, {emit}) {
    const theCategory = computed({
        get: () => props.modelValue,
        set: (value) => emit('update:modelValue', value)
    });
    return { theCategory };
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
        this.theFields.push(this.createField())
    },
    addOption(field) {
        field.options.push('')
    },


  },
  computed: {
    theFields() {
        return this.theCategory.fields
    }

  }
});
</script>


<style scoped>
.formWarning {
    color: darkred;

}

.formRow {
	display: table-row;
    text-align: left;
}

#category {
    grid-template-columns: [category] 1fr [field] 3fr [endCategory];
    display: grid;
    grid-auto-flow: aut;
    /* display: flex;
    flex-direction: row;
    align-self: start; */
}

.categoryItem {
    grid-column-start: 0;
    display: flex;
}

.fieldArea {
    grid-column: field / endCategory;
    grid-template-columns: [fieldInput] 1fr [optionInput] 1fr [endField];
    display: inline-flex;
    margin-left: 10px
}

.fieldItem {
    grid-column-start: fieldInput;
    grid-row-end: span optionInput;
    display: inline-flex;
}

.optionArea {
    grid-column-start: optionInput;
    grid-column-end: endField;
    grid-template-columns: [optionStart] 1fr [optionIn] 1fr [optionEnd];
    display: flex;
    margin-left: 10px;
}

.optionLabel {
    grid-column: 1;

}
.optionLabel {
    grid-column: 2;
    display: inline-flex;
}


.categoryInput {
    grid-row-start: 1;
    background-color: peru;
    /*
    text-align: left;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    flex-wrap: nowrap;
    */

}

.field button {
    align-self: start;

}

.field {
    display: flex;
    flex-direction: row;
    align-self: start;
    margin-left: 5em;
    flex-wrap: nowrap;

}

.optionInput {
    display: flex;
    flex-direction: column;
}

input {
    align-self: start;

}
button {
    display: inline-block;
    align-self: start

}
</style>


<template>
    <div id="category">
        <div class="categoryItem">
        category: 
        <input 
                v-model="theCategory.name"
                placeholder="Enter category name" size="25"
                >
        
        </div>
        <div class="fieldArea"
            v-for="field, fieldIdx in theFields"
            :key="fieldIdx"
        >
            <div class="fieldItem">
                field:
                <input
                        v-model="theFields[fieldIdx].name"
                        placeholder="Enter field name" size="25">
                <button 
                    v-if="fieldIdx == 0"
                    @click="addField()">+</button>
            </div>
            <div class="optionArea">

                options: 
                <div class="optionInput">
                    <div class="optionItem"
                        v-for="option, optionIdx in theFields[fieldIdx].options" :key="optionIdx">
                            <input 
                                v-model="theFields[fieldIdx].options[optionIdx]"
                                placeholder="option" size="25">
                    </div>
                    <button @click="addOption(field)">+</button>
                </div>

            </div>
        </div>
    </div>


</template>
