import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';
import clsx from 'clsx';

import { createMuiTheme, makeStyles, ThemeProvider } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
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
  const [open, setOpen] = React.useState(true);

  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <div className={classes.root}>
      <CssBaseline />
      <ThemeProvider theme={outerTheme}>
        <CssBaseline />
        <AppBar
          position="absolute"
          className={clsx(classes.appBar, open && classes.appBarShift)}>
          <Toolbar className={classes.toolbar}>
            <IconButton
              edge="start"
              color="inherit"
              aria-label="open drawer"
              onClick={handleDrawerOpen}
              className={clsx(classes.menuButton, open && classes.menuButtonHidden)}>
              <MenuIcon />
            </IconButton>
            <Typography
              component="h1"
              variant="h6"
              color="inherit"
              className={classes.title}>
              QCEO
                          </Typography>
          </Toolbar>
        </AppBar>
      </ThemeProvider>
    </div>
  )
}

class EnterMain extends Component {
  render() {
    const { user, isAuthenticated } = this.props.auth;
    const userLinks = (
      <Container>
        <div className='right menu'>
          <div className="ui vertical animated button" tabindex="0">
            <div class="hidden content" onClick={this.props.logout}>
              Logout
            </div>
            <div class="visible content">
              {user ? user.username : ''}
            </div>
          </div>
        </div>
      </Container>
    );

    const guestLinks = (
      <Container>
        <Button>
          <Link to='/login' className='header item'>
            Login
        </Link>
        </Button>
        <Button>
          <Link to='/register' className='header item'>
            Sign Up
        </Link>
        </Button>

      </Container>
    );

    return (
      <div className='ui inverted menu' style={{ borderRadius: '0' }}>
        <MainBar />
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
)(EnterMain);
