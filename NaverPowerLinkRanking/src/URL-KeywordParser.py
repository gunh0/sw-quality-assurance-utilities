import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

def PowerLinkPaser(SearchURL, Keyword):
    url_list = []
    keyword_list = []
    ranking_list = []
    nextBtn=['init']
    pageIndex=1
    if Keyword != '':
        while len(nextBtn)==1:     # 다음페이지 버튼이 존재하는 경우
            baseurl = 'https://ad.search.naver.com/search.naver?where=ad&query='
            url = baseurl + quote_plus(Keyword) + 'pagingIndex=' + str(pageIndex)
            req = urllib.request.urlopen(url)
            res = req.read()
            soup = BeautifulSoup(res, 'html.parser')
            nextBtn = soup.find_all('a', class_='next')
            print(nextBtn)
        
'''        
        divData = soup.find_all('a', class_='url')
        print (len(divData))
        pageIndex = 1
        while len(nextBtn)==1:     # 다음페이지 버튼이 존재하는 경우
            pageIndex+=1
            NextPageURL = url + 'pagingIndex=' + str(pageIndex)
            req = urllib.request.urlopen(NextPageURL)
            res = req.read()
            soup = soup = BeautifulSoup(res, 'html.parser')
            nextBtn = soup.find_all('a', class_='next')

            divData.append(soup.find_all('a', class_='url'))
            print (len(divData))
    return (url_list, keyword_list, ranking_list)

a, b, c = PowerLinkPaser('URL','호텔')
print(a,b,c)
----------------------------------------------------------

        divData = soup.find_all('a', class_='url')
        rank = 0
        findFlag = 0
        for urls in divData:
            rank += 1
            #print(keyword, "|", searchUrl, "-", rank, ":", urls.get_text())
            if(searchUrl == urls.get_text()):
                findFlag = 1
                url_col.append(searchUrl)
                keyword_col.append(keyword)
                ranking_col.append(str(rank))
        if(findFlag == 0):
            httpPat = '^http://'
            httpsPat = '^https://'
            if re.search(httpPat, searchUrl) is None:
                httpTransUrl = 'http://' + searchUrl
                rank = 0
                for urls in divData:
                    rank += 1
                    #print(keyword, "|", searchUrl, "-", rank, ":", urls.get_text())
                    if(httpTransUrl == urls.get_text()):
                        findFlag = 1
                        url_col.append(httpTransUrl)
                        keyword_col.append(keyword)
                        ranking_col.append(str(rank))
            if(findFlag == 0):
                if re.search(httpsPat, searchUrl) is None:
                    httpsTransUrl = 'https://' + searchUrl
                    rank = 0
                    for urls in divData:
                        rank += 1
                        #print(keyword, "|", searchUrl, "-", rank, ":", urls.get_text())
                        if(httpsTransUrl == urls.get_text()):
                            findFlag = 1
                            url_col.append(httpsTransUrl)
                            keyword_col.append(keyword)
                            ranking_col.append(str(rank))
            if(findFlag == 0):
                url_col.append(searchUrl)
                keyword_col.append(keyword)
                ranking_col.append("None")
'''