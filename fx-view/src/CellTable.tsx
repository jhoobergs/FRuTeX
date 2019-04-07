import React from 'react'
import Cell, { bgColor } from './Cell';
import './CellTable.css';
import { CELLS_FETCH } from './actions';
import { connect } from 'react-redux';
import { watchFile } from 'fs';
import { select } from 'redux-saga/effects';

interface StateProps {
  cells: { [key: string]: {
    content: string[],
    color: string[]
  } }
  loading: boolean
  selection: number[],
  contentValue: string,
  colorValue: string
}

interface DispatchProps {
  cellsFetch: () => any
  updateValue: (row: number, col: number, attrib: string, value: string) => any
  select: (row: number, col: number) => void
  changeContent: (val: string) => void
  changeColor: (val: string) => void
}

type Props = StateProps & DispatchProps


interface State {
}

class MyTable extends React.PureComponent<Props, State> {
  constructor(props: any) {
    super(props);
    this.props.cellsFetch();
    this.state = {
    }

    this.handleValueChange = this.handleValueChange.bind(this);
    this.handleValueKeyPress = this.handleValueKeyPress.bind(this);
    this.handleColorChange = this.handleColorChange.bind(this);
    this.handleColorKeyPress = this.handleColorKeyPress.bind(this);
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
        children.push(<Cell select={() => this.props.select(i,j)} key ={k.toString()} value={(this.props.cells[`${i}, ${j}`] || {content:["",""]}).content[0]} color={(this.props.cells[`${i}, ${j}`] || {color: [bgColor.Default, ""]}).color[0]}></Cell>)
        k += 1
      }
      //Create the parent and add the children
      table.push(<tr key ={k.toString()}>{children}</tr>)
    }
    return table
  }

  handleValueChange(event: any) {
    this.setState({
        contentValue: event.target.value
    });
  }

  handleValueKeyPress(event: any) {
    if(event.key == "Enter")
      this.props.updateValue(this.props.selection[0], this.props.selection[1], "content", event.target.value);
  }

  handleColorChange(event: any) {

    this.setState({
        colorValue: event.target.value
    });
  }

  handleColorKeyPress(event: any) {
    if(event.key == "Enter")
      this.props.updateValue(this.props.selection[0], this.props.selection[1], "color", event.target.value);
  }

  render() {
    console.log(JSON.stringify(this.props.cells))
    console.log(this.props.selection)
    let content = <h1>Loading</h1>
    if(! this.props.loading){
      content = <div className="top"><table>
      <tbody>
      {this.createTable()}
      </tbody>
    </table>
    <div className="sidebar">
      <div className="inputs">
      <textarea className="content" name="content" cols={40} rows={3} onKeyPress={(event) =>this.handleValueKeyPress(event)}></textarea>
      <textarea className="content" name="content" cols={40} rows={3} value={this.props.contentValue}></textarea>
      <textarea className="color" name="color" cols={40} rows={3}  onKeyPress={(event) =>this.handleColorKeyPress(event)}></textarea>
      <textarea className="color" name="color" cols={40} rows={3} value={this.props.colorValue}></textarea> 
      </div>
    </div>
    </div>
    } //  onChange={(event) =>this.handleColorChange(event)} | onChange={(event) =>this.handleValueChange(event)}

    return(
      content
    );
  }
}


function mapStateToProps (state: any): StateProps {
  console.log('here')
  return {
    cells: state.cells,
    loading: state.loading,
    selection: state.selection,
    contentValue: state.contentValue, //,
    colorValue: state.colorValue, //
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
    },
    select(row: number, col: number) {
      console.log(`CHANGE_SELECTION ${row} ${col}`)
      dispatch({type: 'CHANGE_SELECTION', payload: {
        row, col
      }})
    },
    changeContent(val: string) {
      dispatch({type: 'CHANGE_CONTENT', payload: {
        val
      }})
    },
    changeColor(val: string) {
      dispatch({type: 'CHANGE_COLOR', payload: {
        val
      }})
    }
  }
}

export default connect<StateProps, DispatchProps, {}>(
  mapStateToProps,
  mapDispatchToProps,
)(MyTable)