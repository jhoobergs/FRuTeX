import React, { Component } from 'react';
import { Provider } from 'react-redux'
import './App.css';
import MyTable from './CellTable'

import store from './store'

// const loadingSelector = createLoadingSelector([ACCOUNT_FETCH_LOGIN, ACCOUNT_FETCH_REGISTER, ACCOUNT_INIT_USER])

class WrappedApp extends React.Component {
  render () {
    return (
      <Provider store={store}>
        <MyTable></MyTable>
      </Provider>
    )
  }
}
console.log('At my table')
export default WrappedApp
