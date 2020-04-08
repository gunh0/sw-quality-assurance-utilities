import React, {Component} from 'react';
import {Link, Redirect} from 'react-router-dom';
import {connect} from 'react-redux';
import {Field, reduxForm} from 'redux-form';
import {register} from '../../actions/auth';

import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            <Link color="inherit" href="https://material-ui.com/">
                Your Website
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

const useStyles = makeStyles((theme) => ({
    paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center'
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main
    },
    form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(3)
    },
    submit: {
        margin: theme.spacing(3, 0, 2)
    }
}));

class RegisterForm extends Component {
    renderField = ({
        input,
        label,
        type,
        meta: {
            touched,
            error
        }
    }) => {
        return (
            <div
                className={`field ${touched && error
                    ? 'error'
                    : ''}`}>
                <label>{label}</label>
                <input {...input} type={type}/> {
                    touched && error && (
                        <span className='ui pointing red basic label'>{error}</span>
                    )
                }
            </div>
        );
    };

    onSubmit = formValues => {
        this
            .props
            .register(formValues);
    };

    render() {
        if (this.props.isAuthenticated) {
            return <Redirect to='/'/>;
        }
        return (
            <div className='ui container'>
                <div className='ui segment'>
                    <form
                        onSubmit={this
                            .props
                            .handleSubmit(this.onSubmit)}
                        className='ui form'>
                        <Field
                            name='username'
                            type='text'
                            component={this.renderField}
                            label='Username'
                            validate={[required, minLength3, maxLength15]}/>
                        <Field
                            name='email'
                            type='email'
                            component={this.renderField}
                            label='Email'
                            validate={required}/>
                        <Field
                            name='password'
                            type='password'
                            component={this.renderField}
                            label='Password'
                            validate={required}/>
                        <Field
                            name='password2'
                            type='password'
                            component={this.renderField}
                            label='Confirm Password'
                            validate={[required, passwordsMatch]}/>
                        <button className='ui primary button'>Register</button>
                    </form>
                    <Container component="main" maxWidth="xs">
                        <CssBaseline/>
                        <div className={useStyles.paper}>
                            <Typography component="h1" variant="h5">
                                Sign up
                            </Typography>
                            <form className={useStyles.form} noValidate="noValidate">
                                <Grid container="container" spacing={2}>
                                    <Grid item="item" xs={12} sm={6}>
                                        <TextField
                                            autoComplete="fname"
                                            name="firstName"
                                            variant="outlined"
                                            required="required"
                                            fullWidth="fullWidth"
                                            id="firstName"
                                            label="First Name"
                                            autoFocus="autoFocus"/>
                                    </Grid>
                                    <Grid item="item" xs={12} sm={6}>
                                        <TextField
                                            variant="outlined"
                                            required="required"
                                            fullWidth="fullWidth"
                                            id="lastName"
                                            label="Last Name"
                                            name="lastName"
                                            autoComplete="lname"/>
                                    </Grid>
                                    <Grid item="item" xs={12}>
                                        <TextField
                                            variant="outlined"
                                            required="required"
                                            fullWidth="fullWidth"
                                            id="email"
                                            label="Email Address"
                                            name="email"
                                            autoComplete="email"/>
                                    </Grid>
                                    <Grid item="item" xs={12}>
                                        <TextField
                                            variant="outlined"
                                            required="required"
                                            fullWidth="fullWidth"
                                            name="password"
                                            label="Password"
                                            type="password"
                                            id="password"
                                            autoComplete="current-password"/>
                                    </Grid>
                                </Grid>
                                <Button
                                    type="submit"
                                    fullWidth="fullWidth"
                                    variant="contained"
                                    color="primary"
                                    className={useStyles.submit}>
                                    Sign Up
                                </Button>
                                <Grid container="container" justify="flex-end">
                                    <Grid item="item">
                                        <Link to="/login" variant="body2">
                                            Already have an account? Sign in
                                        </Link>
                                    </Grid>
                                </Grid>
                            </form>
                        </div>
                        <Box mt={5}>
                            <Copyright/>
                        </Box>
                    </Container>
                </div>
            </div>
        );
    }
}

const required = value => (
    value
        ? undefined
        : 'Required'
);

const minLength = min => value => value && value.length < min
    ? `Must be at least ${min} characters`
    : undefined;

const minLength3 = minLength(3);

const maxLength = max => value => value && value.length > max
    ? `Must be ${max} characters or less`
    : undefined;

const maxLength15 = maxLength(15);

const passwordsMatch = (value, allValues) => value !== allValues.password
    ? 'Passwords do not match'
    : undefined;

const mapStateToProps = state => (
    {isAuthenticated: state.auth.isAuthenticated}
);

RegisterForm = connect(mapStateToProps, {register})(RegisterForm);

export default reduxForm({form: 'registerForm'})(RegisterForm);
