import axios from 'axios';

import {
  USER_LOADING,
  USER_LOADED,
  AUTH_ERROR,
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_SUCCESS
} from './types';

// LOAD USER
export const loadUser = () => async (dispatch, getState) => {
  dispatch({ type: USER_LOADING });

  try {
    const res = await axios.get('http://localhost:8000/api/auth/user', tokenConfig(getState));
    dispatch({
      type: USER_LOADED,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: AUTH_ERROR
    });
  }
};

// REGISTER USER
export const register = ({ username, email, password }) => async dispatch => {
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body
  const body = JSON.stringify({ username, email, password });

  try {
    const res = await axios.post('http://localhost:8000/api/auth/register', body, config);
    dispatch({
      type: REGISTER_SUCCESS,
      payload: res.data
    });
  } catch (err) {
    dispatch({type: REGISTER_FAIL});
    alert('회원가입에 실패하였습니다.');
  }
};

// LOGIN USER
export const login = ({ username, password }) => async dispatch => {
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body
  const body = JSON.stringify({ username, password });

  try {
    const res = await axios.post('http://localhost:8000/api/auth/login', body, config);
    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data
    });
  } catch (err) {
    dispatch({type: LOGIN_FAIL});
    alert('로그인에 실패하였습니다.');
  }
};

// LOGOUT USER
export const logout = () => async (dispatch, getState) => {
  await axios.post('http://localhost:8000/api/auth/logout', null, tokenConfig(getState));
  dispatch({
    type: LOGOUT_SUCCESS
  });
};

// helper function
export const tokenConfig = getState => {
  // Get token
  const token = getState().auth.token;

  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  if (token) {
    config.headers['Authorization'] = `Token ${token}`;
  }

  return config;
};
