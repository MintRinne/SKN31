# run2.py
#모듈에 있는 일부 함수, 클래스, 변수를 import -> 이름으로 호출

from calc import plus, minus # calc의 plus, minus 두 함수 사용 
#from 사용할 것이 있는 경로 import 사용할 것(모듈, 모듈 안 함수, 클래스, 변수)

result = plus(100, 200)
result2 = minus(200, 300)
print(result, result2)

#다른 패키지의 모듈 호출
import my_package.greet as h

h.hello_eng()
print(h.__version__)

from my_package import greet #권장
greet.hello_kor()

#패키지 -> 모듈 -> 함수 import
from my_package.greet import hello_kor, hello_eng

hello_eng()

# import 를 하면 PATHONPATH 경로에서 찾는다. (현재 실행 중인 디렉토리)
import sys
sys.path.append(r'c:\temp\lib') #working directory가 아닌 경로에 있는 라이브러리 경로 저장

from new_package import new_module

new_module.test_func()
