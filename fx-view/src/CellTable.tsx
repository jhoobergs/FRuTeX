import React from 'react'
import Cell, { bgColor } from './Cell';
import './CellTable.css';
import { CELLS_FETCH } from './actions';
import { connect } from 'react-redux';
import { watchFile } from 'fs';

interface StateProps {
  cells: { [key: string]: {
    content: string,
    color: string
  } }
  loading: boolean
}

interface DispatchProps {
  cellsFetch: () => any
  updateValue: (row: number, col: number, attrib: string, value: string) => any
}

type Props = StateProps & DispatchProps


interface State {
  
}

class MyTable extends React.PureComponent<Props, State> {
  constructor(props: any) {
    super(props);
    this.props.cellsFetch();
  }

  createTable = () => {
    let table = []
    let n: number =  10;
    let k: number = 0;
    // Outer loop to create parent
    for (let i = 0; i < n; i++) {
      let children = []
      //Inner loop to create children
      for (let j = 0; j < n; j++) {
        children.push(<Cell updateValue={(attrib: string, value: string) => this.props.updateValue(i,j, attrib, value)} key ={k.toString()} value={(this.props.cells[`${i}, ${j}`] || {content:""}).content} color={(this.props.cells[`${i}, ${j}`] || {color: bgColor.Default}).color}></Cell>)
        k += 1
      }
      //Create the parent and add the children
      table.push(<tr key ={k.toString()}>{children}</tr>)
    }
    return table
  }

  render() {
    let content = <h1>Loading</h1>
    if(! this.props.loading){
      content = <table>
      <tbody>
      {this.createTable()}
      </tbody>
    </table>
    }

    return(
      content
    );
  }
}


function mapStateToProps (state: any): StateProps {
  console.log('here')
  console.log(JSON.stringify(state.cells))
  return {
    cells: state.cells,
    loading: state.loading
  }
}

  
function mapDispatchToProps (dispatch: any): DispatchProps {
  return {
    cellsFetch () {
      console.log('Dispatching')
      dispatch({type: 'CELLS_FETCH'})
    }, updateValue(row: number, col: number, attrib: string, value: string) {
      dispatch({type: 'UPDATE_VALUE', payload: {
        row, col, attrib, expr: value
      }})
    }
  }
}

export default connect<StateProps, DispatchProps, {}>(
  mapStateToProps,
  mapDispatchToProps,
)(MyTable)