import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { logout } from '../actions/auth';

import Container from '@material-ui/core/Container';
import Button from '@material-ui/core/Button';

class EnterMain extends Component {
  render() {
    const { user, isAuthenticated } = this.props.auth;
    const userLinks = (
      <Container>
      <div className='right menu'>
        <div className='ui animated button'>
          {user ? user.username : ''}
          <i className='dropdown icon' />
          <div className='menu'>
            <Button onClick={this.props.logout} className='item'>
              Logout
            </Button>
          </div>
        </div>
      </div>
      </Container>
    );

    const guestLinks = (

      <div className='left menu'>
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
      </div>
    );

    return (
      <div className='ui inverted menu' style={{ borderRadius: '0' }}>
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
