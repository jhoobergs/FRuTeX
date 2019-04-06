import { CELLS_FETCH, NEWS_RECEIVED} from './actions'

import { put, takeLatest, all } from 'redux-saga/effects';

function* fetchNews() {

  const json = yield fetch("http://localhost:8000/data.json")
        .then(response => response.json(), );    

  yield put({ type: NEWS_RECEIVED, json: json.articles, });
}

function* actionWatcher() {
     yield takeLatest(CELLS_FETCH, fetchNews)
}

export default function* rootSaga() {
   yield all([
   actionWatcher(),
   ]);
}