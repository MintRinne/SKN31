
from src.common import utils
print( "app테스트")
utils.util_func()

#실행
#project root directory 아래서 실행
# python src\test\app.py -> app.py 실행 : root dir에서 찾음 실행 파일에 같은 계층에 있는 곳

# python -m src.test.app
# 실행하는 디렉토리가 root directory가 되어 import의 시작됨.
# -m은 모듈로 실행시키는 것