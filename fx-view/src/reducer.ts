import { CELLS_FETCH, DATA_RECEIVED} from './actions'

export const initialState: any = {
  loading: true,
  cells: {}
}

export default function reducer (state: any = initialState, action: any): any {
  console.log("I am at the reducer.")
  switch (action.type) {
    case 'CELLS_FETCH':
      console.log('I am at Cells_fetch')
      return {
        ...state,
        loading: true
      }
    case 'DATA_RECEIVED':
      console.log('I am at Data_Received')
      return {
        ...state, cells: action.cells, loading: false
      }
    case 'UPDATE_VALUE':
    console.log('I am at UPDATE_VALUE')
    return {
      ...state,
      loading: true
    }
    default:
      return state
  }
}
