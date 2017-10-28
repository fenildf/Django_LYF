import { combineReducers } from 'redux';
import TableReviewReducer from './TableReview';
import ContrastReviewReducer from './ContrastReview';

const reducer = combineReducers({
	TableReviewReducer,
	ContrastReviewReducer
});

export default reducer;
