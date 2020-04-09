import React, {useState} from 'react';
import {Link, Route, Switch, BrowserRouter as Router} from 'react-router-dom';
import clsx from 'clsx';

import {makeStyles, createMuiTheme, withStyles, ThemeProvider} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import AssignmentIcon from '@material-ui/icons/Assignment';
import BarChartIcon from '@material-ui/icons/BarChart';
import Box from '@material-ui/core/Box';
import Button from '@material-ui/core/Button';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import Container from '@material-ui/core/Container';
import CssBaseline from '@material-ui/core/CssBaseline';
import DashboardIcon from '@material-ui/icons/Dashboard';
import Divider from '@material-ui/core/Divider';
import Drawer from '@material-ui/core/Drawer';
import IconButton from '@material-ui/core/IconButton';
import LayersIcon from '@material-ui/icons/Layers';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import MenuIcon from '@material-ui/icons/Menu';
import PeopleIcon from '@material-ui/icons/People';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

import {signIn} from './auth';
import AuthRoute from './AuthRoute';
import Home from './Home';
import About from './About';
import Profile from './Profile';
import NotFound from './NotFound';
import LoginForm from './LoginForm';
import LogoutButton from './LogoutButton';

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

const ColorButton = withStyles((theme) => ({
    root: {
        color: theme.palette,
        backgroundColor: '#00b2cc',
        '&:hover': {
            backgroundColor: '#6effff'
        }
    }
}))(Button);

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

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            <Link
                color="inherit"
                href="https://material-ui.com/"
                underline="none"
                string='inherit'>
                Your Website
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

function App() {
    const classes = useStyles();
    const [user, setUser] = useState(null);
    const [open, setOpen] = React.useState(true);
    const isAuthenticated = user != null;

    const handleDrawerOpen = () => {
        setOpen(true);
    };
    const handleDrawerClose = () => {
        setOpen(false);
    };

    const login = ({email, password}) => setUser(signIn({email, password}));
    const logout = () => setUser(null);

    return (
        <div className={classes.root}>
            <ThemeProvider theme={outerTheme}>
                <Router>
                    <CssBaseline/>
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
                                <MenuIcon/>
                            </IconButton>
                            <Typography
                                component="h1"
                                variant="h6"
                                color="inherit"
                                noWrap="noWrap"
                                className={classes.title}>
                                QCEO
                            </Typography>
                            <Link
                                to="/Home"
                                style={{
                                    textDecoration: 'none'
                                }}>
                                <ColorButton variant="contained" color="primary" className={classes.margin}>
                                    {'Home'}
                                </ColorButton>
                            </Link>
                            <Link
                                to="/About"
                                style={{
                                    textDecoration: 'none'
                                }}>
                                <ColorButton variant="contained" color="primary" className={classes.margin}>
                                    {'About'}
                                </ColorButton>
                            </Link>
                            <Link
                                to="/Profile"
                                style={{
                                    textDecoration: 'none'
                                }}>
                                <ColorButton variant="contained" color="primary" className={classes.margin}>
                                    {'Profile'}
                                </ColorButton>
                            </Link>
                            {
                                isAuthenticated
                                    ? (<LogoutButton logout={logout}/>)
                                    : (
                                        <Link
                                            to="/login"
                                            style={{
                                                textDecoration: 'none'
                                            }}>
                                            <ColorButton variant="contained" color="primary" className={classes.margin}>
                                                {'Login'}
                                            </ColorButton>
                                        </Link>
                                    )
                            }
                        </Toolbar>
                    </AppBar>
                    <Drawer
                        variant="permanent"
                        classes={{
                            paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose)
                        }}
                        open={open}>
                        <div className={classes.toolbarIcon}>
                            <IconButton onClick={handleDrawerClose}>
                                <ChevronLeftIcon/>
                            </IconButton>
                        </div>
                        <Divider/>
                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="품질점검"/>
                        </ListItem>
                        <Divider/>
                        <ListItem button="button">
                            <ListItemIcon>
                                <DashboardIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Dashboard"/>
                        </ListItem>
                        <ListItem button="button">
                            <ListItemIcon>
                                <ShoppingCartIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Orders"/>
                        </ListItem>
                        <ListItem button="button">
                            <ListItemIcon>
                                <PeopleIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Customers"/>
                        </ListItem>
                        <ListItem button="button">
                            <ListItemIcon>
                                <BarChartIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Reports"/>
                        </ListItem>
                        <ListItem button="button">
                            <ListItemIcon>
                                <LayersIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Integrations"/>
                        </ListItem>
                        <Divider/>
                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Current month"/>
                        </ListItem>
                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Last quarter"/>
                        </ListItem>
                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="Year-end sale"/>
                        </ListItem>
                    </Drawer>
                    <main className={classes.content}>
                        <div className={classes.appBarSpacer}/>
                        <Container className={classes.container}>
                            <Switch>
                                <Route exact="exact" path="/" component={Home}/>
                                <Route path="/about" component={About}/>
                                <Route
                                    path="/login"
                                    render={props => (<LoginForm isAuthenticated={isAuthenticated} login={login} {...props}/>)}/>
                                <AuthRoute
                                    isAuthenticated={isAuthenticated}
                                    path="/profile"
                                    render={props => <Profile user={user} {...props}/>
                                    }
                                />
                                <Route component={NotFound}/>
                            </Switch>
                            <Box pt={4}>
                                <Copyright/>
                            </Box>
                        </Container>
                    </main>
                </Router>
            </ThemeProvider>
        </div>
    );
}

export default App;
