import React, { Component } from 'react';
import { Router, Route, Switch } from 'react-router-dom';

import history from './history';
import Header from './layout/Header';

import RegisterForm from './auth/RegisterForm';
import LoginForm from './auth/LoginForm';

import { Provider } from 'react-redux';
import store from './store';
import PrivateRoute from './common/PrivateRoute';
import { loadUser } from './actions/auth';
import Dashboard from './Dashboard/Dashboard';

class App extends Component {

    componentDidMount() {
        store.dispatch(loadUser());
    }

    render() {
        return (
            <Provider store={store}>
                <Router history={history}>
                    <Header />
                    <Switch>
                        <PrivateRoute exact path='/' component={Dashboard} />
                        <Route exact path='/register' component={RegisterForm} />
                        <Route exact path='/login' component={LoginForm} />
                    </Switch>
                </Router>
            </Provider>
        );
    }
}

export default App;
