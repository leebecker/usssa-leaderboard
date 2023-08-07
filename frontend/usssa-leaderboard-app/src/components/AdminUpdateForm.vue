
<template>
    <!-- Select <i>category</i> along with associated options. -->

    <AccordionList>
      <AccordionItem>
        <template #summary>Add Teams</template>
        <template #icon>&#128101;&#128681;</template>

        <TheContingentUpdateForm 
          :slug="leaderboard.slug"
          :categories="leaderboard.categories" 
          :category_results="leaderboard.category_results"
          :contingents="leaderboard.contingents"
        />
      </AccordionItem>
      <AccordionItem>
        <template #summary>Update Category Results</template>
        <template #icon>&#129351;&#129352;&#129353;</template>

        <TheCategoryUpdateForm 
          :slug="leaderboard.slug"
          :categories="leaderboard.categories" 
          :category_results="leaderboard.category_results"
          :contingents="leaderboard.contingents"
        />
      </AccordionItem>
    </AccordionList>


</template>

<script>
import axios from 'axios'
import TheCategoryUpdateForm from './TheCategoryUpdateForm.vue'
import TheContingentUpdateForm from './TheContingentUpdateForm.vue'
import { AccordionList, AccordionItem } from  "vue3-rich-accordion";


export default {
  name: 'AdminUpdateForm',
  props: {
      slug: String
  },
  data() {
    console.log("HERE WE ARE IS THIS RIGHT?")
      return {
          // initialize to an empty list
          leaderboard: {
            contingents: [],
            standings: [],
            categories: [],
            category_results: [],
            idToContingent: []
          }
      };
  },
  methods: {
      async getLeaderBoard() {
          await axios.get(`http://127.0.0.1:8000/leaderboards/${this.slug}`).then(response => {
              this.leaderboard = response.data;
              this.leaderboard.idToContingent = Object.fromEntries(
                this.leaderboard.contingents.map(c => [c.id, c])
              );
              console.log(this.leaderboard)
              return response.data;
          });
      }
  },
  async created() {
      await this.getLeaderBoard();
      //console.log(this.leaderboard.contingents)
      console.log(this.leaderboard);
  },
  components: { 
    TheCategoryUpdateForm: TheCategoryUpdateForm,
    TheContingentUpdateForm: TheContingentUpdateForm,
    AccordionList: AccordionList,
    AccordionItem: AccordionItem,
  },
  computed: {
    totalEventCategories() {
      console.log(this.leaderboard)
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

  }
}
</script>