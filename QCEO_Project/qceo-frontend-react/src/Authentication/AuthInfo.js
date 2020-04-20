import axios from "axios";

// Saving temporary user information
const users = [
  { username: 'qwer', email: 'kim@lsware.com', password: '1234' },
  { username: 'Lee', email: 'lee@test.com', password: '456' },
  { username: 'Park', email: 'park@test.com', password: '789' },
]

export function signIn({ id, pw }) {
  //const user = users.find(user => user.username === username && user.password === password);
  //if (user === undefined) throw new Error();
  //return user;

  const body = JSON.stringify({ username: id, email: "test1234@example.com", password: pw });
  const config = {
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
  };

  axios.post('http://localhost:8000/api/auth/logout')
    .then(function (response) {
      console.log("axios : ", response);
    })
    .catch(function (error) {
      console.log("axios : ", error);
    });

  const user = body;
  return user;
}