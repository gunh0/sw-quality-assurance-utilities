import React from 'react';
import { Route, Redirect } from 'react-router-dom';

function AuthRoute({ isAuthenticated, component: Component, render, ...rest }) {
  return (
    <Route
      {...rest}
      render={props =>
        isAuthenticated ? (
          render ? render(props) : <Component {...props} />
        ) : (
            <Redirect
              to={{ pathname: '/login', state: { from: props.location } }}
            />
          )
      }
    />
  );
}

export default AuthRoute;
