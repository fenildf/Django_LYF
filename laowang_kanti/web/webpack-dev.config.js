const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const TransferWebpackPlugin = require('transfer-webpack-plugin');

const SRC_DIR = path.resolve(__dirname, 'src');
const BUILD_DIR = path.resolve(__dirname, 'dist');
const NODE_MODULES = path.resolve(__dirname, 'node_modules');
const TEMPLATE = path.resolve(__dirname, 'src/templates/index.html');

require("babel-polyfill");

module.exports = {
	context: SRC_DIR,
	/*entry: {
		app: path.resolve(__dirname, 'src/index.js'),
	},*/
	entry: ["babel-polyfill", path.resolve(__dirname, 'src/index.js')],
	output: {
		path: BUILD_DIR,
		publicPath: '/',
		filename: '[name].bundle.[hash].js',
	},
	/*output: {
    	path: BUILD_DIR,  // 输出路径
    	filename: '[name].bundle.[hash].js',  // 输出文件名
    	publicPath: BUILD_DIR, // 必填项
    	chunkFilename : 'routes/[name].chunk.js?[chunkhash:10]', // 按需加载输出的文件名
	},*/
	devtool: 'source-map',
	devServer: {
		contentBase: 'src/template',
		watchContentBase: true,
		historyApiFallback: true,
		hot: true,
		//progress: true,
		https: false,

		//host: '0.0.0.0',
		port: 5000,
		disableHostCheck: true,
		proxy: {
			'/api/v1/questions/*': {
				target: 'http://tiku.afanti100.com',
				host: 'afanti100.com',
				changeOrigin: true
			}
		}
	},
	plugins:[
		new webpack.DefinePlugin({
			'process.env': {
				'NODE_ENV': JSON.stringify('development')
			}
		}),
		new webpack.HotModuleReplacementPlugin(),
		new HtmlWebpackPlugin({
			template: TEMPLATE,
			inject: 'body'
		}),
		new webpack.LoaderOptionsPlugin({
			options: {
				context: __dirname,
				postcss: [
				// bunch of plugins
        		],
      		},
    	}),
    	/*new TransferWebpackPlugin([
    		{from: TEMPLATE},
    		], path.resolve(__dirname, 'src')
    	),*/
	],
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				include: SRC_DIR,
				loader: require.resolve('babel-loader'),
				options: {
					plugins: [
						['import', { libraryName: 'antd', style: 'css' }],
					],
    				// This is a feature of `babel-loader` for webpack (not Babel itself).
   					// It enables caching results in ./node_modules/.cache/babel-loader/
    				// directory for faster rebuilds.
    				cacheDirectory: true
  				}
			},
			{
		        test: /\.(less|scss|sass|css)$/,
		        include: /node_modules/,
		        use: [
		        	'style-loader',
		        	{
		        		loader: 'css-loader'
		        	}
		        ]
		    },
			{
				test: /\.(less|scss|sass|css)$/,
				exclude: /node_modules/,
				use: [
					'style-loader',
					{
						loader: 'css-loader',
						options: {
							localIdentName: '[name]-[local]-[hash:base64:5]',
							modules: true,
							minimize: true,
							camelCase: true,
							importLoaders: 1
						}
					}/*,
					{
						loader: 'postcss-loader'
					}*/
				]
			},
			{
				test: /\.(png|jpg|svg)$/,
				use: {
					loader: 'url-loader'
				}
			}
		],
	},
};