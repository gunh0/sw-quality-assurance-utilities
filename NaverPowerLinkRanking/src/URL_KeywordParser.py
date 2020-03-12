import re
import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

urlTempList = []
rank = 1

def PowerLinkPaser(SearchURL, Keyword):
    url_list = []
    keyword_list = []
    ranking_list = []
    nextBtn = ['init']
    pageIndex = 1
    global rank
    rank=1
    urlTempList.clear()
    if Keyword != '':
        while len(nextBtn) == 1:     # 다음페이지 버튼이 존재하는 경우
            baseurl = 'https://ad.search.naver.com/search.naver?where=ad&query='
            url = baseurl + quote_plus(Keyword) + \
                '&pagingIndex=' + str(pageIndex)
            #print('Parser Module : ', url)
            req = urllib.request.urlopen(url)
            res = req.read()
            soup = BeautifulSoup(res, 'html.parser')
            divData = soup.find_all('a', class_='url')
            for urls in divData:
                urlTempList.append([rank, urls.get_text()])
                rank += 1
            nextBtn = soup.find_all('a', class_='next')
            pageIndex += 1
        #print('Parser Module : ', urlTempList)
        SearchRanking = SearchURL_Function(SearchURL)
        keyword_list.append(Keyword)
        if SearchRanking is None:
            url_list.append(SearchURL)
            ranking_list.append("None")
        else:
            url_list.append(SearchRanking[1])
            ranking_list.append(str(SearchRanking[0]))
    #print('Parser Module : ', url_list, keyword_list, ranking_list)
    return(url_list, keyword_list, ranking_list)


def SearchURL_Function(URL):
    for i in range(0, len(urlTempList)):
        # 'http'나 'https'가 포함되지 않거나, 단순히 'gmarket' 과 같이 하나의 키워드가 포함되어 있는 URL도 찾아낸다.
        if re.search(str(URL), urlTempList[i][1]):
            return (urlTempList[i][0], urlTempList[i][1])


'''
# Function Test
a, b, c = PowerLinkPaser('www.gmarket','호텔')
print(a,b,c)
'''
