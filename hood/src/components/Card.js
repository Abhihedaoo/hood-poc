import React, { Component } from "react";
import './Card.css'

class Card extends Component {
    
  render() {
    return (
      <div class="card">
        <div class="container">
          <h4>
            <b>{this.props.name}</b>
          </h4>
        </div>
      </div>
    );
  }
}

export default Card;
