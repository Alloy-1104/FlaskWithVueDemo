<template>
  <BMICalculator/>
</template>

<script>
import BMICalculator from "./components/BMICalculator.vue";

export default {
  name: 'App',
  components: {
    BMICalculator
  }
}
</script>

<style>
#app {
  width: 100%;
  height: 100%;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color:#f0f2f5; 
  display: flex;
  flex-direction: column;
  justify-content: center;
}

input {
  color: #2c3e50;
}

.container {
  background-color: white;
  padding: 20px 10px;
}

.container.inner {
  padding: 0;
}

.container > * {
  margin: 10px 0;
  position: relative;
}

.container > .title {
  height: 40px;
  line-height: 40px;
  font-size: 2rem;
  margin-bottom: 30px;
}

</style>
