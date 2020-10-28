import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { Field, reduxForm } from 'redux-form';

import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';

import { login } from '../actions/auth';

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            {new Date().getFullYear()}
            {' by devgun@github.io All rights reserved.'}
        </Typography>
    );
}

class LoginForm extends Component {
    renderField = ({ input, label, type, meta: { touched, error } }) => {
        return (
            <div className={`field ${touched && error ? 'error' : ''}`}>
                <label>{label}</label>
                <input {...input} type={type} />
                {touched && error && (
                    <span className='ui pointing red basic label'>{error}</span>
                )}
            </div>
        );
    };

    hiddenField = ({ type, meta: { error } }) => {
        return (
            <div className='field'>
                <input type={type} />
                {error && <div className='ui red message'>{error}</div>}
            </div>
        );
    };

    onSubmit = formValues => {
        this.props.login(formValues);
    };

    render() {
        if (this.props.isAuthenticated) {
            return <Redirect to='/' />;
        }
        return (
            <Container>
                <br/>
                <div className='ui segment'>
                    <div className="image-container" align="center">
                        <img src="http://www.lsware.co.kr/resource/images/common/img_logo.png" alt="LSware" align="center"/>
                    </div>
                    <div className="ui inverted divider"></div>
                    <form
                        onSubmit={this.props.handleSubmit(this.onSubmit)}
                        className='ui form'
                    >
                        <Field
                            name='username'
                            type='text'
                            component={this.renderField}
                            label='Username'
                        />
                        <Field
                            name='password'
                            type='password'
                            component={this.renderField}
                            label='Password'
                        />
                        <Field
                            name='non_field_errors'
                            type='hidden'
                            component={this.hiddenField}
                        />
                        <button className='ui primary button'>Login</button>
                        <p style={{ marginTop: '1rem' }}>
                            Don't have an account? <Link to='/register'>Register</Link>
                        </p>
                    </form>
                </div>
                <br/>
                <Copyright />
            </Container>

        );
    }
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

LoginForm = connect(
    mapStateToProps,
    { login }
)(LoginForm);

export default reduxForm({
    form: 'loginForm'
})(LoginForm);
