
<script>

import axios from 'axios'
import AdminFormCreateEventCategory from './AdminFormCreateEventCategory.vue'

export default {
  name: 'AdminFormCreateEvent',
  props: {
  },
  data() {
    const defaultCategories = [ this.createCategory() ]
    var data = {
      name: '',
      description: '',
      award_values: {
        gold: 100,
        silver: 70,
        bronze: 40
      },
      value: 10,
      categories: defaultCategories
    }
    return data;
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
      var eventData = {
        name: this.name,
        description: this.description,
        award_values: this.award_values,
        categories: this.categories,
        contingents: []
      };
      console.log(eventData)
      this.postEvent(eventData);
    },
    clear() {
      this.name = ''
      this.description = ''
      this.award_values = {
        gold: 100,
        silver: 70,
        bronze: 40
      },
      this.categories = [this.createCategory()]
    },
    async postEvent(eventData) {
            var api_url = process.env.VUE_APP_LEADERBOARD_API_URL
            await axios.post(`${api_url}/leaderboards`, eventData).then(response => {
                console.log(response.data);
                // TODO event bus the leaderboard
                // this.category_results = response.data.category_results
                return response.data;
            });
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

<template>
    <div class="formRow">
        <div class="formLabel">
            <h4>Short Name</h4>
        </div>
        <div class="formInput">
            <input 
              v-model="name"
              placeholder="Enter short name" size="50">
            <p>(This name is used to generate URLs, e.g. T5 Championship 2023)</p>
        </div>
    </div>
    <div class="formRow">
        <div class="formLabel">
            <h4>Description</h4>
        </div>
        <div class="formInput">
            <input 
              v-model="description"
              placeholder="Enter display name" size="50">
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
          <button @click="addCategory">+ Category</button>
        </div>
        <div class="formInput">
          <AdminFormCreateEventCategory 
            v-for="category, categoryIdx in categories"
            :key="categoryIdx"
            v-model="categories[categoryIdx]"/>
        </div>

    </div>

    <button @click="submit">Submit</button>
    <button @click="clear">Clear</button>

</template>