import React, { Component } from 'react';
import './Cell.css';

export const bgColor = { Default: "#81b71a",
                    Blue: "#00B1E1",
                    Cyan: "#37BC9B",
                    Green: "#8CC152",
                    Red: "#E9573F",
                    Yellow: "#F6BB42",
};

interface StateProps {
  key: string,
  value: string,
  color: string
}

interface DispatchProps {
  updateValue: (attrib: string, value: string) => void
}

type Props = StateProps & DispatchProps

class Cell extends React.Component<Props, any>  {
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
        this.props.updateValue("content", this.state.value);
    }

    handleColorChange(color: any) {
        this.setState({
            color: color
        });
    }
  
    render() {
      return (
        <button>
            <input type="text" value={this.state.value} style={{backgroundColor: this.state.color}} onChange={(event) =>this.handleValueChange(event.target.value)} />
        </button>
      );
    }
  }

  export default Cell;
