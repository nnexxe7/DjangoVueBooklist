<template>
  <header>
    <div class="logo"><a href="/">My Site</a></div>
    <nav>
      <ul>
        <li>
          <a href="#"><i class="fas fa-envelope"></i> Contact</a>
        </li>
        <li>
          <a href="#"><i class="fas fa-book"></i> Books</a>
        </li>
        <li>
          <a href="#"><i class="fas fa-list"></i> List</a>
        </li>
        <li>
          <a href="#" @click="showSearchInput"
            ><i class="fas fa-search"></i> Search</a
          >
        </li>
        <li>
          <a href="#"><i class="fas fa-sign-in-alt"></i> Log In</a>
        </li>
      </ul>
    </nav>
    <div :class="{ hidden: !showInput }">
      <input
        v-model="query"
        type="text"
        placeholder=" Search..."
        spellcheck="false"
      />
      <div class="search-icons">
        <i v-if="showInput" class="fas fa-search" @click="search"></i>
        <i v-if="showInput" class="fas fa-times" @click="closeSearchInput"></i>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      showInput: false,
    };
  },
  methods: {
    showSearchInput() {
      this.showInput = true;
    },
    closeSearchInput() {
      this.showInput = false;
    },
  },
};
</script>

<style scoped>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f1f1f1;
  height: 60px;
  max-height: 60px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  margin-top: 2px;
  margin-right: 5px;
  margin-left: 5px;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none;
}

.logo a {
  text-decoration: none;
  color: #333;
  margin-left: 10px;
}

nav ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

nav ul li {
  margin-left: 1rem;
}

nav ul li:first-child {
  margin-left: 0;
}

nav ul li a {
  display: flex;
  align-items: center;
  color: #555;
  text-decoration: none;
  margin-right: 10px;
}

nav ul li a:hover {
  color: #000;
}

nav ul li a i {
  margin-right: 0.5rem;
}

nav ul li a span {
  margin-left: 0.5rem;
}

.hidden {
  display: none;
}

div input {
  position: absolute;
  left: 0;
  right: 0;
  margin-top: 8px;
  top: 0;
  width: 95%;
  height: 50px;
  align-items: center;
  border: none;
  background-color: #f1f1f1;
  margin-left: 0.5rem;
  font-size: 1.75em;
  border-radius: 5px;
}

input[type="text"] {
  padding: 0;
}

.search-icons i:nth-child(2) {
  margin-right: 10px;
}

.search-icons i:nth-child(1) {
  margin-right: 20px;
}
</style>
