<template>

  <AccordionList>
  <AccordionItem>
    <template #summary>Create Events</template>
    <template #icon>➕</template>
    <AdminFormCreateEvent></AdminFormCreateEvent>
    <!-- <LeaderBoardList :enable-admin="true"/> -->
  </AccordionItem>
  </AccordionList>

  <AccordionList>
  <AccordionItem>
    <template #summary>Edit Events</template>
    <template #icon>✏️</template>
    <LeaderBoardList :enable-admin="true"/>
  </AccordionItem>
  </AccordionList>
</template>

<script>
// @ is an alias to /src
import LeaderBoardList from '@/components/LeaderBoardList.vue'
import AdminFormCreateEvent from '@/components/AdminFormCreateEvent.vue'
import { AccordionList, AccordionItem } from  "vue3-rich-accordion";

export default {
  name: 'RootView',
  components: {
    LeaderBoardList,
    AdminFormCreateEvent,
    AccordionList,
    AccordionItem,
  },
  data() {
    return {
    }
  }
}
</script>
