<template>
  <div class="container">
    <div class="twenty-percent"></div>
    <div class="eighty-percent">
      <div class="gallery-wrapper">
        <div class="swiper-container">
          <div class="swiper-wrapper">
            <div class="swiper-slide">
              <img src="@/assets/swiper1.jpg" />
              <div class="slide-text">
                <h2>Title</h2>
                <p>Description</p>
              </div>
            </div>
            <div class="swiper-slide">
              <img src="@/assets/swiper2.jpg" />
              <div class="slide-text">
                <h2>Title 2</h2>
                <p>Description 2</p>
              </div>
            </div>
            <div class="swiper-slide">
              <img src="@/assets/swiper3.jpg" />
              <div class="slide-text">
                <h2>Title 3</h2>
                <p>Description 3</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Swiper from "swiper/bundle";
import "swiper/swiper-bundle.css";

export default {
  mounted() {
    new Swiper(".swiper-container", {
      slidesPerView: 1,
      spaceBetween: -1,
      loop: true,
      centeredSlides: true,
      grabCursor: true,
      preloadImages: 0,
      autoplay: {
        delay: 5000,
        disableOnInteraction: false,
      },
    });
  },
};
</script>

<style>
* {
  margin: 0;
}

.container {
  display: flex;
  height: 100vh; /* Ustawienie na całą wysokość okna przeglądarki */
}

.twenty-percent {
  width: 2%;
}

.eighty-percent {
  width: 98%;
  box-sizing: border-box;
}

.gallery-wrapper {
  overflow: hidden;
}

.swiper-slide img {
  width: 100%;
  height: 350px;
  object-fit: cover;
  object-position: center;
}

.slide-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: #fff;
}

.slide-text h2 {
  font-size: 2em;
  margin-bottom: 10px;
}

.slide-text p {
  font-size: 1.2em;
}

.swiper-button-prev,
.swiper-button-next {
  position: absolute;
  top: 13%;
}
</style>
