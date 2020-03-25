# PowerLinkRanking v2.3

![image](https://user-images.githubusercontent.com/41619898/75845179-b01c6400-5e1b-11ea-8497-76099d395573.png)



**Users can view the Naver Click Choice Ads by entering the search term in NAVER.**

**This program is designed to determine the ranking of URLs to look up in relation to keywords in Powerlink when searching NAVER.**



---



### NAVER AD Servieces

- https://saedu.naver.com/adguide/eng.nhn

  ![image](https://user-images.githubusercontent.com/41619898/76375166-7c47be00-6388-11ea-91f8-32a428b8553a.png)

---



### Basic Search Tab

![image](https://user-images.githubusercontent.com/41619898/77491961-8dadc180-6e82-11ea-8557-2e1c03a30157.png)



### Multi Search Tab (using by .xlsx)

![image-20200325103004107](C:\Users\123\AppData\Roaming\Typora\typora-user-images\image-20200325103004107.png)



---



### Python Library List

- easygui
  - http://easygui.sourceforge.net/#
- tkinter
  - https://docs.python.org/3/library/tkinter.html



---



### Multi Search Form

- .csv : Not supported
- .xls : Not supported
- **.xlsx : Support**



![image](https://user-images.githubusercontent.com/41619898/77394526-f6456180-6de2-11ea-949a-6ba2d3bbd0f7.png)



---



### Make .exe File

1. pyinstaller --clean --onefile --noconsole --icon=icon/icon.ico main.py

2. ```
   [.spec]
   import sys
   sys.setrecursionlimit(2000)
   
   [compt.py]
   out = out.decode(encoding, errors='ignore')
   ```

3. pyinstaller --clean --onefile --noconsole --icon=icon/icon.ico main.spec