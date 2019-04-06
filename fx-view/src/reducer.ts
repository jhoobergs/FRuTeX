import { CELLS_FETCH, NEWS_RECEIVED} from './actions'

export const initialState: any = {
  loading: true,
  cells: {}
}

export default function reducer (state: any = initialState, action: any): any {
  switch (action.type) {
    case CELLS_FETCH:
      return {
        ...state,
        loading: true
      }
    case NEWS_RECEIVED:
      return {
        ...state, cells: action.json[0], loading: false
      }
    default:
      return state
  }
}
