<template>
  <div>
    <div>
      <div>
        <h2>{{ bookDetails.name }}</h2>
        <p>Author: {{ bookDetails.author }}</p>
        <img :src="'http://localhost:8000' + bookDetails.image" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BookDetail",
  data() {
    return {
      bookDetails: {},
    };
  },
  created() {
    this.fetchBookDetails();
  },
  methods: {
    fetchBookDetails() {
      const bookName = this.$route.params.bookName;
      const bookAuthor = this.$route.params.bookAuthor;
      axios
        .get(`http://localhost:8000/book/${bookName}/${bookAuthor}`)
        .then((response) => {
          this.bookDetails = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
