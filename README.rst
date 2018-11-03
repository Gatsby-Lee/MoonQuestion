.. image:: https://github.com/Gatsby-Lee/MoonQuestion/blob/master/moonquestion/static/images/logo/logo_160.png

Setup
--------------

Install packages

* webpack 4.x | babel-loader 8.x | babel 7.x

.. code-block:: bash

  # yarn creates `package.json` automatically after adding packages.
  yarn add --dev webpack babel-loader @babel/core @babel/preset-env css-loader uglifyjs-webpack-plugin
  yarn add vue-loader
  yarn add vue
  OR
  # `npm init` creates `package.json`.
  # -D, --save-dev: Package will appear in your devDependencies
  npm install --save-dev webpack babel-loader @babel/core @babel/preset-env vue-loader css-loader uglifyjs-webpack-plugin
  npm install --save-dev vue-loader
  npm install vue


Update `package.json`

.. code-block:: bash

  "scripts": {
    "dev": "WEBPACK_ENV=development webpack --progress --colors --watch"
  },


Run webpack

.. code-block:: bash

  npm run dev
  OR
  yarn dev



External References
-------------------
* babel, babel-loader ( from webpack ) verion
  * https://github.com/babel/babel-loader
