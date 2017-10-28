import { GET_QUESTIONS, UPDATE_QUESTIONS, removeCookie } from '../../constants';

export const getQuestions = (data) => {
	//let url = '//10.170.251.183:8080/questions/?db_table=question_yingyuzhoubao_20160625&filter_method=random&min_id=4400&max_id=44500';
	let test = '//10.170.251.183:8080/questions/?';
	let url = process.env.NODE_ENV === 'production' ? '/api/v1/questions/?' : '//10.170.251.183:8080/questions/?';
	//http://10.170.251.183:8080/questions/compare/?db_table=question_yingyuzhoubao_20160625&filter_method=random
	for (var field of Object.keys(data)) {
		if (field === 'db_table') {
			url += field+'='+data[field]; 
		} else {
			url += '&'+field+'='+data[field];
		}
		
	}
	return dispatch => {
		fetch(url, {credentials: 'include'}).then(rawResponse => {
			return rawResponse.json();
		}).then(response => {
			if (response.meta.status === 0) {
				dispatch(updateQuestions({data: response.data}));
			} else if (response.meta.status === 1) {
				removeCookie('user');
				location.href = '/web/login';
				dispatch(updateQuestions(null));
			} else {
				dispatch(updateQuestions(null));
			}
		}).catch(e => {
			dispatch(updateQuestions(null));
		});
	}
}

export const updateQuestions = (data) => ({
	type: UPDATE_QUESTIONS,
	data
})
