import Modal from "@/components/Modal";

export default {
  components: {
    Modal,
  },
  props: {
    componentTitle: String,
    // Put whatever props you'd like here
  },
  data: () => ({
    modalState: false,
  }),
  methods: {
    openModal() {
      this.modalState = true;
    },
    closeModal() {
      this.modalState = false;
    },
    tryRightClick() {
      alert("Try right-clicking 😉");
    },
  },
  mounted() {
    console.log("Another modal component mounted.");
  },
};
