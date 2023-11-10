import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SearchResult from "../views/SearchResultPage.vue";
import BookDetail from "../views/BookDetail.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/search-result",
    name: "SearchResult",
    component: SearchResult,
  },
  {
    path: "/book/:bookName/:bookAuthor",
    name: "BookDetail",
    component: BookDetail,
  },
];
const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
