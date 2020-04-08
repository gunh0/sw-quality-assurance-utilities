import React, {Component} from 'react';
import {Link, Router, Route, Switch} from 'react-router-dom';

import history from './history';
import Dashboard from './components/Dashboard'
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';

import {Provider} from 'react-redux';
import {loadUser} from './actions/auth';

import store from './store';

class App extends Component {

    componentDidMount() {
        store.dispatch(loadUser());
    }

    render() {
        return (
            <Provider store={store}>
                <Router history={history}>
                    <header>
                        <Link to="/">
                            <button>Home</button>
                        </Link>
                        <Link to="/login">
                            <button>login</button>
                        </Link>
                        <Link to="/register">
                            <button>register</button>
                        </Link>
                    </header>
                    <main>
                        <Switch>
                            <Route exact="exact" path='/' component={Dashboard}/>
                            <Route path='/login' component={LoginForm}/>
                            <Route path='/register' component={RegisterForm}/>
                        </Switch>
                    </main>
                </Router>
            </Provider>
        );
    }
}

export default App;