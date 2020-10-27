## Django With Tailwind:CSS

Installation Document is following the [tailwind site's script](https://tailwindcss.com/docs/installation). Following is the Adding the module in the Webpack module running the React.js.

## Script of the Process

###  Install Modules

`autoprefixer@10.0.0` is breaks next's **postcss loader** on start. so rolled back to the `autoprefixer@9.8.6` and issue is resolve. **[post on Github](https://github.com/vercel/next.js/issues/17236)**

```r
$ cd static
$ yarn add -D tailwindcss postcss-cli postcss-loader autoprefixer@9.8.6
```

### TailwindCSS & PostCSS configuration

```r
$ nvim tailwind.config.js
module.exports = {
  theme: {
    extend: {}
  },
  variants: {},
  plugins: []
}

$ npx tailwind init
  tailwindcss 1.3.0
  Created Tailwind config file: tailwind.config.js
```

### build the Base CSS file

```r
$ mkdir ./src/style
$ nvim ./src/style/tailwind.css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
```

### Building the Tailwind:CSS file

```r
$ nvim postcss.config.js
module.exports = {
  plugins: [
    require("tailwindcss")("./tailwind.config.js"),
    require("autoprefixer")
  ]
};

$ nvim package.json
  "scripts": {
    ...
    "build:css": "postcss src/style/tailwind.css -o src/style/main.css"
  },

$ npm run build:css
  yarn run v1.22.5
    $ postcss src/style/tailwind.css -o src/style/main.css
  Done in 2.11s.
```

### `main.css` Insert in React.js

```javascript
# ./src/index.js
import React from "react";
import "./style/main.css";
```

### Webpack Setting

```r
$ nvim webpack.config.js

    module: {
      rules: [
        ...
        {
          test: [/\.css$/, /\.s[ac]ss$/i],
          use: [
            'style-loader',
            'css-loader',
            'sass-loader',
            {
              loader: 'postcss-loader',
              options: {
                postcssOptions: {
                  ident: 'postcss',
                  plugins: [
                    require('tailwindcss'),
                    require('autoprefixer'),
                  ],
                },
              }
            },
          ],
        },
```

### Fixing the tailwind.css

```r
$ nvim ./src/style/tailwind.css

  @tailwind base;
  @tailwind components; 
  .hash-tag {
    @apply inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2;
  }
  @tailwind utilities;

$ yarn build:css
$ yarn start
```

<br />

## Sites

- **[Tailwind CSS Install](https://tailwindcss.com/docs/installation)**
- **[Tailwind CSS in React.js](https://ggodong.tistory.com/212)**
