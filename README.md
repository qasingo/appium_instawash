# appium_instawash
instawash appium test automation
## main.py
이 파일은 테스트 케이스를 실행하는 엔트리 포인트입니다. 테스트를 실행할 테스트 케이스의 wd 와 runTest_ 함수를 호출하여 사용합니다.
원하는 테스트만 실행할 수 있습니다.

## tests/intro_tc.py
이 파일에는 인트로 테스트 케이스 및 관련 기능이 정의되어 있습니다. intro(kr) 화면에서 로그인 진입까지 테스트를 진행하고 결과를 엑셀파일로 생성합니다.

## config/webDriver.py
이 파일은 WebDriver 관련 설정 및 기능을 정의합니다. 테스트 앱의 경로, 디바이스 정보 및 WebDriver 초기화에 관련된 함수들이 포함되어 있습니다. element 를 찾는 함수와 스크린샷을 찍는 함수도 이곳에 있습니다.

## utills/interaction_utils.py
이 파일에는 테스트를 수행하는 유틸리티 함수가 포함되어 있습니다. 현재는 화면을 왼쪽 또는 오른쪽으로 스와이프할 수 있는 기능이 구현되어 있습니다.

### 앞으로 할 일
1. 테스트케이스 생성 부분을 분리하기
2. intro(jp) 테스트 생성하기
