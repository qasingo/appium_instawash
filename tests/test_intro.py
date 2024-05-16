import time
import config.webDriver
from config.webDriver import instawash_wd
from config.webDriver import get_elementXpath, get_elementId
from utils.interaction_utils import window_swipe_left, window_swipe_right

# TC 생성
import pandas as pd
testResults = []
# 테스트 파일 스크린샷 저장할 경로
screenshot_path = r'C:/Workspace/2024/appium_instawash/testResult/'
testResult_path = r'C:/Workspace/2024/appium_instawash/testResult/'
# webDriver 실행
# TC 앱 시작 위치에 따라 app_package 값과 app_activity 값을 전달해서 실행한다
def intro_wd():
    print('>> intro_wd')
    app_package = None
    app_activity = None
    wd = instawash_wd(app_package, app_activity)
    return wd
def scr(wd, scrName):
    print('>> scr')
    # 파일 이름만 붙여 저장하도록 함
    scr = config.webDriver.screenshot(wd, screenshot_path + scrName)
    return  scr
# 테스트 tc결과를 받아 리스트에 저장한다.
def testResultData(depth1, depth2, depth3,
                    testDescription, preCondition, testStep,
                    expectedResult, autoTestResult, notes):
    print('>> testResultData')
    testResults.append((depth1, depth2, depth3,
                    testDescription, preCondition, testStep,
                    expectedResult, autoTestResult, notes))
# 테스트파일명, 결과, 파일 저장 경로를 받아서 Testcase 를 생성한다.
# 결과리스트가 저장될 칼럼을 생성하여 xlsx 파일 형태로 저장한다.
def creatTestcase(testName, testResults,testResult_path):
    print('>> creatTestcase')
    detaFrame = pd.DataFrame(testResults, columns=['depth1', 'depth2', 'depth3',
                    'testDescription', 'preCondition', 'testStep',
                    'expectedResult', 'autoTestResult', 'notes'])
    save_path = testResult_path + testName + '.xlsx'
    detaFrame.to_excel(save_path)

# 권한 설정 패스 임시 코드
# 위치 추적 허용은 1회 허용 이후 나타나지 않는데 해당 코드는 1회 허용 이후라고 가정한다.
def temp(wd):
    print('>> temp')
# 서비스 권한 알림 확인 버튼 클릭
    btnConfirm_id = 'com.claf.InstaWash:id/btnConfirm'
    permission_allow_foreground_only_button_id = 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'
    btnConfirm_ele = get_elementId(wd,  btnConfirm_id)
    btnConfirm_ele.click()
    time.sleep(2)

# 국가(kr) 변경 Testcase
def select_country_kr(wd):
    print('>> select_country_kr')
    depth1 = 'intro'
    depth2 = '국가'
    depth3 = ''
    preCondition = '국가 설정 일본 상태'
    testDescription = '국가 일본 > 대한민국 변경 확인'
    testStep  = ('1) 왼쪽 상단 국가 선택 버튼을 클릭한다.'
                          '2) 나타난 국가 선택 팝업창에서 대한민국 버튼을 클릭한다.'
                          '3) 대한민국 으로 국가 버튼이 변경됨')
    expectedResult = '왼쪽 상단 국가명이 대한민국 으로 변경됨'
    try:
        btnCountry_id = 'com.claf.InstaWash:id/btnCountry'
        btnCountry_ele = get_elementId(wd, btnCountry_id)
        btnCountry_ele.click()
        time.sleep(2)
        btnKor_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]'
        btnKor_ele = get_elementXpath(wd, btnKor_xpath)
        btnKor_ele.click()
        time.sleep(2)
        autoTestResult = check_country_kr(wd)
    except:
        print("국가(kr) 변경 testcase 실패")
        autoTestResult = 'N/A'
    finally:
        time.sleep(2)
        notes = ''
        return  depth1, depth2, depth3, testDescription, preCondition, testStep,expectedResult, autoTestResult, notes
# 국가(jp) 변경 Testcase
def select_country_jp(wd):
    try:
        btnCountry_id = 'com.claf.InstaWash:id/btnCountry'
        btnCountry_ele = get_elementId(wd, btnCountry_id)
        btnCountry_ele.click()
        time.sleep(2)
        btnJp_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]'
        btnJp_ele = get_elementXpath(wd, btnKor_xpath)
        btnJp_ele.click()
        print('국가(kr) 변경')
        time.sleep(2)
        check_country_jp(wd)
    except:
        print("국가(jp) 변경 testcase 실패")
    finally:
        time.sleep(2)

 # 국가(kr) 확인
def check_country_kr(wd):
    print('>> check_country_kr')
    result = ''
    try:
        countryName_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView'
        countryName_ele = get_elementXpath(wd, countryName_xpath)
        countryName = countryName_ele.text
        if countryName == '대한민국':
            print('국가(kr) 확인 : PASS')
            result = 'PASS'
        else:
            print('국가(kr) 확인 : FAIL')
            result = 'FAIL'
            print(countryName)
    except:
        print("국가(kr) 확인 testcase 실패")
        result = 'N/A'
    finally:
        time.sleep(2)
        return  result
# 국가(jp) 확인
def check_country_jp(wd):
    print('>> check_country_jp')
    try:
        countryName_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView'
        countryName_ele = get_elementXpath(wd, countryName_xpath)
        countryName = countryName_ele.text
        if countryName == '':
            print('국가(jp) 확인 : PASS')
        else:
            print('국가(jp) 확인 : FAIL')
            print(countryName)
    except:
        print("국가(jp) 확인 testcase 실패")
    finally:
        time.sleep(2)
# (kr) intro 이미지 확인
def page_check_kr(wd):
    print('>> page_check_kr')
    depth1 = 'intro'
    depth2 = '인트로 페이지 & 다음 버튼'
    depth3 = ''
    preCondition = ''
    testDescription = '한국 인트로 페이지 및 다음 버튼 기능 확인'
    testStep = ('1) 한국 인트로 1~3 페이지 확인'
                '2) 1~3 페이지 하단 다음 버튼 클릭'
                '3) 4 페이지 하단 시작하기 버튼 확인')
    expectedResult = ('1) 한국 인트로 페이지 노출'
                      '2) 다음 버튼 클릭 시 다음 페이지로 이동'
                      '3) 마지막 페이지 다음 버튼이 시작하기 버튼으로 변경됨')
    # 인트로 이미지를 스크린샷으로 찍어 저장한다
    # 버튼의 text 가 변경될 때까지 스크린샷을 찍도록 함
    try:
        btnStart_id = 'com.claf.InstaWash:id/btnStart'
        btnStart_ele = get_elementId(wd, btnStart_id)
        count = 0
        while btnStart_ele.text == '다음':
            count += 1
            saveName = '(kr)intro_' + str(count) + '.png'
            scr(wd, saveName)
            print(saveName)
            time.sleep(2)
            btnStart_ele.click()
            time.sleep(2)
        scr(wd, '(kr)intro_last.png')
        print('(kr)intro_last.png')
        print('(Kr) intro 이미지 확인 : PASS')
        autoTestResult = 'PASS'
    except:
        print("(Kr) 슬라이드 이미지 확인 testcase 실패")
        autoTestResult = 'N/A'
    finally:
        time.sleep(2)
        notes = '저장된 스크린샷 확인 필요'
        return depth1, depth2, depth3, testDescription, preCondition, testStep, expectedResult, autoTestResult, notes

# (kr) intro 좌우 스와이프 확인
# 첫번째 intro 페이지에서 시작해야하는 사전조건이 있으나 코드로 구현하지 못했다.
# 좌/우 케이스를 나누는게 좋을 것 같다.
def page_swipe_kr(wd):
    print('>> page_swipe_kr')
    depth1 = 'intro'
    depth2 = '스와이프'
    depth3 = ''
    preCondition = ''
    testDescription = '스와이프 기능 확인'
    testStep = ('1) intro 첫페이지에서 스와이프하여 앞페이지로 이동 . \n'
                '2) 스와이프하여 intro 마지막 페이지로 이동 .\n'
                '3) 마지막 페이지에서 스와이프하여 뒷페이지로 이동')
    expectedResult = ('1) 첫페이지에서 스와이프로 앞페이지 이동 불가'
                      '2) 스와이프하여 마지막 페이지로 이동'
                      '3) 마지막 페이지에서 스와이프하여 뒷페이지로 이동 불가')
    try:
        btnStart_id = 'com.claf.InstaWash:id/btnStart'
        btnStart_ele = get_elementId(wd, btnStart_id)
        count = 0
        # 다음 버튼이 보이면 왼쪽으로 스와이프
        while btnStart_ele.text == '다음':
            window_swipe_left(wd)
            time.sleep(1)
            count += 1
        # 시작하기 버튼이 보이면 왼쪽으로 1회 스와이프
        if btnStart_ele.text == '시작하기':
            print('(kr) intro 좌로 스와이프 확인 : PASS')
            window_swipe_left(wd)
            time.sleep(2)
            # left count 수 만큼 오른쪽으로 스와이프
            while count > 0:
                window_swipe_right(wd)
                time.sleep(1)
                count -= 1
            autoTestResult = 'PASS'
        else:
            print('(kr) intro 좌로 스와이프 확인 : FAIL')
            autoTestResult = 'FAIL'
        # 다음 버튼이 보이면 오른쪽으로 1회 스와이프
        if btnStart_ele.text == '다음':
            print('(kr) intro 우로 스와이프 확인 : PASS')
            window_swipe_right(wd)
            autoTestResult = 'PASS'
            time.sleep(2)
        else:
            print('(kr) intro 우로 스와이프 확인 : FAIL')
            autoTestResult = 'FAIL'
    except:
        print('(kr) intro 좌우 스와이프 확인 testcase 실패')
        autoTestResult = 'N/A'
    finally:
        time.sleep(2)
        notes = ''
        return depth1, depth2, depth3, testDescription, preCondition, testStep, expectedResult, autoTestResult, notes

# (kr) 시작하기 버튼 로그인 진입 확인
def startLogin_startBtn_kr(wd):
    print('>> startLogin_startBtn_kr')
    depth1 = 'intro'
    depth2 = '시작하기'
    depth3 = ''
    preCondition = ''
    testDescription = '시작하기 버튼으로 로그인 진입'
    testStep = ('1) 인트로 마지막 페이지에서 시작하기 버튼 클릭\n'
                '2) 약관 동의 팝업 전체 동의 후 시작하기 클릭\n'
                '3) 마케팅 수신 동의 확인 클릭')
    expectedResult = ('번호 로그인 페이지 진입')
    try:
        btnStart_id = 'com.claf.InstaWash:id/btnStart'
        btnStart_ele = get_elementId(wd, btnStart_id)
        # (사전 조건 세팅) 다음 일 경우 계속 다음 클릭
        while btnStart_ele.text == '다음':
            btnStart_ele.click()
            time.sleep(2)
        # 시작하기 버튼일 경우 1회 클릭
        if btnStart_ele.text == '시작하기':
            btnStart_ele.click()
            time.sleep(2)
            # 전체동의 클릭
            checkbox_all_id = 'com.claf.InstaWash:id/checkbox_all'
            checkbox_all_ele = get_elementId(wd, checkbox_all_id)
            checkbox_all_ele.click()
            time.sleep(2)
            # 동의하고 시작하기 클릭
            btnConfirm1_id = 'com.claf.InstaWash:id/btnConfirm'
            btnConfirm1_ele = get_elementId(wd, btnConfirm1_id)
            btnConfirm1_ele.click()
            time.sleep(2)
            # 마케팅정보 앱 푸시 동의 확인 클릭
            btnConfirm2_id = 'com.claf.InstaWash:id/btnConfirm'
            btnConfirm2_ele = get_elementId(wd, btnConfirm2_id)
            btnConfirm2_ele.click()
            time.sleep(2)
        # RESULT
        # 로그인 화면 진입 확인
        textViewTitle_id = 'com.claf.InstaWash:id/textViewTitle'
        textViewTitle_ele = get_elementId(wd, textViewTitle_id)
        if textViewTitle_ele.text == '전화번호를 입력해 주세요.':
            print('(kr) 시작하기 버튼 로그인 진입 확인 : PASS')
            autoTestResult = 'PASS'
        else:
            print('(kr) 시작하기 버튼 로그인 진입 확인 : FAIL')
            autoTestResult = 'FAIL'
    except:
        print('(kr) 시작하기 버튼 로그인 진입 확인 testcase 실패')
        autoTestResult = 'N/A'
    finally:
        time.sleep(2)
        notes = ''
        return depth1, depth2, depth3, testDescription, preCondition, testStep, expectedResult, autoTestResult, notes


# (임시) temp 의 경우 앱 액티비티가 해결될 경우 필요없는 기능이다 (테스트 시작 지점으로 가기 위한 임시 코드)
# (사전조건 : 디바이스 언어 설정 (한국어))
def runTest_intro_kr(wd, testDate):
    print('인트로 테스트 kr 시작_' + testDate)
    # (임시) 서비스 권한 확인
    temp(wd)
    # 국가 선택 및 설정 확인
    testResultData(*select_country_kr(wd))
    # 슬라이드 기능 확인
    testResultData(*page_swipe_kr(wd))
    # intro 이미지 확인 & 다음 버튼 기능 확인
    testResultData(*page_check_kr(wd))
    # 시작하기 버튼 기능 확인
    testResultData(*startLogin_startBtn_kr(wd))
    print(testResults)

    testName = 'introTest_' + testDate
    # 해당 엑셀 파일이 열려있는 경우 오류 발생하니 주의
    creatTestcase(testName,testResults, testResult_path)


# 테스트 실패 시 재시작하는 기능 만들기 (try-except 에 들어갈 기능)
# 일본 테스트 케이스 만들기
# 디바이스 언어 설정 기능 만들기(사전조건 : 디바이스 언어 설정 (일본어/한국어))