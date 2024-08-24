const path = require("path");
const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  assetsDir: "static",
  outputDir: path.resolve(__dirname, "..\\dist"),
  pages: {
    index: {
      entry: "src/main.js",
      title: "BMI計算機"
    }
  }
})
