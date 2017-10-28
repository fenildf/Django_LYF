import React, { Component } from 'react';
import LoginForm from '../../components/LoginForm';

import styles from './index.css';

class Login extends Component {
	constructor(props, context) {
		super(props, context);
	}

	render() {
		return (
			<div className={styles['login-wrapper']}>
				<LoginForm />
			</div>
		)
	}
}

export default Login;