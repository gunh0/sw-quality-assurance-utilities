import React, {useState} from 'react';
import clsx from 'clsx';

import {makeStyles} from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import AccountCircle from '@material-ui/icons/AccountCircle';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import PeopleIcon from '@material-ui/icons/People';
import BarChartIcon from '@material-ui/icons/BarChart';
import LayersIcon from '@material-ui/icons/Layers';
import AssignmentIcon from '@material-ui/icons/Assignment';

import BasicDashboard from './BasicDashboard';
import QGBoard from './quality_guarantee/QGBoard';

const drawerWidth = 240;

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
    }
}));

export default function Dashboard() {
    const classes = useStyles();
    const [open, setOpen] = React.useState(true);
    const [mainComp, setComp] = useState(BasicDashboard);
    const handleDrawerOpen = () => {
        setOpen(true);
    };
    const handleDrawerClose = () => {
        setOpen(false);
    };

    return (
        <div className={classes.root}>
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
                    <IconButton
                        aria-label="account of current user"
                        aria-controls="menu-appbar"
                        aria-haspopup="true"
                        color="inherit">
                        <AccountCircle/>
                    </IconButton>
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
                <List>
                    <div>
                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="품질보증"/>
                        </ListItem>

                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="코드품질"/>
                        </ListItem>

                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="품질관리"/>
                        </ListItem>

                        <ListItem button="button" onClick={()=>setComp(QGBoard)}>
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="기능 구현 중..."/>
                        </ListItem>

                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="테스트지원"/>
                        </ListItem>

                        <ListItem button="button">
                            <ListItemIcon>
                                <AssignmentIcon/>
                            </ListItemIcon>
                            <ListItemText primary="자동화"/>
                        </ListItem>

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
                    </div>
                </List>
                <Divider/>
                <List>
                    <div>
                        <ListSubheader inset="inset">Saved reports</ListSubheader>
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
                    </div>
                </List>
            </Drawer>
            <main children={mainComp}/>
        </div>
    );
}