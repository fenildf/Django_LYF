import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getSimilarQuestions } from '../../actions/';
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

class ProtoContrastReview extends Component {
	constructor(props, context) {
		super(props, context);
		//this.handleModeChange = this.handleModeChange.bind(this);
		//this.handleTableChange = this.handleTableChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
		this.handleClick = this.handleClick.bind(this);
		this.state = {
			mode: "range",
			filter_method: 'random'
		};
	}

	/*handleModeChange(value) {
		this.setState({
			mode: value
		});
	}*/

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
	        } else if (values.min_id && values.max_id && this.props.data && this.props.data.length === 2) {
	        	data = {
	        		min_id: parseInt(values.min_id),
	        		max_id: parseInt(values.max_id),
	        		current_question_id: this.props.data[0].question_id,
	        		filter_method: this.state.filter_method
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
        data && this.props.dispatch(getSimilarQuestions(data));
	}

	handleClick = (e) => {
		e.preventDefault();
		let new_mode = e.target.getAttribute('data-mode');
		let new_filter_method = e.target.getAttribute('data-value');
		this.setState({
			mode: new_mode ? new_mode : this.state.mode,
			filter_method: new_mode === 'url' ? this.state.filter_method : new_filter_method
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

	handleSubmit = (e) => {
		e.preventDefault();
	    this.props.form.validateFields((err, values) => {
	      if (!err) {
	        console.log('Received values of form: ', values);
	        this.handleUpdate(values);
	      }
	    });
	}

	componentDidUpdate() {
		if (this.props.data) {
			this.refs.iframe1.contentDocument.open();
			this.refs.iframe1.contentDocument.write(this.props.data.question.html);
			this.refs.iframe1.contentDocument.close();
			this.refs.iframe2.contentDocument.open();
			this.refs.iframe2.contentDocument.write(this.props.data.reference_question.html);
			this.refs.iframe2.contentDocument.close();
		}
	}

	render() {
		const { getFieldDecorator } = this.props.form;
		var questionID1, questionID2, questionHtml1, questionHtml2;
		if (this.props.data) {
			questionID1 = this.props.data.question.question_id;
			questionID2 = this.props.data.reference_question.question_id;
			questionHtml1 = this.props.data.question.html;
			questionHtml2 = this.props.data.reference_question.html;
		} else {
			questionID1 = 0;
			questionID2 = 0;
			questionHtml1 = '';
			questionHtml2 = '';
		}
		return (
			<Form onSubmit={this.handleSubmit} className={styles['container']}>
				<div className={styles['line-group']}>
					<FormItem className={styles['first-comp'] + ' ' + styles['form-input']}>
						{getFieldDecorator('db_table', {
            				rules: [{ required: true, message: '请输入表名!' }],
          				})(
							<Input size="large" placeholder="请输入表名" onChange={this.handleTableChange} />
						)}
					</FormItem>
					<Button className={styles['last-comp']} type="primary" htmlType="submit">搜索</Button>
				</div>
				<div className={styles['line-group']}>
					<label className={styles['first-comp']}>限定区间</label>
					<div className={ styles['inline'] }>
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
						<Button className={styles['m-comp']} data-value="asc" onClick={this.hanldeClick}>顺序排列</Button>
						<Button className={styles['last-comp']} data-value="random" onClick={this.handleClick}>随机</Button>
					</div>
				</div>
				<div className={styles['line-group']}>
					<label className={styles['first-comp']}>指定URL</label>
					<div className={ styles['inline'] }>
						<FormItem className={styles['m-comp'] + ' ' + styles['form-input']}>
							{getFieldDecorator('question_url ', {
	            				rules: [{ required: false }],
	          				})(
								<Input size="large" />
							)}
						</FormItem>
						<Button className={styles['last-comp']} data-mode="url" onClick={this.handleClick}>确定</Button>
					</div>
				</div>
				<div className={ styles['iframe-group']} >
					<Button className={styles['slick-left'] + (this.state.mode === "range" ? '' : ' hidden')} 
							icon="caret-left"
							data-value="previous" 
							onClick={this.handleClick}></Button>
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
							data-value="next" 
							onClick={this.handleClick}></Button>
				</div>
			</Form>
		)
	}
}

const ContrastReview = Form.create()(ProtoContrastReview);

const mapStateToProps = (state) => {
	return state.ContrastReviewReducer.data;
}

export default connect(mapStateToProps)(ContrastReview);