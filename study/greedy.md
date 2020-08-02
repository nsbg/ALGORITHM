### 탐욕 알고리즘    
        
1. 개념       
       
    ✔ 여러 경우 중 하나를 결정해야 할 때마다 **그 순간에** 최적이라고 생각되는 것을 선택하는 방식     
    
    ✔ 그 순간에 가장 좋은 것을 선택하기 때문에 최적의 해는 아니지만 최악의 해도 아님     
     
    <img src="https://media.vlpt.us/post-images/cyranocoding/c8b8eff0-b228-11e9-89af-8fc0a61dbc3e/1CeFxqV8wFf2NaQm1hqYGMQ.png">     
      
     
       
2. 적용   
    
    ✔ 아래 조건 만족할 경우 효과적인 알고리즘    
     
        1) 앞의 선택이 이후 선택에 영향 주지 않을 때   
        2) 문제에 대한 최적해가 부분문제에 대해서도 최적해일 때    
                  
        => 이 조건이 성립하지 않으면 탐욕 알고리즘으로 최적해 구할 수 없음     
   
    ✔ 매트로이드 : 탐욕 알고리즘으로 언제나 최적해를 구할 수 있는 구조    
       
    ✔ Prim Algorithm, Kruskal Algorithm, Dijkstra Algorithm, 거스름돈 나누기 등     
     
    ✔ [백준 11399](https://www.acmicpc.net/problem/11399), [백준 11047](https://www.acmicpc.net/problem/11047)     
        
         
3. 거스름돈 나누기    
      
    ✔ 가지고 있는 동전들이 서로의 약수/배수여야만 그리디 적용 가능