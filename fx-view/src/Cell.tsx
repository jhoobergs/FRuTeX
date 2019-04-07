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
  select: () => void
}

type Props = StateProps & DispatchProps

class Cell extends React.Component<Props, any>  {
    constructor(props: any) {
      super(props);
      this.state = {
        value: props.value,
        color: props.color
      };
  
    }
  
    render() {
      return (
        <button>
            <input type="text" readOnly={true} value={this.state.value} style={{backgroundColor: this.state.color}} onClick={this.props.select} />
        </button>
      );
    }
  }

  export default Cell;
