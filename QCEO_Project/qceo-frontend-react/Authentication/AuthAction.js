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

  //console.log('Axios Data Check: ', user);

  if (user === undefined)
  {
    alert('로그인에 실패하였습니다.');
    return await user;
  }
  else
  {
    alert('로그인에 성공하였습니다.');
    return await body;
  }
}