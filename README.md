# 추천시스템 

## timeline
- [2019-02-21] : 첫 회의. 각자 추천시스템에 대해 공부할 것 정함
- [2019-02-25] : 추천시스템 알아가기
  - [참고 link1](https://datascienceschool.net/view-notebook/fcd3550f11ac4537acec8d18136f2066/) : [정리](https://github.com/miniii222/BOAZ_adv_project/blob/master/recommender%20system/study/%EC%B6%94%EC%B2%9C%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EC%95%8C%EC%95%84%EA%B0%80%EA%B8%B0.ipynb)
  - [참고 link2](https://www.fun-coding.org/recommend_basic1.html) : [정리](https://github.com/miniii222/BOAZ_adv_project/blob/master/recommender%20system/study/%EC%B6%94%EC%B2%9C%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EC%95%8C%EC%95%84%EA%B0%80%EA%B8%B02.ipynb)
- [2019-03-07] : 데이터 다운로드 & EDA 진행
  #### - 회의내용
    - y 파악하기
    - session id, user id 파악하기
    - 강의 5,6,7 들어오기
    - session_based rs 조사하기
- [2019-03-08] : EDA
- [2019-03-13] : 파이썬 머신러닝 
- [2019-03-14] : surprise 패키지 공부
- [2019-03-15] : 회의
  #### - 회의내용
  - 샘플코드 공부할 것.
  - 데이터 공부, 모델 공부
- [2019-03-20] : last_date & click 추가해서 submission 점수x
- [2019-03-21] : only last_date submission 점수x
- [2019-03-29] : 주최 측에서 데이터 
 
- [2019-05-02] : 새로운 마음으로 화이팅! 5/7 각자 한 거 결과 보고 & ppt 상의


# RecSys 2019
## 데이터 개요
#### 시간
- train data : 2018-11-01 00:00:08~ 2018-11-06 23:59:59 / test data : 2018-11-07 00:00:07 ~ 2018-11-08 23:59:59
#### 데이터 개수
- `train data` : user ID 개수 - 730803, session ID 개수 : 910683
- `test data` : user ID 개수 - 250852, session ID 개수 : 291381
- `train + test` : user ID 개수 - 948041, session ID 개수 : 1202048
- train에만 있는 user_id 개수 697189 / test에만 있는 user_id 개수 217238
- train, test 모두 포함하는 user_id 개수 33614
- train에만 있는 session_id 개수 910667 / test에만 있는 session_id 개수 291365
- train, test 모두 포함하는 session_id 개수 16
- `item_meta` 데이터에는 unique한 927142개의 item에 대한 특성에 대한 정보가 있다.

## 알게 된 것
- 다른 날이어도 같은 session_id가 있을 수 있다.
- 

### 관련자료 공부
- [coursera](https://www.coursera.org/learn/machine-learning/lecture/uG59z/content-based-recommendations) : 정리 [link](https://github.com/miniii222/Coursera/tree/master/Machine_Learning_Andrew_Ng/Recommender%20System)
- [udemy](https://www.udemy.com/building-recommender-systems-with-machine-learning-and-ai/learn/v4/content)
- 논문

제목 | 저자 | 정리 link
----|----|----
Factorization Machines [(link)](https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf)|Steffen Rendle|
Latent Relational Metric Learning via Memory-based Attention for Collaborative Ranking [(link)](https://arxiv.org/pdf/1707.05176.pdf)|Yi Tay, Luu Anh tuan, Siu Cheung Hui|
Sequential Recommender System based on Hierarchical Attention Network [(link)](https://www.ijcai.org/proceedings/2018/0546.pdf)|Haochao Ying, Fuzhen Zhuang, Yanchi Liu...|
Wide & Deep Learning for Recommender Systems [(link)](https://arxiv.org/pdf/1606.07792.pdf)|Heng-Tze Cheng, Levent Koc, Jeremiah Harmsen...|


[2019-06-22] 컨퍼런스 발표 회의
[2019-06-23] 
[2019-06-24] 리허설에 할 것 준비. item 별 dwelling time
[2019-06-27] 컨퍼런스 리허설

