import axios from "axios";

export async function signIn (username, password){
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body
  const body = JSON.stringify(username, password);
  
  let user = await axios.post('http://localhost:8000/api/auth/login', body, config)
    .then((response) => {
      return response.data;
    })
    .catch((response) => {
      return response.data;
    });

  console.log(user);
  //console.log(user);
  if (user === undefined) return user;
  else return body;
}