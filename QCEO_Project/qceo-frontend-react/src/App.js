import React, { Component } from 'react';
import { Router, Route, Switch } from 'react-router-dom';

import history from './history';
import Main from './layout/Main';

import RegisterForm from './Authentication/RegisterForm';
import LoginForm from './Authentication/LoginForm';

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
                    <Main />
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
