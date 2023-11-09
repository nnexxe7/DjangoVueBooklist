<script>
import SidebarLink from "./SidebarLink";
import { collapsed, toggleSidebar, sidebarWidth } from "./state";
import axios from "axios";

export default {
  props: {},
  components: { SidebarLink },
  setup() {
    return { collapsed, toggleSidebar, sidebarWidth };
  },
  data() {
    return {
      hided: false,
      searchOpen: false,
      query: "",
      results: [],
    };
  },
  methods: {
    showSearch() {
      this.hided = !this.hided;
      this.collapsed = false;
    },
    search() {
      if (!this.query) {
        return;
      }
      const query = this.query;
      axios
        .get(`http://localhost:8000/search/?q=${this.query}`)
        .then((response) => {
          this.results = JSON.parse(JSON.stringify(response.data));
          this.$router.push({ name: "SearchResult", query: { q: this.query } });
          this.query = "";
          this.hided = !this.hided;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">
        <div>V</div>
        <div>S</div>
      </span>
      <span v-else>Vue Sidebar</span>
    </h1>

    <SidebarLink to="/" icon="fas fa-columns">Dashboard</SidebarLink>
    <SidebarLink to="/analytics" icon="fas fa-chart-bar">Analytics</SidebarLink>
    <SidebarLink to="/friends" icon="fas fa-sign-in-alt">Log In</SidebarLink>
    <SidebarLink to="" @click="showSearch" icon="fas fa-search"
      >Search</SidebarLink
    >
    <input
      v-if="hided"
      v-model="query"
      type="text"
      placeholder="Type here to search ..."
      class="sidebar-link"
    />
    <button v-if="hided" @click="search">Search for book</button>

    <span
      class="collapse-icon"
      :class="{ 'rotate-180': collapsed }"
      @click="toggleSidebar"
    >
      <i class="fas fa-angle-double-left" />
    </span>
  </div>
</template>

<style>
:root {
  --sidebar-bg-color: #2f855a;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
}
</style>

<style scoped>
.sidebar {
  color: white;
  background-color: var(--sidebar-bg-color);

  float: left;
  position: fixed;
  z-index: 999;
  top: 0;
  left: 0;
  bottom: 0;
  padding: 0.5em;

  transition: 0.3s ease;

  display: flex;
  flex-direction: column;
}

.sidebar h1 {
  height: 2.5em;
}

.collapse-icon {
  position: absolute;
  bottom: 0;
  padding: 0.75em;

  color: rgba(255, 255, 255, 0.7);

  transition: 0.2s linear;
}

.rotate-180 {
  transform: rotate(180deg);
  transition: 0.2s linear;
}
</style>
