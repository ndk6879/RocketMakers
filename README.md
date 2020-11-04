<h1>과정</h1>  

제플린에 보이는 화면대로 비슷하게 구현하려 하다가 프런트 부분에 제약이 많아서 제가 아는 선에서 비슷한 기능 위주로 만들었습니다.  
사고 이력, 수리 내역, 제조사를 직접 입력하면 form으로 받아와서 데이터베이스에 저장시키는 방식으로 구현해봤습니다.  
그리고 입력한 데이터들을 추가시키는 것 말고도 읽고, 업데이트하고, 삭제하는 부분까지 쉽게 만들기 구현하기 위해 DRF를 사용하려고 했습니다.

장고는 사용해봤지만 라이브러리를 사용한 경험이 없어서 그나마 많이 들어본 DRF부터 해보자고 시작했습니다.   
RESTful 한 API 개발을 위해 여기저기 찾아보고 공부하면서 serializers도 알게 되고 로컬서버 실행은 성공했습니다.   

서버를 실행하고 보니 모델의 데이터가 비어 있었습니다. 원격서버 말고 로컬 서버에서 했는데 왜 그렇지 하고 찾아보니  
DRF를 만들기 전에 이미 프로젝트 앱에서 만든 모델의 데이터들이랑 새로 만든 DRF랑 연동시켜줘야 하는 것을 알게 됐습니다.   
그래서 알아보니 애초 프로젝트를 만들고 앱을 설정할 때 settings.py의 DATABASE에 MySQL을 추가하는 방법도 있었는데   
저는 forms.py를 이용해서 데이터 입력가능한 부분까지 만들고 DRF를 시작해서 순서가 조금 달랐습니다.   

그래도 다시 생각해서 DRF 로컬서버를 끄고(실제 장고서버와 DRF서버가 따로 있다는 것도 알게 됐습니다.)   
원래 프로젝트의 settings.py의 DATABASE에 MySQL를 추가하고 진행하려 했는데 에러가 발생했습니다.  
에러 수정과정이 조금 벅차서 MySQL말고 제가 기존에 sqlite3로 만들었던 데이터를 DRF과 연동할 방법은 알아보려고 했습니다.   
그런데 이 과정부터 다시 DRF서버를 실행시키는 것까지 더 공부하고 필요한 시간이 충분하지 않아서 여기서 마무리했습니다.  




<h1>궁금한 점</h1>  

DRF 로컬서버를 실행하는데 성공하고 프로젝트 앱의 모델을 연동시켜서 출력시키는 과정에서 난항을 겪어서  
비효율적이지만 그냥 따로 CRUD기능을 가진 페이지들을 만드는 생각을 해봤습니다.  
그런데 다시 생각해보니 그런 기능들은 DB Browser for SQLite같은 프로그램을 사용하면 쉽게 사용 가능한데 굳이 DRF을 만들 필요가 있나라는 궁금점이 생겼습니다.

<h1> + 느낀 점</h1>  

학기 중에 처음 해보는 코딩테스트. 처음에는 감 잡기도 어려웠고 한번도 사용안해 본 라이브러리들을 빠르게 공부해서 사용하기란 쉽진 않았다. 
시간을 넉넉하게 주셨지만 그래도 최대한 빨리 제출 할려고 몇일을 몰아서 몰두했지만 쉽진 않았다. 그래도 바쁘게 뭔가를 공부하고 배운거 같아 좋았다.