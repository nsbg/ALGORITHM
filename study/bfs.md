### 너비 우선 탐색        
---
     
1. 개념       
        
    ✔ 그래프의 모든 정점들을 특정한 순서에 따라 방문하는 알고리즘         
         
    ✔ 시작점과 가까운(이동에 필요한 간선의 수가 적은) 정점 순서로 방문하게 됨     
         
    ✔ 시간 복잡도 : O(V+E) => 모든 정점을 방문하며 모든 간선을 검사                                       
         
      

2. 방법      
           
    ✔ 현재 정점과 인접한 간선들을 검사하다가 **방문하지 않은 정점들을 발견**하면 **그 간선을 통해 방문하지 않은 정점들을 자료구조 큐에 넣음**    
         
    ✔ 큐의 front 정점을 방문하고 pop       
            
    ✔ 큐에 더 이상 정점이 존재하지 않을 때까지 위의 과정을 반복하여 그래프의 모든 정점 방문                                
           
        

3. 구현 방식 : 인접 행렬 / 인접 리스트    