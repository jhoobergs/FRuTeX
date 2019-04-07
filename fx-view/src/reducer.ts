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
    case 'CHANGE_SELECTION':
    console.log('I am at CHANGE SELECTION')
    return {
      ...state,
      selection: [action.payload.row, action.payload.col],
      contentValue: state.selection ? (state.cells[`${action.payload.row}, ${action.payload.col}`] || {content: ["",""]} ).content[1] : "",
      colorValue: state.selection ? (state.cells[`${action.payload.row}, ${action.payload.col}`] || {color: ["",""]} ).color[1] : "",
    }
    case 'CHANGE_CONTENT':
    console.log('I am at CHANGE_CONTENT')
    return {
      ...state,
      contentValue: action.payload.val
    }
    case 'CHANGE_COLOR':
    console.log('I am at CHANGE_COLOR')
    return {
      ...state,
      colorValue: action.payload.val
    }
    default:
      return state
  }
}
