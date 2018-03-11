const fs = require('fs');

const config = {
  entry: JSON.parse(fs.readFileSync('webpack/webpack.entrypoints.json')),
  output: {
    filename: '[name].js',
    path: __dirname + '/../build/js',
  },
};

module.exports = config;