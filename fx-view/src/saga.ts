import { CELLS_FETCH, NEWS_RECEIVED} from './actions'

import { put, takeLatest, all } from 'redux-saga/effects';

async function* fetchNews() {

  console.log('Fetchnews in saga')

  const json = await fetch("http://localhost:8000/data.json")
        .then(response => {console.log(response); return response.json() });    

  console.log(json)
  yield put({ type: NEWS_RECEIVED, cells: json.cells });
}

function* actionWatcher() {
     yield takeLatest(CELLS_FETCH, fetchNews)
}

export default function* rootSaga() {
   yield all([
   actionWatcher(),
   ]);
}