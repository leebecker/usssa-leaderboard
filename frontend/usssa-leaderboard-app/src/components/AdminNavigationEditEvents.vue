
<template>
    <AccordionList>
      <AccordionItem>
        <template #summary>Add Teams</template>
        <template #icon>&#128101;&#128681;</template>

        <AdminFormContingentUpdate 
          :slug="leaderboard.slug"
          :categories="leaderboard.categories" 
          :category_results="leaderboard.category_results"
          :contingents="leaderboard.contingents"
        />
      </AccordionItem>
      <AccordionItem>
        <template #summary>Update Category Results</template>
        <template #icon>&#129351;&#129352;&#129353;</template>

        <AdminFormCategoryUpdate 
          :slug="leaderboard.slug"
          :categories="leaderboard.categories" 
          :category_results="leaderboard.category_results"
          :contingents="leaderboard.contingents"
        />
      </AccordionItem>
    </AccordionList>


</template>

<script>
import AdminFormCategoryUpdate from './AdminFormCategoryUpdate.vue';
import AdminFormContingentUpdate from './AdminFormContingentUpdate.vue';
import { AccordionList, AccordionItem } from  "vue3-rich-accordion";
import { useLeaderboardsStore} from "@/stores"

const leaderboardStore = useLeaderboardsStore()

export default {
  name: 'AdminNavigationEditEvents',
  props: {
      slug: String
  },
  data() {
    console.log("init data");
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
          this.leaderboard = await leaderboardStore.getLeaderboard(this.slug)
          console.log(this.leaderboard)
      }
  },
  async created() {
      await this.getLeaderBoard();
      //console.log(this.leaderboard.contingents)
      console.log(this.leaderboard);
  },
  components: { 
    AdminFormCategoryUpdate,
    AdminFormContingentUpdate,
    AccordionList,
    AccordionItem,
  },
  computed: {

  }
}
</script>