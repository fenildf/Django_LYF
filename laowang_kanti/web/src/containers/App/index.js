import React, { Component } from 'react';
import Header  from '../../components/Header';
/*import Footer from '../../components/Footer';
import AdvertBanner from '../../components/AdvertBanner';
import styles from './index.css';*/

class App extends Component {
	constructor(props, context) {
		super(props, context);
	}

	render() {
		return (
			<div>
				<Header />
				<div>
				{this.props.children}
				</div>
			</div>
		)
	}
}

export default App;