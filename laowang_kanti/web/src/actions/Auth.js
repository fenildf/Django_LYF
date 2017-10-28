import { AUTH_USER_INFO, UPDATE_AUTH_INFO, getCookie, removeCookie } from '../constants';

export const authUserInfo = (data) => {
	//let url = '//10.170.251.183:8080/sessions/';
	//10.170.251.183:8080/questions/?
	let url = process.env.NODE_ENV === 'production' ? '/api/v1/sessions/' : '//10.170.251.183:8080/sessions/';
	fetch(url, {
		method: "post",
		body: JSON.stringify(data),
		credentials: 'include'
	}).then(rawresponse => {
		console.log('raw is' + rawresponse);
		return rawresponse.json();
	}).then(response => {
		console.log('response is' + response);
		if (response.meta.status === 0) {
			let cur = new Date();
			cur.setHours(cur.getHours()+18);
			document.cookie = 'user='+data.username+";expires="+cur.toGMTString;
			location.href = '/web/review/';
			dispatch(updateAuthInfo(response.meta));
		}
	}).catch(e => {
		dispatch(updateAuthInfo(null));
	});
}

export const updateAuthInfo = (data) => ({
	type: UPDATE_AUTH_INFO,
	data
})

export const logout = () => {
	//let url = '//10.170.251.183:8080/logout/';
	let url = process.env.NODE_ENV === 'production' ? '/api/v1/logout/' : '//10.170.251.183:8080/logout/';
	fetch(url, {credentials: 'include'}).then(rawresponse => {
		return rawresponse.json();
	}).then(response => {
		console.log(response);
		removeCookie('user');
		location.href = '/web/login';
	}).catch(e => {
		console.log(e)
	});
}
