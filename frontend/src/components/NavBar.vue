<template>
  <div class="sidebar" :style="{ width: sidebarWidth }">
    <h1>
      <span v-if="collapsed">
        <div>V</div>
        <div>S</div>
      </span>
      <span v-else>Vue Sidebar</span>
    </h1>

    <router-link to="/">
      <span class="navbar-item">
        <i class="fas fa-columns"></i>
        <transition name="fade">
          <span v-if="!collapsed">Dashboard</span>
        </transition>
      </span>
    </router-link>

    <span class="navbar-item">
      <i class="fas fa-chart-bar"></i>
      <transition name="fade"> <span v-if="!collapsed">Test</span> </transition>
    </span>

    <span class="navbar-item" @click="openModal">
      <i class="fas fa-sign-in-alt"></i>
      <transition name="fade">
        <span v-if="!collapsed">Log In</span>
      </transition>
    </span>

    <span class="navbar-item">
      <i class="fas fa-home"></i>
      <transition name="fade"> <span v-if="!collapsed">Home</span> </transition>
    </span>

    <span class="navbar-item" @click="showSearch">
      <i class="fas fa-search"></i>
      <transition name="fade">
        <span v-if="!collapsed">Search</span>
      </transition>
    </span>

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

  <div>
    <Modal v-if="modalState" @close="closeModal">
      <template v-slot:header>Modal component</template>
      <template v-slot:body>
        <div v-if="loginMode">
          <!-- Sekcja logowania -->
          <h2 class="Napis-modal">Logowanie</h2>
          <!-- Dodaj pola logowania, np. inputy na nazwę użytkownika i hasło -->
          <input
            v-model="username"
            placeholder="Nazwa użytkownika"
            class="input-with-margin"
          />
          <input
            v-model="password"
            type="password"
            placeholder="Hasło"
            class="input-with-margin"
          />
          <br />
          <button @click="performLogin" class="button-with-margin">
            Zaloguj
          </button>
          <p @click="toggleMode">Nie masz konta? <b>Zarejestruj się!</b></p>
        </div>

        <div v-else>
          <!-- Sekcja rejestracji -->
          <h2 class="Napis-modal">Rejestracja</h2>
          <!-- Dodaj pola rejestracji, np. inputy na nazwę użytkownika, hasło i potwierdzenie hasła -->
          <input
            v-model="newUsername"
            placeholder="Nowa nazwa użytkownika"
            class="input-with-margin"
          />
          <input
            v-model="newPassword"
            type="password"
            placeholder="Nowe hasło"
            class="input-with-margin"
          />
          <input
            v-model="confirmPassword"
            type="password"
            placeholder="Potwierdź hasło"
            class="input-with-margin"
          />
          <input
            v-model="email"
            type="email"
            placeholder="Adres e-mail"
            class="input-with-margin"
          />
          <input
            v-model="confirmEmail"
            type="email"
            placeholder="Potwierdź e-mail"
            class="input-with-margin"
          />
          <br />
          <button @click="performRegistration" class="button-with-margin">
            Zarejestruj się
          </button>
          <p @click="toggleMode">Masz już konto? <b>Zaloguj się!</b></p>
        </div>
      </template>
    </Modal>
  </div>
</template>

<script>
import SidebarLink from "./SidebarLink";
import { collapsed, toggleSidebar, sidebarWidth } from "./state";
import axios from "axios";
import modalMixin from "@/mixins/component-modal-mixin";

export default {
  mixins: [modalMixin],
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
      modalState: false,
      loginMode: true,
      newUsername: "",
      newPassword: "",
      confirmPassword: "",
      email: "",
      confirmEmail: "",
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
    login() {
      this.modalState = true;
    },
    closeModal() {
      this.modalState = false;
    },
    closeModal() {
      this.modalState = false;
    },
    toggleMode() {
      this.loginMode = !this.loginMode;
    },
    async performLogin() {
      try {
        const response = await axios.post("http://localhost:8000/api/login/", {
          username: this.username,
          password: this.password,
        });
        console.log(response.data.message);
        // Dodaj kod obsługujący zalogowanie
      } catch (error) {
        console.error("Błąd logowania:", error.response.data.message);
        // Dodaj kod obsługujący błąd logowania
      }
    },
    async performRegistration() {
      try {
        const response = await axios.post(
          "http://localhost:8000/api/register/",
          {
            username: this.newUsername,
            password: this.newPassword,
            email: this.email,
          }
        );
        console.log(response.data.message);
        // Dodaj kod obsługujący rejestrację
      } catch (error) {
        console.error("Błąd rejestracji:", error.response.data.message);
        // Dodaj kod obsługujący błąd rejestracji
      }
    },
  },
};
</script>

<style>
:root {
  --sidebar-bg-color: #2f855a;
  --sidebar-item-hover: #38a169;
  --sidebar-item-active: #276749;
  position: relative;
}
</style>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.1s;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}

.navbar-item {
  display: flex;
  align-items: center;
  cursor: pointer;
  position: relative;
  font-weight: 400;
  user-select: none;
  margin: 0.1em 0;
  padding: 0.4em;
  border-radius: 0.25em;
  height: 1.5em;
  color: white;
  text-decoration: none;
  white-space: nowrap;
}

.navbar-item:hover {
  background-color: var(--sidebar-item-hover);
}

.navbar-item.active {
  background-color: var(--sidebar-item-active);
}

.navbar-item i {
  flex-shrink: 0;
  width: 25px;
  margin-right: 10px;
}

.navbar-item span {
  margin-right: 20px;
}

.Napis-modal {
  margin-bottom: 10px;
}

.button-with-margin {
  margin-top: 5px;
  margin-bottom: 10px;
  width: 100%;
  min-height: 35px;
}

.input-with-margin {
  margin-bottom: 10px;
}
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
