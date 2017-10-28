import React, { Component } from 'react';
//import { Tabs } from 'antd';
//const TabPane = Tabs.TabPane;
import Tabs from 'antd/lib/tabs';
import 'antd/lib/tabs/style/css';
const TabPane = Tabs.TabPane;

import SearchQuestion from '../SearchQuestion';
import TableReview from '../TableReview';
import ContrastReview from '../ContrastReview';

class Review extends Component {
	constructor(props, context) {
		super(props, context);
	}

	render() {
		return (
			<Tabs defaultActiveKey="1">
				<TabPane tab="题目查看" key="1">
					<SearchQuestion />
				</TabPane>
				<TabPane tab="表单查看" key="2">
					<TableReview />
				</TabPane>
				<TabPane tab="对比查看" key="3">
					<ContrastReview />
				</TabPane>
			</Tabs>
		)
	}
}

export default Review;