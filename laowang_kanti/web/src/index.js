import React from 'react';
import ReactDOM from 'react-dom';
import { Route, IndexRoute, Router, hashHistory, browserHistory } from 'react-router';
import App from './containers/App';
import Home from './containers/Home';
import Login from './containers/Login';
import Review from './containers/Review';
import { createStore, applyMiddleware } from 'redux';
import { Provider } from 'react-redux';
import thunk from 'redux-thunk'
import { createLogger } from 'redux-logger'
import reducer from './reducers';
import './index.css';

const middleware = [thunk];
if (process.env.NODE_ENV == 'development') {
	console.log("creatrelooger");
	middleware.push(createLogger());
}

const composeEnhancers = (middleware) =>{
  if (process.env.NODE_ENV == 'development') {
  	return (window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose)(middleware)
  } else 
    return middleware
}

const store = composeEnhancers(applyMiddleware(...middleware))(createStore)(reducer, {});

const routesConfig = (
	<Route path='/' component={App}>
		<IndexRoute component={Home} />
		<Route path='/web/' component={Home} />
		<Route path='/web/login' component={Login} />
		<Route path='/web/review' component={Review} />
	</Route>
);

/*const testRoutesConfig = (
	<Route path='/' component={App}>
		<IndexRoute component={Home} />
		<Route path='/paperlist' component={PaperList} />
		<Route path='/paperdetail/:id' component={PaperDetail}></Route>
		<Route path='/questiondetail/:id' component={QuestionDetail}></Route>
	</Route>
);*/

/*const routesConfig = (
	<Route path='/' component={App}>
		<Route path='paperlist'
			   getComponent={(location, cb) => {
			   		require.ensure([], require => {
                   		cb(null, require(PaperList).default)
                	},'paperlist');
             	}} 
        />
        <Route path='paperdetail'
			   getComponent={(location, cb) => {
			   		require.ensure([], require => {
                   		cb(null, require(PaperDetail).default)
                	},'paperdetail');
             	}} 
        />
        <Route path='questiondetail/:id'
			   getComponent={(location, cb) => {
			   		require.ensure([], require => {
                   		cb(null, require(QuestionDetail).default)
                	},'questiondetail');
             	}} 
        />
	</Route>
)*/

ReactDOM.render((
	<Provider store={store}>
		<Router routes={routesConfig} history={browserHistory} />
	</Provider>), 
	document.getElementById('app')
);