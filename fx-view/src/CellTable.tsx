import React from 'react'
import Cell from './Cell';
import './CellTable.css';
import { CELLS_FETCH } from './actions';
import { connect } from 'react-redux';
import { watchFile } from 'fs';

function isEmpty(obj: any) {
  for(var key in obj) {
      if(obj.hasOwnProperty(key))
          return false;
  }
  return true;
}

interface StateProps {
  cells: { [key: string]: {
    content: string,
    color: string
  } }
  loading: boolean
}

interface DispatchProps {
  cellsFetch: () => any
}

type Props = StateProps & DispatchProps


interface State {
  
}

class MyTable extends React.PureComponent<Props, State> {
  constructor(props: any) {
    super(props);
    /*this.state = {
      cells: this.props.cellsFetch()
    };*/
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
        children.push(<Cell key ={k.toString()} value={this.props.cells[`${i},${j}`].content} color={this.props.cells[`${i},${j}`].color}></Cell>)
        k += 1
      }
      //Create the parent and add the children
      table.push(<tr key ={k.toString()}>{children}</tr>)
    }
    return table
  }

  render() {
    return(<div>
      if (this.props.loading) {
        <h1>Loading</h1>
      } else {
      <table>
        <tbody>
        {this.createTable()}
        </tbody>
      </table>
      }
      </div>
    );
  }
}


function mapStateToProps (state: any): StateProps {
  console.log('here')
  console.log(state.cells)
  return {
    cells: state.cells,
    loading: state.loading
  }
}

  
function mapDispatchToProps (dispatch: any): DispatchProps {
  return {
    cellsFetch () {
      dispatch({ type: CELLS_FETCH })
    },
  }
}

export default connect<StateProps, DispatchProps, {}>(
  mapStateToProps,
  mapDispatchToProps,
)(MyTable)