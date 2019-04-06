import React from 'react'
import Cell from './Cell';
import './CellTable.css';

export default class myTable extends React.Component {

  createTable = () => {
    let table = []
    let n: number =  10;
    // Outer loop to create parent
    for (let i = 0; i < n; i++) {
      let children = []
      //Inner loop to create children
      for (let j = 0; j < n; j++) {
        children.push(<Cell></Cell>)
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