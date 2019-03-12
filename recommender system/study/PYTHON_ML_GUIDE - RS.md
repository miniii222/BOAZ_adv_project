추천시스템 (Recommender System) 정리
===================================
- 선택된 콘텐츠와 연관된 추천 콘텐츠가 얼마나 사용자의 관심을 끌고 개인에게 맞춘 콘텐츠를 추천했는지.
- 사용자 자신도 몰랐던 취향을 시스템이 발견하고 콘텐츠를 추천

* * *

## 1. 컨텐츠 기반 필터링(Content Based Filtering)
* 사용자가 특정한 아이템을 매우 선호하는 경우, 그 아이템과 비슷한 콘텐츠를 가진 다른 아이템을 추천.
* 특정 영화에 높은 평점을 줬다면 그 영화의 장르, 출연 배우, 감독, 영화 키워드 등의 콘텐츠와 유사한 다른 영화 추천

* * *
## 2. 협업 필터링(Collaborative Filtering)
* 사용자가 아직 평가하지 않은 아이템을 예측 평가하는 것.
* 사용자가 평가한 다른 아이템을 기반으로 사용자가 평가하지 않은 아이템의 예측 평가를 도출.
* 사용자 - 아이템 평점 행렬 only. (Sparse Matrix)

  ### 1. Nearest Neighbor(Memory)
    - 취향이 비슷한 친구들에게 영화가 어땠는지를 물어보는 것과 비슷.
    - 사용자가 아이템에 매긴 평점 정보나 상품 구매 이력과 같은 사용자 행동 양식(User Behavior)만을 기반으로 추천.
    #### 사용자 기반(User-User) : 당신과 비슷한 고객들이 다음 상품도 구매했습니다. 
      + 특정 사용자와 유사한 다른 사용자를 TOP-N으로 선정. TOP-N 사용자가 좋아하는 아이템을 추천.
      + 특정 사용자와 타 사용자 간의 유사도(Similarity)를 측정한 뒤 가장 유사도가 높은 N명의 사용자들이 선호하는 아이템을 추천.
      
    #### 아이템 기반(Item-Item) : 이 상품을 선택한 다른 고객들은 다음 상품도 구매했습니다.
      + 아이템이 가지는 속성과 상관없음.
      + 사용자들이 그 아이템을 좋아하는지/싫어하는지의 평가 척도가 유사한 아이템을 추천하는 기준.

    - 일반적으로 User-based << Item-based
    - 비슷한 상품을 구입한다고 해서 사람들의 취향이 비슷하다고 판단할 수 없다. 유행하거나, 유명한 상품들은 취향과 관계없음.
    - 사용자들이 평점을 매긴 경우도 많지 않다.
    - 대부분 Item-Item 알고리즘 적용.
    - 유사도를 구할 때는 대부분 `코사인 유사도` 적용.
  
  ### 2. Latent Factor
    - User-Item Matrix(사용자-아이템 평점 매트릭스) 속에 숨어 있는 잠재 요인을 추출해 추천 예측.
    - Matrix Factorization : SVD와 같은 차원 감소 기법으로 분해하는 과정에서 `잠재 요인` 추출.
    - U x I = U x f * f x I (U : users / I : items / f : factors 잠재요인)
    -   R   =   P   *   Q
    - 다차원 희소 행렬 -> 저차원 밀집 행렬
    - 사용자가 아직 평점을 부여하지 않은 아이템에 대한 예측 평점을 생성.
    #### SVD(Singular value Decomposition)
     - R = P*Q 로 분해하는 방법
     - NaN 값이 없는 행렬에만 이용.
     - SGD, ALS 방식의 SVD
    #### SVD(Singular value Decomposition)
      1. P와 Q를 임의의 값을 가진 행렬로 선정.
      2. P와 Q값을 곱해 예측 R행렬을 계산하고 예측R 행렬과 실제 R행렬에 해당하는 오류 값 계산.
      3. 오류 값을 최소화할 수 있도록 P와Q행렬 업데이트
      4. 만족할 만한 값을 가질 때까지 2,3 반복
     - 구현 code : [link](https://github.com/miniii222/BOAZ_adv_project/blob/master/recommender%20system/study/PYTHON_ML_GUIDE%20-%20SVD_SGD.ipynb)
     
     
### Example code
- Content based - [link](https://github.com/miniii222/BOAZ_adv_project/blob/master/recommender%20system/study/Content_based_ex_TMDB.ipynb)
     
      
      
