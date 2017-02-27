# 구현 순서
- 라즈베리파이에 터미널 접속해서 커맨드 날려서 에어컨 켜고/끄기 구현
- 서버 띄워서 외부에서 접속하여 에어컨 켜고/끄기
- 슬랙으로 에어컨 켜고/끄기
- 아마존 에코로 에어컨 켜고/끄기
- 라즈베리파이 ip를 고정 ip대신에 유동 ip를 사용하고 자동적으로 네트워크상에서 기기를 찾아 요청을 보낼 수 있도록 네트워크 구성

# TODO
- 회로도 그리기
- 빵판에 회로 만들기
- 리모컨에서 나오는 ir신호 캡쳐
- ir신호 생성해서 에어컨 제어하기
- 서버 셋업 
- 아마존 에코 연동
- 라즈베리파이 자동 검색 네트워크 구성 
- 만능 기판에 ir발신기 회로 구성

# 회로도 작성 툴 선택
- https://trends.google.com/trends/explore?q=fritzing,Eagle%20Cad,circuits.io
- https://ptarmiganlabs.com/blog/2013/08/27/fritzing-vs-circuits-io-vs-eagle-comparing-schematics-editors/
- fritzing vs Eagle Cad vs circuits.io ?
- fritzing이 무난해 보인다

# 메모리카드 선택
- http://m.blog.naver.com/alkydes/220699946626
- http://nogada-lab.tistory.com/13
- 결론은 mlc로 16기가 구매하기
- Sandisk micro sd extreme 16GB 구매
- 샌디스크 16기가가 대부분 품절이라 (http://www.wemakeprice.com/deal/adeal/1343369/?utm_source=naver_ep&utm_medium=PRICE_af&utm_campaign=1343369&src=text&kw=02413D) 에서 32기가 구매. (5번 32GB 무료배송)
