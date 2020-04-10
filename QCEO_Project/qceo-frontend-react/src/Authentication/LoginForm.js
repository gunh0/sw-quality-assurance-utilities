import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';

import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Link from '@material-ui/core/Link';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

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
    marginTop: theme.spacing(1)
  },
  submit: {
    margin: theme.spacing(3, 0, 2)
  }
}));

function LoginForm({ isAuthenticated, login, location }) {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const classes = useStyles();

  const handleClick = () => {
    try {
      login({ username, password });
    } catch (e) {
      console.log(username, password);
      alert('로그인에 실패하였습니다.');
      setUsername('');
      setPassword('');
    }
  };

  const { from } = location.state || {from: {pathname: "/profile"}};
  if (isAuthenticated){
    return <Redirect to={from} />;
  }



  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
                </Typography>
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          id="username"
          label="ID (Username)"
          name="username"
          autoComplete="username"
          value={username}
          onChange={({ target: {
            value
          } }) => setUsername(value)}
          type="text"></TextField>
        <TextField
          fullWidth
          variant="outlined"
          margin="normal"
          required
          id="password"
          label="Password"
          name="password"
          autoComplete="password"
          value={password}
          onChange={({ target: {
            value
          } }) => setPassword(value)}
          type="password"></TextField>
        <Button
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          className={classes.submit}
          onClick={handleClick}>
          Sign In
                </Button>
        <Grid item>
          <Link href="#" variant="body2">
            {"Don't have an account? Sign Up"}
          </Link>
        </Grid>
      </div>
    </Container>
  );
}

export default LoginForm;