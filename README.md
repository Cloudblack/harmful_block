# 유해매체 차단 모델 구현

## 프로젝트 기간
2021/11/08 ~ 2021/11/15

### 프로젝트 발표 동영상  

[프로젝트 발표 영상](https://drive.google.com/file/d/1WvoXdaTTsPVa6b-lS1GW1rOyzZ4wfK33/view?usp=sharing)  

[프로젝트 모델 시연 영상](https://drive.google.com/file/d/1uxq52Dr76WTt0G1kHIRyPFXkRv4ao0Sz/view?usp=sharing)
- 첫 번째 영상에 포함되어있는 부분입니다


# 프로젝트 배경

- 오징어 게임이 유행할때 초등학생들이 오징어게임 츄리닝을 입은 것을 보고 어떻게 오징어게임을 알까 하는 생각이 들었다
- 오징어게임을 볼 수 있는 넷플릭스에서 일반 프로필의 보안도 pin 번호 잠금 뿐이다. 또 키즈프로필을 사용 할 수 있지만 정말 어린 애들만 볼 수준이라 학생들만 해도 여기에 만족하지 못할 것 같습니다 ( 6살 짜리 제 조카는 백반기행을 봅니다 )
- 플랫폼에서 제공하는 것도 물론 좋지만 화면을 인식해서 유해매체를 차단 할 수 있다면 좋을 것 같아 프로젝트를 시작했다

# 프로젝트 분석

- 유해매체란 무엇일까?
    - 유해 + 매체
        ![이미지 1257](https://user-images.githubusercontent.com/86823305/165061741-b6d3495c-aeb2-4c93-a8af-eb90875cf4ea.png)


        
        
    - 유해매체는 매체에 유해를 더한게 유해매체입니다 사실 유해매체를 차단하는 가장 확실한 방법은 매체 자체를 접하지 않으면된다, 매체로는 영화,비디오,게임,음반,음악,음악영상,공연,전기통신의 부호 문언 음향 ,방송프로그램 , 신문들,잡지,간행물,옥외 광고물 상업적 광고물, 전단 등등 사실상 청소년은 눈도 못뜨고 귀도 막고 다녀야됩니다 매체 자체를 차단하기보단 매체에서 유해한것을 막아야할 것 같습니다.
- 청소년 에게 미칠 수 있는 영향
  - ![이미지 1258](https://user-images.githubusercontent.com/86823305/165061534-eda42bb4-4c66-4921-9535-631edfc3c3c5.png)
    

    
    
    - 2021 청소년 통계에 따르면 청소년들이 여가시간에 인터넷을 이용하는 시간이 주당 30시간 즉, 하루에 4 ~ 5시간을 사용합니다 대충 생각할때 8시간 자고 12시간 학교다녀오면 4시간남는데 여가시간을 전부 사용하는 것 같습니다
    초 중 고등학생별 스마트폰 과의존 위험군이 30 ~ 40%에 달합니다 기준이 뭔지 모르겠지만 아마 저도 수치를 올리는데 한몫 했을것같습니다 여기선 스마트폰에 비중을 더했지만 컴퓨터까지 포함하면 청소년들이 인터넷을 많이 사용한다고 볼 수 있을 것 같습니다
- 청소년들이 많은 시간을 할애하는 인터넷은 안전한 곳일까?
    - 음란물, 폭력, 약물, 도박등 인터넷은 정보의 바다인만큼 유해한 정보도 엄청나게 많습니다 어떻게 사용하냐의 차이죠 아무리 잘 사용해도 팝업이나 광고 등 생각지도 못한데서 튀어 나오는 경우도 있습니다
    - 채팅, 글, 댓글등 에서도 비속어와 폭력등이 있습니다 자의든 타의든 미성년자들이 인터넷에서 유해매체를 접하기 아주 쉽습니다
- 청소년 유해 차단 실태
    ![이미지 1260](https://user-images.githubusercontent.com/86823305/165061812-35cfdd33-1082-4e1c-9759-8329d5cd533f.png)

   
    
    - 스마트폰의 경우 청소년 유해 차단앱이 있지만 설치한 비율도 절반수준에 어플이 업데이트되지않아 사실상 무용지물입니다.
    ![이미지 1261](https://user-images.githubusercontent.com/86823305/165061821-4bad1415-80ca-4770-a8c0-2800e371c556.png)

    
    
    - 국가에서도 유해사이트 자체를 우리나라에서 볼 수 없게 차단합니다 하지만 차단을 무시할 수있는 방법이 너무 많고 또, 너무 쉬워서 차단된 걸 오히려 국가가 인정한 사이트라면서 오히려 좋다고하는 사람도 있었습니다
    

# 프로젝트 가설

- 어떻게 유해 매체를 차단 할 것인가?
    ![이미지 1262](https://user-images.githubusercontent.com/86823305/165061852-6dac7da3-b381-40e6-b9aa-1a5abc3ccbf4.png)

    
    
    1. 웹에서 이미지들을 스크래핑해서 가져온후
    2. 모델에 넣습니다
    3. 무해 하다면 제자리로 돌려보냅니다
    
    3-1.유해성을 감지한다면 사진을 폐기하고 대체합니다
    
    1. 반복작업하여 유해한 사진을 전부 제거합니다
    ![이미지 1263](https://user-images.githubusercontent.com/86823305/165061866-5471ae73-43d4-4e1d-b58b-00f0b1ddb7d7.png)

    
    
    - 객체인식으로 유해성을 분류후 대체 이미지로 커버
- 한 이미지에서 객체 검출을 하지 않은 이유
    ![이미지 1264](https://user-images.githubusercontent.com/86823305/165061887-d9c3d27c-5d22-4ad4-af57-c4194fa4e375.png)

    
    
    - 예기치 않은 검출로 아동 애니메이션 짱구는 못 말려가/ 성인만화 크레용 신짱이 되는걸 우려해서입니다

# 프로젝트 진행

- 폭력 마약 도박등 사진은 생각보다 이미지를 찾기 힘들어 시간 관계상 음란물을 사용했습니다
![이미지 1265](https://user-images.githubusercontent.com/86823305/165061953-f7bc23fa-c235-47b6-81d6-0b0c7aca89b2.png)


- 데이터 수집
    ![이미지 1266](https://user-images.githubusercontent.com/86823305/165061969-885592c0-cb1e-4661-a3ea-6aab94743066.png)    
    
    - 셀레니움을 사용해 데이터를 수집했고 이중 분류를 위해 음란물 사진(유해매체)과 인스타그램의 사진(비 유해매체)들을 크롤링 했습니다 , 또 중복되는 사진들은 전부 제거해 줬습니다

- 모델
    ![이미지 1267](https://user-images.githubusercontent.com/86823305/165061996-875cb476-8136-4452-9d1c-8a7320102ad9.png)

    
    
    - 트레인, 발리데이션, 테스트 세개의 세트로 나누어 진행 하였고 전처리로는 증강없이 정규화만 진행했습니다.
    - 모델은 레스넷50v2에 인풋과 전처리용 층과 2중 분류를 사용하기위한 출력층을 추가했습니다
    - 데이터가 적어 Trainable on 시켰습니다
    - Optimizer는 아담 손실함수는 Binary Crossentropy를사용 했습니다
    - 추가로 call back함수로 checkpoint와 ealry stopping reduce LR를 사용했습니다

- 결과
    ![이미지 1268](https://user-images.githubusercontent.com/86823305/165062009-7e00589e-1f58-481d-b8b0-5dd5394581d0.png)

    
    - 데이터 세트별 정확도 입니다 트레인 발리데이션 테스트 순서로 97 99 99퍼가 나왔습니다 기준모델 58퍼 기준 데이터가 좀 적지만 꽤 괜찮은 결과인것 같습니다
    - 예시 테스트
        ![이미지 1274](https://user-images.githubusercontent.com/86823305/165062039-41c4fe05-a36b-4fbf-b514-061a703f82ee.png)
        ![이미지 1269](https://user-images.githubusercontent.com/86823305/165062049-ab07d5cc-fbf0-451f-9dbb-7d9f5fa60149.png)
        ![이미지 1270](https://user-images.githubusercontent.com/86823305/165062052-f371046d-67d3-4691-9eaa-57813c56c73a.png)
        ![이미지 1271](https://user-images.githubusercontent.com/86823305/165062054-cd3d29cc-6fd1-40de-99f5-0813c0ceb569.png)
        ![이미지 1272](https://user-images.githubusercontent.com/86823305/165062057-3c21d314-6662-4761-9df8-8e42f607d86f.png)
        ![이미지 1273](https://user-images.githubusercontent.com/86823305/165062061-7eb307d2-ed7c-42b4-a57b-162d015c65f3.png)
        
    - 이외에 여러 테스트를 더 해보았으나 보이는 특징으로는 그림에는 관대합니다 , 그리고 실물에는 엄격합니다 그런데 인스타로 유해매체가 아닌걸 학습했더니 수영복에 엄청나게 관대합니다

# 회고
![이미지 1275](https://user-images.githubusercontent.com/86823305/165062155-61319042-f340-42a4-88dc-6898c3eec5bb.png)
- 데이터 수집의 중요성, 데이터 양의 중요성을 배웠다
- 크롤링 하는 방법을 배웠다
- 사전학습 모델을 가져와 사용 하는 법을 배웠다
