import React, { Component } from 'react';

import Form from 'antd/lib/form';
import 'antd/lib/form/style/css';
const FormItem = Form.Item;

import Input from 'antd/lib/input';
import 'antd/lib/input/style/css';

import Icon from 'antd/lib/icon';
import 'antd/lib/icon/style/css';

import Button from 'antd/lib/button';
import 'antd/lib/button/style/css';

import styles from './index.css';

import { authUserInfo } from '../../actions/';

class ProtoLoginForm extends Component {
	constructor(props, context) {
		super(props, context);
	}

	handleSubmit = (e) => {
		e.preventDefault();
	    this.props.form.validateFields((err, values) => {
	      if (!err) {
	        console.log('Received values of form: ', values);
	        this.props.dispatch(authUserInfo(values));
	      }
	    });
	}

	render() {
		const { getFieldDecorator } = this.props.form;
		return (
			<Form onSubmit={this.handleSubmit} className="login-form">
		        <FormItem>
		          {getFieldDecorator('username', {
		            rules: [{ required: true, message: '请输入用户名！' }],
		          })(
		            <Input prefix={<Icon type="user" style={{ fontSize: 13 }} />} placeholder="用户名" />
		          )}
		        </FormItem>
		        <FormItem>
		          {getFieldDecorator('password', {
		            rules: [{ required: true, message: '请输入密码！' }],
		          })(
		            <Input prefix={<Icon type="lock" style={{ fontSize: 13 }} />} type="password" placeholder="密码" />
		          )}
		        </FormItem>
		        <Button type="primary" htmlType="submit" className={styles["login-form-button"]}>
		           登录
		         </Button>
		    </Form>
		)
	}
}

const LoginForm = Form.create()(ProtoLoginForm);

export default LoginForm;