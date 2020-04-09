import React from 'react';

function Profile({ user }) {
  const { username, password, email } = user || {};
  return (
    <>
      <h1>Profile</h1>
      <dt>ID</dt>
      <dd>{username}</dd>
      <dt>Password</dt>
      <dd>{password}</dd>
      <dt>Email</dt>
      <dd>{email}</dd>
    </>
  );
}

export default Profile;