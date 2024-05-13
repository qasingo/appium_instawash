# appium_instawash
instawash appium test automation
main.py
이 파일은 테스트 케이스를 실행하는 엔트리 포인트입니다. 테스트를 실행할 테스트 케이스의 wd 와 test_ 함수를 호출하여 사용합니다.
원하는 테스트만 실행할 수 있습니다.

tests/intro_tc.py
이 파일에는 인트로 테스트 케이스 및 관련 기능이 정의되어 있습니다. 현재는 한국(kr) 테스트 케이스만 작성되어 있으며 intro 화면에서 로그인 진입까지가 테스트 범위입니다. 한국(kr) 및 일본(jp) 국가별 테스트가 추가될 예정입니다.

config/webDriver.py
이 파일은 WebDriver 관련 설정 및 기능을 정의합니다. 테스트 앱의 경로, 디바이스 정보 및 WebDriver 초기화에 관련된 함수들이 포함되어 있습니다. element 를 찾는 함수와 스크린샷을 찍는 함수도 이곳에 있습니다.

utills/interaction_utils.py
이 파일에는 테스트를 수행하는 유틸리티 함수가 포함되어 있습니다. 현재는 화면을 왼쪽 또는 오른쪽으로 스와이프할 수 있는 기능이 구현되어 있습니다.
