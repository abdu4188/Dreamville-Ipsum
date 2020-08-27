<template>
  <img
    class="VuetifyLogo"
    alt="Vuetify Logo"
    src="/dreamville.jpg"
  >
</template>

<style>
.VuetifyLogo {
  height: 100px;
  width: 190px;
  transform: rotateY(560deg);
  animation: turn 3.5s ease-out forwards 1s;
}

@keyframes turn {
  100% {
    transform: rotateY(0deg);
  }
}
</style>
