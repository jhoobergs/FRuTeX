import React, { Component } from 'react';
import './Cell.css';

var bgColor = { Default: "#81b71a",
                    Blue: "#00B1E1",
                    Cyan: "#37BC9B",
                    Green: "#8CC152",
                    Red: "#E9573F",
                    Yellow: "#F6BB42",
};

class Cell extends React.Component<{key: string, value: string, color: string}, {value: string, color: string }>  {
    constructor(props: any) {
      super(props);
      this.state = {
        value: props.value,
        color: props.color
      };
  
      this.handleValueChange = this.handleValueChange.bind(this);
      this.handleColorChange = this.handleColorChange.bind(this);
    }

    handleValueChange(value: any) {
        this.setState({
            value: value
        });
    }

    handleColorChange(color: any) {
        this.setState({
            color: color
        });
    }
  
    render() {
      return (
        <td>
            <input type="text" value={this.state.value} style={{backgroundColor: this.state.color}} onChange={(event) =>this.handleValueChange(event.target.value)} />
        </td>
      );
    }
  }

  export default Cell;
