import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getQuestions } from '../../actions/';
//import { Tabs } from 'antd';
//const TabPane = Tabs.TabPane;
//
import Form from 'antd/lib/form';
import 'antd/lib/form/style/css';
const FormItem = Form.Item;

import Input from 'antd/lib/input';
import 'antd/lib/input/style/css';

import Button from 'antd/lib/button';
import 'antd/lib/button/style/css';

import Select from 'antd/lib/select';
import 'antd/lib/select/style/css';
const Option = Select.Option; 

import styles from './index.css';

class ProtoTableReview extends Component {
	constructor(props, context) {
		super(props, context);
		this.handleModeChange = this.handleModeChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
		this.handleClick = this.handleClick.bind(this);
		this.state = {
			mode: "range",
			filter_method: "random"
		};
		//props.dispatch(getQuestions());
	}

	handleModeChange(value) {
		this.setState({
			mode: value
		});
	}

	handleUpdate = (values) => {
		//校验数据并dispatch
        var data;
        if (this.state.mode === 'range') {
        	//指定范围
        	if (this.state.filter_method === 'random') {
        		data = {
    				db_table: values.db_table,
    				filter_method: 'random'
    			}
        		values.min_id && values.max_id && (data = {
    				...data,
    				min_id: parseInt(values.min_id),
    				max_id: parseInt(values.max_id)
    			});
        		console.log(data);
	        } else if (this.state.filter_method === 'asc') {
	        	if (values.min_id) {
	        		data = {
		        		db_table: values.db_table,
        				filter_method: 'asc',
        				min_id: parseInt(values.min_id)		
	        		}
	        	}
	        } else if (this.props.data && this.props.data.length === 2) {
	        	data = {
    				db_table: values.db_table,
	        		filter_method: this.state.filter_method
	        	}
                if (this.state.filter_method === 'next'){
	        		data['current_question_id'] = this.props.data[1].question_id
                } else {
	        		data['current_question_id'] = this.props.data[0].question_id
                }
	        }
        } else {
        	//指定url
        	data = {
        		db_table: values.db_table,
        		question_url: values.question_url
        	}
        }
        //dispatch数据
        data && this.props.dispatch(getQuestions(data));
	}

	handleSubmit = (e) => {
		e.preventDefault();
	    this.props.form.validateFields((err, values) => {
	      if (!err) {
	        console.log('Received values of form: ', values);
	        this.handleUpdate(values);
	      }
	    });
	}

	handleClick = (e) => {
		e.preventDefault();
		//获取当前顺序并校验提交数据
		this.setState({
			filter_method: e.target.getAttribute('data-value')
		}, ()=>{
			this.props.form.validateFields((err, values) => {
				if (!err) {
			        console.log('Received values of form2: ', values);
			        //校验数据并dispatch
			        this.handleUpdate(values);
			      }
			});	
		});
		
	}

	componentDidUpdate() {
		if (this.props.data && this.props.data.length === 2) {
			this.refs.iframe1.contentDocument.open();
			this.refs.iframe1.contentDocument.write(this.props.data[0].html);
			this.refs.iframe1.contentDocument.close();
			this.refs.iframe2.contentDocument.open();
			this.refs.iframe2.contentDocument.write(this.props.data[1].html);
			this.refs.iframe2.contentDocument.close();
		}
	}

	render() {
		const { getFieldDecorator } = this.props.form;
		var questionID1, questionID2, questionHtml1, questionHtml2;
		if (this.props.data && this.props.data.length === 2) {
			questionID1 = this.props.data[0].question_id;
			questionID2 = this.props.data[1].question_id;
			questionHtml1 = this.props.data[0].html;
			questionHtml2 = this.props.data[1].html;
		} else {
			questionID1 = 0;
			questionID2 = 0;
			questionHtml1 = '';
			questionHtml2 = '';
		}
		return (
			<Form onSubmit={this.handleSubmit} className={styles['container']}>
				<div className={styles['line-group']}>
					<FormItem className={styles['first-comp']}>
						{getFieldDecorator('db_table', {
            				rules: [{ required: true, message: '请输入表名!' }],
          				})(
							<Input size="large" placeholder="请输入表名" onChange={this.handleTableChange} />
						)}
					</FormItem>
					<Button className={styles['last-comp']} type="primary" htmlType="submit">搜索</Button>
				</div>
				<div className={styles['line-group']}>
					<Select className={styles['first-comp']} defaultValue="range" onChange={this.handleModeChange}>
						<Option value="range">限定区间</Option>
						<Option value="url">指定URL</Option>
					</Select>
					<div className={ styles['inline'] + (this.state.mode === "range" ? '' : ' hidden')} >
						<FormItem className={styles['first-comp'] + ' ' + styles['form-input']}>
							{getFieldDecorator('min_id', {
	            				rules: [{ required: false }],
	          				})(
								<Input className={styles['m-comp']} size="large" />
							)}
						</FormItem>
						到
						<FormItem className={styles['m-comp'] + ' ' + styles['form-input']}>
							{getFieldDecorator('max_id', {
	            				rules: [{ required: false }],
	          				})(
								<Input className={styles['m-comp']} size="large" />
							)}
						</FormItem>
						<Button className={styles['m-comp']} 
								onClick={this.handleClick} 
								data-value="asc" 
								type={this.state.filter_method==='asc' ? 'default': 'dashed'}>顺序排列</Button>
						<Button className={styles['last-comp']} 
								onClick={this.handleClick} 
								data-value="random"
								type={this.state.filter_method==='random' ? 'default': 'dashed'}>随机</Button>
					</div>
					<div className={ styles['inline'] + (this.state.mode === "url" ? '' : ' hidden')} >
						<FormItem className={styles['m-comp'] + ' ' + styles['form-input']}>
							{getFieldDecorator('question_url', {
	            				rules: [{ required: false }],
	          				})(
								<Input size="large" />
							)}
						</FormItem>
						<Button className={styles['last-comp']} htmlType="submit">确定</Button>
					</div>
				</div>
				<div className={ styles['iframe-group']} >
					<Button className={styles['slick-left'] + (this.state.mode === "range" ? '' : ' hidden')} 
							icon="caret-left" 
							onClick={this.handleClick} 
							data-value="previous"
							type={this.state.filter_method==='previous' ? 'default': 'dashed'}></Button>
					<div className={styles['left-iframe']}>
						<div className={styles['question-id-wrapper']}>
							<label>Question ID:</label>
							<span>{questionID1}</span> 
						</div>
						<iframe ref='iframe1'>
						</iframe>
					</div>
					<div className={styles['right-iframe']}>
						<div className={styles['question-id-wrapper']}>
							<label>Question ID:</label>
							<span>{questionID2}</span>
						</div>
						<iframe ref='iframe2'>
						</iframe>
					</div>
					<Button className={styles['slick-right'] + (this.state.mode === "range" ? '' : ' hidden')} 
							icon="caret-right" 
							onClick={this.handleClick} 
							data-value="next"
							type={this.state.filter_method==='next' ? 'default': 'dashed'}></Button>
				</div>
			</Form>
		)
	}
}

const TableReview = Form.create()(ProtoTableReview);

const mapStateToProps = (state) => {
	return state.TableReviewReducer.data;
}

export default connect(mapStateToProps)(TableReview);
