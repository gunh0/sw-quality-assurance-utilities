import React, {Component} from 'react';
import { Router, Route, Switch } from 'react-router-dom';

import Dashboard from './components/Dashboard'
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';
import PrivateRoute from './common/PrivateRoute';

import { loadUser } from './actions/auth';
import { Provider } from 'react-redux';

import store from './store';
import history from './history';

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
                        <PrivateRoute exact="exact" path='/' component={Dashboard}/>
                        <Route exact="exact" path='/dashboard' component={Dashboard}/>
                        <Route exact="exact" path='/login' component={LoginForm}/>
                        <Route exact="exact" path='/register' component={RegisterForm}/>
                    </Switch>
                </Router>
            </Provider>
        );
    }
}

export default App;