# DarkDrop Market — curl User-Agent Bypass CTF

This is a simple CTF challenge designed to teach HTTP header manipulation 
and User-Agent based access control bypass using `curl`.

---

## 🎭 Challenge Story (시나리오)

경찰청 사이버수사팀은 “DarkDrop Market”이라는 의심스러운 사이트를 발견했다.  
겉으로 보기에는 아무 정보도 없는 평범한 화면이지만, 익명의 제보에 따르면  
이 사이트는 **특정 User-Agent 값을 가진 클라이언트에게만 중요한 정보를 보여준다**고 한다.

수사관은 curl을 이용해 User-Agent 값을 조작하여  
사이트의 숨겨진 FLAG를 찾아내야 한다.


