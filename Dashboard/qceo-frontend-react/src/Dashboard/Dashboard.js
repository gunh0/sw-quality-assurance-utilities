import React from 'react';
import { Link, BrowserRouter as Router } from 'react-router-dom';
import clsx from 'clsx';

import { makeStyles, createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import AssignmentIcon from '@material-ui/icons/Assignment';
import BarChartIcon from '@material-ui/icons/BarChart';
import Box from '@material-ui/core/Box';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
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
import PeopleIcon from '@material-ui/icons/People';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import Typography from '@material-ui/core/Typography';

import QIBoard from './RedmineBase_QualityInspection';

//import QIBoard from './RedmineBase_QualityInspection/index'

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

function Copyright() {
    return (
        <Typography variant="body2" color="textSecondary" align="center">
            {'Copyright © '}
            {new Date().getFullYear()}
            {' by devgun@github.io All rights reserved.'}
        </Typography>
    );
}

function Dashboard() {
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
                <Router>
                    <CssBaseline />
                    <Drawer
                        variant="permanent"
                        classes={{
                            paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose)
                        }}
                        open={open}>
                        <div className={classes.toolbarIcon}>
                            <IconButton onClick={handleDrawerClose}>
                                <ChevronLeftIcon />
                            </IconButton>
                            <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title} align="center">
                                QCEO
          </Typography>
                            <IconButton onClick={handleDrawerOpen}>
                                <ChevronRightIcon />
                            </IconButton>
                        </div>
                        <Divider />
                        <Link to='/qiboard' style={{ textDecoration: 'none' }}>
                            <ListItem button>
                                <ListItemIcon>
                                    <AssignmentIcon />
                                </ListItemIcon>
                                <ListItemText primary="품질점검" />
                            </ListItem>
                        </Link>
                        <Divider />
                        <ListItem button>
                            <ListItemIcon>
                                <DashboardIcon />
                            </ListItemIcon>
                            <ListItemText primary="Dashboard" />
                        </ListItem>
                        <ListItem button>
                            <ListItemIcon>
                                <ShoppingCartIcon />
                            </ListItemIcon>
                            <ListItemText primary="Orders" />
                        </ListItem>
                        <ListItem button>
                            <ListItemIcon>
                                <PeopleIcon />
                            </ListItemIcon>
                            <ListItemText primary="Customers" />
                        </ListItem>
                        <ListItem button>
                            <ListItemIcon>
                                <BarChartIcon />
                            </ListItemIcon>
                            <ListItemText primary="Reports" />
                        </ListItem>
                        <ListItem button>
                            <ListItemIcon>
                                <LayersIcon />
                            </ListItemIcon>
                            <ListItemText primary="Integrations" />
                        </ListItem>
                        <Divider />
                        <ListItem button>
                            <ListItemIcon>
                                <AssignmentIcon />
                            </ListItemIcon>
                            <ListItemText primary="Current month" />
                        </ListItem>
                        <ListItem button>
                            <ListItemIcon>
                                <AssignmentIcon />
                            </ListItemIcon>
                            <ListItemText primary="Last quarter" />
                        </ListItem>
                        <ListItem button>
                            <ListItemIcon>
                                <AssignmentIcon />
                            </ListItemIcon>
                            <ListItemText primary="Year-end sale" />
                        </ListItem>
                    </Drawer>
                    <main className={classes.content}>
                        <div className={classes.appBarSpacer} />
                        <Container className={classes.container}>
                            <QIBoard />
                            <Box pt={4}>
                                <Copyright />
                            </Box>
                        </Container>
                    </main>
                </Router>
            </ThemeProvider>
        </div>
    );
}

export default Dashboard;