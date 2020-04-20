import React, { Component } from "react";
import Card from "./Card";
import axios from "axios";

class NamespaceList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      namespaces: [],
      errorMsg: "",
    };
  }

  componentDidMount() {
    axios
      .get("http://flaskapp:5000/namespaces")
      .then((response) => {
        console.log(response);
        this.setState({ namespaces: response.data });
      })
      .catch((error) => {
        console.log(error);
        this.setState({ errorMsg: "Error retrieving data" });
      });
  }

  render() {
    const { namespaces, errorMsg } = this.state;
    return (
      <div>
        <h1>List of namespaces</h1>
        {namespaces.length
          ? namespaces.map((namespace) => {
              return (
                <div key={namespace.uid}>
                  {" "}
                  <Card name={namespace.name} />{" "}
                </div>
              );
            })
          : null}
        {errorMsg ? <div> {errorMsg} </div> : null}
      </div>
    );
  }
}

export default NamespaceList;
