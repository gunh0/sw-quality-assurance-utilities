import React from 'react';
import { Route } from 'react-router-dom';

import Typography from '@material-ui/core/Typography';

function AuthRoute({ isAuthenticated, component: Component, render, ...rest }) {
  return (
    <Route
      {...rest}
      render={props =>
        isAuthenticated ? (
          render ? render(props) : <Component {...props} />
        ) : (
            <Typography component="h1" variant="h5">
              로그인이 필요합니다.
            </Typography>
          )
      }
    />
  );
}

export default AuthRoute;
