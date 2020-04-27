import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';

import { createMuiTheme, makeStyles, withStyles, ThemeProvider } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

const drawerWidth = 240;

const outerTheme = createMuiTheme({
  palette: {
    primary: {
      light: '#8187ff',
      main: '#3d5afe',
      dark: '#0031ca',
      contrastText: '#fff'
    },
    secondary: {
      light: '#6effff',
      main: '#00e5ff',
      dark: '#00b2cc',
      contrastText: '#000'
    }
  }
});

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex'
  },
  toolbar: {
    paddingRight: 24, // keep right padding when drawer closed
  },
  toolbarIcon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme
      .transitions
      .create([
        'width', 'margin'
      ], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen
      })
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme
      .transitions
      .create([
        'width', 'margin'
      ], {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen
      })
  },
  margin: {
    margin: theme.spacing(1)
  },
  menuButton: {
    marginRight: 36
  },
  menuButtonHidden: {
    display: 'none'
  },
  title: {
    flexGrow: 1
  },
  drawerPaper: {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme
      .transitions
      .create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen
      })
  },
  drawerPaperClose: {
    overflowX: 'hidden',
    transition: theme
      .transitions
      .create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen
      }),
    width: theme.spacing(7),
    [
      theme
        .breakpoints
        .up('sm')
    ]: {
      width: theme.spacing(9)
    }
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto'
  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4)
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column'
  },
  fixedHeight: {
    height: 240
  },
  link: {
    margin: theme.spacing(1, 1.5)
  }
}));

function MainBar() {
  const classes = useStyles();
  const ColorButton = withStyles((theme) => ({
    root: {
      color: theme.palette,
      backgroundColor: '#00b2cc',
      '&:hover': {
        backgroundColor: '#6effff'
      }
    }
  }))(Button);
  return (
    <div className={classes.root}>
      <CssBaseline />
      <ThemeProvider theme={outerTheme}>
        <CssBaseline />
        <AppBar position="absolute">
          <Toolbar className={classes.toolbar}>
            <Typography
              component="h1"
              variant="h6"
              color="inherit"
              className={classes.title}>
              QCEO
            </Typography>
            <Paper>
              <Grid container align="center" Itemsspacing={3}>
                <ThemeProvider theme={outerTheme}>
                  <Grid item xs={0.1}>
                    <Button>
                      <Link
                        to="/login"
                        style={{
                          textDecoration: 'none'
                        }}>
                        <ColorButton variant="contained" color="primary">
                          {'Login'}
                        </ColorButton>
                      </Link>
                    </Button>
                  </Grid>
                  <Grid item xs={0.1}>
                    <Button>
                      <Link
                        to="/Register"
                        style={{
                          textDecoration: 'none'
                        }}>
                        <ColorButton variant="contained" color="primary">
                          {'Register'}
                        </ColorButton>
                      </Link>
                    </Button>
                  </Grid>
                </ThemeProvider>
              </Grid>
            </Paper>
          </Toolbar>
        </AppBar>
        <div className={classes.appBarSpacer} />
      </ThemeProvider>
    </div>
  )
}

class Main extends Component {
  render() {
    const { user, isAuthenticated } = this.props.auth;

    const userLinks = (
      <Container>
        <div className='right menu'>
          <div className="ui basic vertical animated button" tabindex="0">
            <div class="hidden content" onClick={this.props.logout}>
              Logout
              </div>
            <div class="visible content">
              <i class="icon user"></i>
              {user ? user.username : ''}
            </div>
          </div>
        </div>
      </Container>
    );

    const guestLinks = (
      <MainBar />
    );

    return (
      <div>
        {isAuthenticated ? userLinks : guestLinks}
      </div>
    );
  }
}

const mapStateToProps = state => ({
  auth: state.auth
});

export default connect(
  mapStateToProps,
  { logout }
)(Main);
