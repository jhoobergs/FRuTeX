import { CELLS_FETCH, NEWS_RECEIVED} from './actions'

export const initialState: any = {
  loading: true,
  cells: {}
}

export default function reducer (state: any = initialState, action: any): any {
  console.log("I am at the reducer.")
  switch (action.type) {
    case CELLS_FETCH:
      console.log('I am at Cells_fetch')
      return {
        ...state,
        loading: true
      }
    case NEWS_RECEIVED:
      console.log('I am at News_Received')
      return {
        ...state, cells: action.cells, loading: false
      }
    default:
      return state
  }
}
