import React, {Component} from 'react';
import {Router, Route, Switch} from 'react-router-dom';

import history from './history';
import Dashboard from './components/Dashboard'
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';

import {Provider} from 'react-redux';
import {loadUser} from './actions/auth';

import store from './store';

class App extends Component {
    state = {
        posts: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/defect/');
            const posts = await res.json();
            this.setState({posts});
        } catch (e) {
            console.log(e);
        }
        store.dispatch(loadUser());
    }

    render() {
        return (
            <Provider store={store}>
                <Router history={history}>
                    <Switch>
                        <Route exact="exact" path='/' component={Dashboard}/>
                        <Route path='/login' component={LoginForm}/>
                        <Route path='/register' component={RegisterForm}/>
                    </Switch>
                </Router>
            </Provider>
        );
    }
}

export default App;