<template>
  <div>
    <h1>Search results for: "{{ query }}"</h1>
    <ul v-for="result in results" :key="result.id">
      <img :src="'http://localhost:8000' + result.image" />
      <div class="info">
        <span class="name">{{ result.name }} </span>
        <span class="author"> by {{ result.author }}</span>
      </div>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchResult",
  data() {
    return {
      results: [],
      query: this.$route.query.q,
    };
  },
  watch: {
    '$route.query.q'(newVal) {
      this.query = newVal;
      this.fetchResults();
    },
  },
  created() {
    this.fetchResults();
  },
  methods: {
    fetchResults() {
      axios
        .get(`http://localhost:8000/search/?q=${this.query}`)
        .then((response) => {
          this.results = response.data.results;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped></style>
