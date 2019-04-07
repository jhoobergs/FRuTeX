import { CELLS_FETCH, DATA_RECEIVED} from './actions'

import { call, put, takeLatest, all, cancel, take } from 'redux-saga/effects';
import { request } from 'http';
import { string } from 'prop-types';

const fetchDataPromise = () => {
  return fetch("http://localhost:8000/data")
      .then(response => response.json())
      .catch(function (err) {
        console.log(err)
    });
}

function* postData(payload) {
  const postRequest = yield call(fetch, "http://localhost:8000/data", {
    method: 'POST', headers : {
      'Accept': 'application/json',
      'Content-Type' :'application/json'
    },
    body: payload
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

function* eventWatcher() {
  yield takeLatest('UPDATE_VALUE', (action ) => postData(action.payload))
}

export default function* rootSaga() {
   yield all([
   actionWatcher(),
   eventWatcher()
   ]);
}