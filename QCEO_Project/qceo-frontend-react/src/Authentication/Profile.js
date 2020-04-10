import React from 'react';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: '25ch',
    },
  },
}));

function Profile({ user }) {
  const classes = useStyles();
  const { username, password, email } = user || {};

  return (
    <form className={classes.root} noValidate autoComplete="off">
      <Typography component="h1" variant="h5">
        Profile
        </Typography>
      <TextField
        id="standard-read-only-input"
        label="ID (username)"
        defaultValue={username}
        InputProps={{
          readOnly: true,
        }}
      />
      <TextField
        id="standard-read-only-input"
        label="Password"
        defaultValue={password}
        InputProps={{
          readOnly: true,
        }}
      />
      <TextField
        id="standard-read-only-input"
        label="Email"
        defaultValue={email}
        InputProps={{
          readOnly: true,
        }}
      />
    </form>
  );
}

export default Profile;