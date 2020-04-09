const users = [
  { username: 'qwer', email: 'Kim@lsware.com', password: '1234' },
  { username: 'Lee', email: 'lee@test.com', password: '456' },
  { username: 'Park', email: 'park@test.com', password: '789' },
]

export function signIn({ username, password }) {
  const user = users.find(user => user.username === username && user.password === password);
  if (user === undefined) throw new Error();
  return user;
}