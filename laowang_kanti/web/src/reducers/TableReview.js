import { UPDATE_QUESTIONS } from '../constants';

const TableReviewReducer = (state = {}, action) => {
	switch (action.type) {
		case UPDATE_QUESTIONS:
			return {
				data: action.data
			};
			break;
		default:
			return state;
			break;
	}
}

export default TableReviewReducer;