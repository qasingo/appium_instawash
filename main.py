import datetime
testDate = datetime.datetime.now().strftime('%m%d(%H%M)')

from tests.test_intro import (intro_wd,
                              runTest_intro_kr)

# 테스트 실행할 wd, 날짜 전송
print(testDate + '테스트 시작')
runTest_intro_kr(intro_wd(), testDate)