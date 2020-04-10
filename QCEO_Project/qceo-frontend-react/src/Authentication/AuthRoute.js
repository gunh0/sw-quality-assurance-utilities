import React from 'react';
import { Route } from 'react-router-dom';

function AuthRoute({ isAuthenticated, component: Component, render, ...rest }) {
  return (
    <Route
      {...rest}
      render={props =>
        isAuthenticated ? (
          render ? render(props) : <Component {...props} />
        ) : (
            //<Redirect to={{ pathname: '/login', state: { from: props.location } }}/>
            <div>Login 필요</div>
          )
      }
    />
  );
}

export default AuthRoute;
