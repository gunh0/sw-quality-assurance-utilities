import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보
LOGIN_INFO = {
    'username': '',
    'password': ''
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as session:
    first_page = session.get('http://project.lsware.co.kr/redmine')
    html = first_page.text
    soup = bs(html, 'html.parser')
    authenticity_token = soup.find('input', {'name': 'authenticity_token'})
    print(authenticity_token['value'])

    # {**dict1, **dict2} 으로 dict들을 unpacking
    LOGIN_INFO = {**LOGIN_INFO, **{'authenticity_token': authenticity_token['value']}}
    print(LOGIN_INFO)

    # 다시 로그인
    login_req = session.post('http://project.lsware.co.kr/redmine/login.do', data=LOGIN_INFO)
    print(login_req.status_code)    # 200 이면 성공
    login_req.raise_for_status()

    '''
    urls = [
        'http://project.lsware.co.kr/redmine/projects/omni-pis-qa/issues',
        'http://project.lsware.co.kr/redmine/projects/olis/issues',
        'http://project.lsware.co.kr/redmine/projects/test1',
        'http://project.lsware.co.kr/redmine/projects/test2/issues'
    ]
    '''
    url = 'http://project.lsware.co.kr/redmine/projects/olis/issues'
    res = session.get(url)
    res.raise_for_status()
    html = res.text
    soup = bs(html,'html.parser')
    print(soup)
    table = soup.find_all('div', class_="autoscroll")
    print(table)

