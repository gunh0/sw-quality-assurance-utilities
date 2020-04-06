import React, { Component } from 'react';
import Button from '@material-ui/core/Button';

class App extends Component {
  state = {
    posts: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/defectapi/');
      const posts = await res.json();
      this.setState({
        posts
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.posts.map(item => (
          <div key={item.num}>
            <h3>{item.num}</h3>
            <h3>{item.title}</h3>
            <Button variant="contained" color="primary">
                Check
            </Button>
          </div>
        ))}
        
      </div>
    );
  }
}

export default App;