import React, { Component } from 'react';
//import { Tabs } from 'antd';
//const TabPane = Tabs.TabPane;

import Input from 'antd/lib/input';
import 'antd/lib/input/style/css';
const { TextArea } = Input;

import Button from 'antd/lib/button';
import 'antd/lib/button/style/css';

import styles from './index.css';

class SearchQuestion extends Component {
	constructor(props, context) {
		super(props, context);
	}

	render() {
		return (
			<div className={styles['container']}>
				<div className={styles['title']}>输入问题ID:</div>
				<TextArea rows={5} />
				<div className={styles['search']}>
					<Button icon="search">查看</Button>
				</div>
			</div>
		)
	}
}

export default SearchQuestion;