import { CELLS_FETCH, DATA_RECEIVED} from './actions'

import { call, put, takeLatest, all, cancel, take } from 'redux-saga/effects';

const fetchDataPromise = () => {
  return fetch("http://localhost:8000/data.json")
      .then(response => response.json())
      .catch(function (err) {
        console.log(err)
    });
}

function* fetchData() {
  console.log('Fetchdata in saga')
  const json = yield call(fetchDataPromise);

  console.log(`Data: ${JSON.stringify(json)}`)
  yield put({ type: 'DATA_RECEIVED', cells: json.cells });
}

function* actionWatcher() {
     yield takeLatest('CELLS_FETCH', fetchData)
}

export default function* rootSaga() {
   yield all([
   actionWatcher(),
   ]);
}