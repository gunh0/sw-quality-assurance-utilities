import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { Field, reduxForm } from 'redux-form';
import { register } from '../actions/auth';

import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';

function Copyright() {
    return (
      <Typography variant="body2" color="textSecondary" align="center">
        {'Copyright © '}
        {new Date().getFullYear()}
        {' by devgun@github.io All rights reserved.'}
      </Typography>
    );
  }

class RegisterForm extends Component {
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

    onSubmit = formValues => {
        this.props.register(formValues);
    };

    render() {
        if (this.props.isAuthenticated) {
            return <Redirect to='/' />;
        }
        return (
            <Container className='ui container'>
                <br/>
                
                <div className='ui segment'>
                <div class="image-container" align="center">
                        <img src="http://www.lsware.co.kr/resource/images/common/img_logo.png" alt="LSware" align="center"/>
                    </div>
                    <div class="ui inverted divider"></div>
                    <form
                        onSubmit={this.props.handleSubmit(this.onSubmit)}
                        className='ui form'
                    >
                        <Field
                            name='username'
                            type='text'
                            component={this.renderField}
                            label='Username'
                            validate={[required, minLength3, maxLength15]}
                        />
                        <Field
                            name='email'
                            type='email'
                            component={this.renderField}
                            label='Email'
                            validate={required}
                        />
                        <Field
                            name='password'
                            type='password'
                            component={this.renderField}
                            label='Password'
                            validate={required}
                        />
                        <Field
                            name='password2'
                            type='password'
                            component={this.renderField}
                            label='Confirm Password'
                            validate={[required, passwordsMatch]}
                        />
                        <button className='ui primary button'>Register</button>
                    </form>
                    <p style={{ marginTop: '1rem' }}>
                        Already have an account? <Link to='/login'>Login</Link>
                    </p>
                </div>
                <br/>
                <Copyright/>
            </Container>
        );
    }
}

const required = value => (value ? undefined : 'Required');

const minLength = min => value =>
    value && value.length < min
        ? `Must be at least ${min} characters`
        : undefined;

const minLength3 = minLength(3);

const maxLength = max => value =>
    value && value.length > max ? `Must be ${max} characters or less` : undefined;

const maxLength15 = maxLength(15);

const passwordsMatch = (value, allValues) =>
    value !== allValues.password ? 'Passwords do not match' : undefined;

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

RegisterForm = connect(
    mapStateToProps,
    { register }
)(RegisterForm);

export default reduxForm({
    form: 'registerForm'
})(RegisterForm);