import { UPDATE_SIMILAR_QUESTIONS } from '../constants';

const ContrastReviewReducer = (state = {}, action) => {
	switch (action.type) {
		case UPDATE_SIMILAR_QUESTIONS:
			return {
				data: action.data
			};
			break;
		default:
			return state;
			break;
	}
}

export default ContrastReviewReducer;