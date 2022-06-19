# my-project

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).

# Deployment

Download nginx and use it to reverse proxy our website .

Using the instruction " npm run build "  to package our frontend pages . 

After building , the folder "dist" will generate and move it to the " nginx/html " in your server .

Finally , using intruction "nginx -s reload" reload the info about the web page .

For more detail , you can check out the [Nginx Deployment Guides](https://docs.nginx.com/nginx/deployment-guides/) and [vue-cil Delopyment](https://cli.vuejs.org/guide/deployment.html).
