### 다이나믹 프로그래밍     
---
    
1. 개념       
       
    ✔ 하나의 문제를 여러 개의 부분 문제로 나눠서 해결하는 기법   
    
    ✔ 이미 계산이 끝난 부분 문제가 다시 발생하면 새로 계산하는 것이 아니라 **이전의 계산값을 참조하여 이용하는 것**이 핵심   
    => 시간은 절약할 수 있지만, 이전 값 저장을 위한 공간이 있어야 하기 때문에 시간과 메모리의 trade-off         
         
           
2. 피보나치 수열  
    
    ✔ fibo(N) = fibo(N-1)+fibo(N-2) (fibo(0)=1, fibo(1)=1)     
       
    ✔ 단순 탐색     
    <image src="https://cdn.codeground.org/cg/images/note/algorithm_8-1.jpg">        
    => 같은 파라미터를 가진 함수를 중복 호출하게 되어 매우 비효율적    
    => **✨Memoization✨**으로 해결               
            
    ✔ Memoization : 한 번 계산된 값을 기록해두고 이후 중복 호출되었을 때 저장해 둔 값을 가져와 사용하는 방법     
    <image src="https://cdn.codeground.org/cg/images/note/algorithm_8-2.jpg">   