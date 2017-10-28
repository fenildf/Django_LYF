import { GET_SIMILAR_QUESTIONS, UPDATE_SIMILAR_QUESTIONS } from '../constants';

export const getSimilarQuestions = (data) => {
	//let url = '//10.170.251.183:8080/questions/?db_table=question_yingyuzhoubao_20160625&filter_method=random&min_id=4400&max_id=44500';
	//let test = '//10.170.251.183:8080/questions/compare/?';
	let url = process.env.NODE_ENV === 'production' ? '/api/v1/questions/compare/?' : '//10.170.251.183:8080/questions/compare/?';
	for (var field of Object.keys(data).sort()) {
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
				dispatch(updateSimilarQuestions({data: response.data}));
			} if (response.meta.status === 1) {
				removeCookie('user');
				location.href = '/web/login';
				dispatch(updateSimilarQuestions(null));
			} else {
				dispatch(updateSimilarQuestions(null));
			}
		}).catch(e => {
			dispatch(updateSimilarQuestions(null));
		});
	}
}

export const updateSimilarQuestions = (data) => ({
	type: UPDATE_SIMILAR_QUESTIONS,
	data
})
