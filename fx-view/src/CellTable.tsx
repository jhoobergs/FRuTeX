import React from 'react'
import Cell from './Cell';
import './CellTable.css';
import { CELLS_FETCH } from './actions';
import { connect } from 'react-redux';

interface StateProps {

}

interface DispatchProps {
  cellsFetch: () => void
}

type Props = StateProps & DispatchProps


interface State {
  cells: {}
}

class MyTable extends React.PureComponent<Props, State> {
  constructor(props: any) {
    super(props);
  }

  createTable = () => {
    let table = []
    let n: number =  10;
    // Outer loop to create parent
    for (let i = 0; i < n; i++) {
      let children = []
      //Inner loop to create children
      for (let j = 0; j < n; j++) {
        children.push(<Cell value={String(i+j)} color="Cyan"></Cell>)
      }
      //Create the parent and add the children
      table.push(<tr>{children}</tr>)
    }
    return table
  }

  render() {
    return(
      <table>
        {this.createTable()}
      </table>
    )
  }

}


function mapStateToProps (state: any): StateProps {
  return {
    ...state,
    cells: state.cells,
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