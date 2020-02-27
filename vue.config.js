module.exports = {
  pluginOptions: {
    electronBuilder: {
      builderOptions: {
        extraFiles: {
          from: 'api_compiled/api',
          to: './resources/api/'
        }
      }
    }
  },
  "transpileDependencies": [
    "vuetify"
  ]
}