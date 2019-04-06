import { createStore, applyMiddleware } from 'redux';
import { logger } from 'redux-logger';
import reducer from './reducer';
import createSagaMiddleware from '@redux-saga/core';
import rootSaga from './saga';


const sagaMiddleware = createSagaMiddleware();

const store = createStore(
    reducer,
    applyMiddleware(sagaMiddleware, logger),
 );

 sagaMiddleware.run(rootSaga);

 export default store