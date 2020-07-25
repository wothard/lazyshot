'use strict'

// All configuration item explanations can be find in https://cli.vuejs.org/config/
module.exports = {
  /**
   * You will need to set publicPath if you plan to deploy your site under a sub path,
   * for example GitHub Pages. If you plan to deploy your site to https://foo.github.io/bar/,
   * then publicPath should be set to "/bar/".
   * In most cases please use '/' !!!
   * Detail: https://cli.vuejs.org/config/#publicpath
   */
  publicPath: '/',
  outputDir: 'dist',
  assetsDir: 'static',
  //vue.config.js
  devServer: {
    proxy: {
      '/': {
        target: 'http://127.0.0.1:5000',
        ws: false,
        changeOrigin: true,//允许跨域
        pathRewrite: {
          '^/': '/'
        }
      }
    },

  },

}
