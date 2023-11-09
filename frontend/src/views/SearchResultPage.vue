<template>
  <div>
    <div class="container">
      <div class="left"></div>
      <div class="mid">
        <h1>Search results for: "{{ query }}"</h1>
        <ul v-for="result in results" :key="result.id">
          <router-link :to="'/book/' + result.name">
            <div class="result-item">
              <img
                class="result-image"
                :src="'http://localhost:8000' + result.image"
              />
              <div class="info">
                <span class="name">{{ result.name }} </span>
                <span class="author"> by {{ result.author }}</span>
              </div>
            </div>
          </router-link>
        </ul>
      </div>
    </div>
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
    "$route.query.q"(newVal) {
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

<style scoped>
h1 {
  margin-left: 25%;
  margin-bottom: 10%;
}

.container {
  text-align: left;
}

.left {
  width: 35%;
  padding: 20px;
  box-sizing: border-box;
}

.mid {
  width: 30%;
  padding: 20px;
  box-sizing: border-box;
}

.result-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 20px;
  margin-top: 20px;
  background-color: #f9f9f9;
  border-bottom: 2px solid #f2f0e8;
}

.result-image {
  max-width: 100px;
  height: auto;
  border-radius: 8px;
  margin-right: 20px;
}

.info {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin-top: 10px;
}

.name {
  font-weight: bold;
  margin-bottom: 5px;
}

.author {
  font-style: italic;
  color: #555;
}
</style>
