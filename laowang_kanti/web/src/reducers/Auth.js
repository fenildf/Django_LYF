import { UPDATE_AUTH_INFO } from '../constants';

const AuthReducer = (state = {}, action) => {
	switch (action.type) {
		case UPDATE_AUTH_INFO:
			return {
				data: action.data
			};
			break;
		default:
			return state;
			break;
	}
}

export default AuthReducer;