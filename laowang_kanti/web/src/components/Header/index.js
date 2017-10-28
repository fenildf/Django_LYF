import React, { Component } from 'react';
import { connect } from 'react-redux';

import Icon from 'antd/lib/icon';
import 'antd/lib/icon/style/css';

import Button from 'antd/lib/button';
import 'antd/lib/button/style/css';

import styles from './index.css';

import { logout } from '../../actions/';

import { getCookie } from '../../constants';

class Header extends Component {
	constructor(props, context) {
		super(props, context);
		this.handleLogout = this.handleLogout.bind(this);
	}

	handleLogout = (e) => {
		//this.props.dispatch(logout);
		logout();
	}

	render() {
		let user = getCookie('user');
		if (user) {
			return (
				<div className={styles['header']}>
					<Icon className={styles['user-icon']} type="user" style={{ fontSize: 13 }} />
					<div className={styles['user-name']}>{user}</div>
					<Button onClick={this.handleLogout}>退出登录</Button>
				</div>
			)
		} else {
			return (
				<div></div>
			)
		}
		
	}
}

export default Header;
/*const mapStateToProps = (state) => {
	return state.ContrastReviewReducer.data;
}

export default connect(mapStateToProps)(ContrastReview);*/