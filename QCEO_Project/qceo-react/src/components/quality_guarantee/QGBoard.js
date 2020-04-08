import React from 'react';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Orders from './Orders';

function QGBoard() {
    return (
        <Container maxWidth="lg">
            {/* Recent Orders */}
            <Grid item="item" xs={12}>
                <Paper>
                    <Orders/>
                </Paper>
            </Grid>
        </Container>
    )
}

export default QGBoard;
