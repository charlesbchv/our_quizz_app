<template>
  <div class="app-name">
    <span>I’m bringing</span>
    <span class="highlight">
      <span class="highlight-text">QuizApp</span>
    </span>
    <span>back!</span>
  </div>
</template>

<script>
export default {
  name: "AppName"
};
</script>

<style scoped>
.app-name {
  font-size: 3em;
  font-weight: bold;
  text-align: center;
  margin: 40px 0;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}

.app-name .highlight {
  background-color: #eb221d;
  padding: 0 10px;
  border-radius: 10px;
  display: inline-block;
  position: relative;
  margin: 0 10px;
}

.app-name .highlight::before,
.app-name .highlight::after {
  content: '';
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 100%;
  background-color: #7b42f6;
}

.app-name .highlight::before {
  left: -20px;
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}

.app-name .highlight::after {
  right: -20px;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}

.app-name .highlight-text {
  font-family: 'Arial', sans-serif; /* Use a specific font family to match the example */
  font-size: 1em; /* Adjust size as necessary */
  color: #ff0c6a; /* Adjust color to match the example */
}
</style>
