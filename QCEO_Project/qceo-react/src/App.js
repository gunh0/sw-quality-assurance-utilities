import React, {Component} from 'react';
import Dashboard from './components/Dashboard'

class App extends Component {
    state = {
        posts: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/defectapi/');
            const posts = await res.json();
            this.setState({posts});
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (<div>
          <Dashboard/>
          </div>);
    }
  }

  export default App;