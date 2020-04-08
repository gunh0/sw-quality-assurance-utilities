import React, {Component} from 'react';

import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

import {Link, Redirect} from 'react-router-dom';
import {connect} from 'react-redux';
import {Field, reduxForm} from 'redux-form';
import {login} from '../../actions/auth';

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
      alignItems: 'center',
    },
    avatar: {
      margin: theme.spacing(1),
      backgroundColor: theme.palette.secondary.main,
    },
    form: {
      width: '100%', // Fix IE 11 issue.
      marginTop: theme.spacing(1),
    },
    submit: {
      margin: theme.spacing(3, 0, 2),
    },
  }));

class LoginForm extends Component {
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

    hiddenField = ({type, meta: {
            error
        }}) => {
        return (
            <div className='field'>
                <input type={type}/> {error && <div className='ui red message'>{error}</div>}
            </div>
        );
    };

    onSubmit = formValues => {
        this
            .props
            .login(formValues);
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
                            label='Username'/>
                        <Field
                            name='password'
                            type='password'
                            component={this.renderField}
                            label='Password'/>
                        <Field name='non_field_errors' type='hidden' component={this.hiddenField}/>
                        <button className='ui primary button'>Login</button>
                    </form>
                    <Container component="main" maxWidth="xs">
                        <CssBaseline/>
                        <div className={useStyles.paper}>
                            <Typography component="h1" variant="h5">
                                Sign in
                            </Typography>
                            <form className={useStyles.form} noValidate="noValidate">
                                <TextField
                                    variant="outlined"
                                    margin="normal"
                                    required="required"
                                    fullWidth="fullWidth"
                                    id="email"
                                    label="Email Address"
                                    name="email"
                                    autoComplete="email"
                                    autoFocus="autoFocus"/>
                                <TextField
                                    variant="outlined"
                                    margin="normal"
                                    required="required"
                                    fullWidth="fullWidth"
                                    name="password"
                                    label="Password"
                                    type="password"
                                    id="password"
                                    autoComplete="current-password"/>
                                <Button
                                    type="submit"
                                    fullWidth="fullWidth"
                                    variant="contained"
                                    color="primary"
                                    className={useStyles.submit}>
                                    Sign In
                                </Button>
                                <Grid container="container">
                                    <Grid item="item" xs="xs">
                                    </Grid>
                                    <Grid item="item">
                                        <Link to="/register" variant="body2">
                                            {"Don't have an account? Sign Up"}
                                        </Link>
                                    </Grid>
                                </Grid>
                            </form>
                        </div>
                        <Box mt={8}>
                            <Copyright/>
                        </Box>
                    </Container>
                </div>
            </div>
        );
    }
}

const mapStateToProps = state => (
    {isAuthenticated: state.auth.isAuthenticated}
);

LoginForm = connect(mapStateToProps, {login})(LoginForm);

export default reduxForm({form: 'loginForm'})(LoginForm);