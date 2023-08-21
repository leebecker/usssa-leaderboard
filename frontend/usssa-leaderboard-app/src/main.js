import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia';
import { useAccordion } from "vue3-rich-accordion";
import "vue3-rich-accordion/accordion-library-styles.css";
import VueNumberInput from '@chenfengyuan/vue-number-input';




createApp(App)
    .use(router)
    .use(useAccordion)
    .use(createPinia())
    .component(VueNumberInput.name, VueNumberInput)
    .mount('#app')
