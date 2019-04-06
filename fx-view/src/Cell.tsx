import React, { Component } from 'react';
import './Cell.css';

var bgColor = { Default: "#81b71a",
                    Blue: "#00B1E1",
                    Cyan: "#37BC9B",
                    Green: "#8CC152",
                    Red: "#E9573F",
                    Yellow: "#F6BB42",
};

class Cell extends React.Component<{value: string, color: string}, { value: string, color: string }>  {
    constructor(props: any) {
      super(props);
      this.state = {
        value: props.value,
        color: bgColor.Default
      };
  
      this.handleValueChange = this.handleValueChange.bind(this);
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
        <view>
            <input type="text" value={this.state.value} style={{backgroundColor: this.state.color}} onChange={(event) =>this.handleValueChange(event.target.value)} />
        </view>
      );
    }
  }

  export default Cell;
