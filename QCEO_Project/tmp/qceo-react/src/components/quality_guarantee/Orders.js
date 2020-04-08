import React, {useState, useEffect} from 'react';
import axios from 'axios';

import Link from '@material-ui/core/Link';
import {makeStyles} from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

import Title from './Title';

// Generate Order Data
function createData(id, date, name, shipTo, paymentMethod, amount) {
    return {
        id,
        date,
        name,
        shipTo,
        paymentMethod,
        amount
    };
}

const rows = [
    createData(
        0,
        '16 Mar, 2019',
        'Elvis Presley',
        'Tupelo, MS',
        'VISA ⠀•••• 3719',
        312.44
    ),
    createData(
        1,
        '16 Mar, 2019',
        'Paul McCartney',
        'London, UK',
        'VISA ⠀•••• 2574',
        866.99
    ),
    createData(
        2,
        '16 Mar, 2019',
        'Tom Scholz',
        'Boston, MA',
        'MC ⠀•••• 1253',
        100.81
    ),
    createData(
        3,
        '16 Mar, 2019',
        'Michael Jackson',
        'Gary, IN',
        'AMEX ⠀•••• 2000',
        654.39
    ),
    createData(
        4,
        '15 Mar, 2019',
        'Bruce Springsteen',
        'Long Branch, NJ',
        'VISA ⠀•••• 5919',
        212.79
    )
];

function preventDefault(event) {
    event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
    seeMore: {
        marginTop: theme.spacing(3)
    }
}));

export default function Orders() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const classes = useStyles();

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const response = await axios.get("http://127.0.0.1:8000/api/defect/");
                setData(response.data);
                setLoading(false);
                console.log("Defects Redmine Read OK!");
            } catch (e) {
                console.log(e);
            }
        };
        fetchData();
    }, []);

    if (loading) {
        return <div>
            loading ...
        </div>
    }

    return (
        <React.Fragment>
            <Title>Recent Orders</Title>
            <div>
                <b>{data}</b>
            </div>
            <div>
                <b>{setData}</b>
            </div>
            <Table size="small">
                <TableHead>
                    <TableRow>
                        <TableCell>Date</TableCell>
                        <TableCell>Name</TableCell>
                        <TableCell>Ship To</TableCell>
                        <TableCell>Payment Method</TableCell>
                        <TableCell align="right">Sale Amount</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {
                        rows.map((row) => (
                            <TableRow key={row.id}>
                                <TableCell>{row.date}</TableCell>
                                <TableCell>{row.name}</TableCell>
                                <TableCell>{row.shipTo}</TableCell>
                                <TableCell>{row.paymentMethod}</TableCell>
                                <TableCell align="right">{row.amount}</TableCell>
                            </TableRow>
                        ))
                    }
                </TableBody>
            </Table>
            <div className={classes.seeMore}>
                <Link color="primary" href="#" onClick={preventDefault}>
                    See more orders
                </Link>
            </div>
        </React.Fragment>
    );
}