import time
import config.webDriver
from config.webDriver import config_omniNotes_wd
from config.webDriver import get_elementXpath, get_elementId
from utills.interaction_utils import window_swipe_left, window_swipe_right
# webDriver 실행
# testcase 앱 시작 위치에 따라 app_package 값과 app_activity 값을 전달해서 실행한다
def intro_wd():
    app_package = None
    app_activity = None
    wd = config_omniNotes_wd(app_package, app_activity)
    return wd
# 해당 테스트 파일 스크린샷 저장할 경로
screenshot_path = r'C:/Workspace/2024/omninote_20240511/testResult/'
def scr(wd, scrName):
    # 파일 이름만 붙여 저장하도록 함
    scr = config.webDriver.screenshot(wd, screenshot_path + scrName)
    return  scr
# 권한 설정 패스 임시 코드
def temp(wd):
    print('>> temp')
# 서비스 권한 알림 확인 버튼 클릭
    btnConfirm_id = 'com.claf.InstaWash:id/btnConfirm'
    permission_allow_foreground_only_button_id = 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'
    btnConfirm_ele = get_elementId(wd,  btnConfirm_id)
    btnConfirm_ele.click()
    time.sleep(2)
    # 위치 추적 허용은 1회 허용 이후 나타나지 않는데 해당 코드는 1회 허용 이후라고 가정한다.
# 국가(Kor) 변경 Testcase
def select_country_kor(wd):
    try:
        btnCountry_id = 'com.claf.InstaWash:id/btnCountry'
        btnCountry_ele = get_elementId(wd, btnCountry_id)
        btnCountry_ele.click()
        time.sleep(2)
        btnKor_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]'
        btnKor_ele = get_elementXpath(wd, btnKor_xpath)
        btnKor_ele.click()
    except:
        print("국가(Kor) 변경 testcase 실패")
    finally:
        time.sleep(2)
# 국가(Jap) 변경 Testcase
def select_country_jp(wd):
    try:
        btnCountry_id = 'com.claf.InstaWash:id/btnCountry'
        btnCountry_ele = get_elementId(wd, btnCountry_id)
        btnCountry_ele.click()

        btnJp_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]'
        btnJp_ele = get_elementXpath(wd, btnKor_xpath)
        btnJp_ele.click()
    except:
        print("국가(Jp) 변경 testcase 실패")

 # 국가(Kor) 확인
def check_country_kor(wd):
    print('>> check_country_kor')
    try:
        countryName_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView'
        countryName_ele = get_elementXpath(wd, countryName_xpath)
        countryName = countryName_ele.text
        if countryName == '대한민국':
            print('국가(Kor) 확인 : PASS')
        else:
            print('국가(Kor) 확인 : FAIL')
            print(countryName)
    except:
        print("국가(Kor) 확인 testcase 실패")
    finally:
        time.sleep(2)
# (Kor) intro 이미지 확인
def intro_image_check_kor(wd):
    print('>> intro_image_check_kor')
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
        print('(Kor) intro 이미지 확인 : PASS')
        time.sleep(2)
    except:
        print("(Kor) 슬라이드 이미지 확인 testcase 실패")
    finally:
        time.sleep(2)

# (Kor) intro 좌우 스와이프 확인
def intro_swipe_kor(wd):
    print('>> intro_swipe_kor')
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
            print('(Kor) intro 좌로 이동 스와이프 확인 : PASS')
            window_swipe_left(wd)
            time.sleep(2)
            # left count 수 만큼 오른쪽으로 스와이프
            while count > 0:
                window_swipe_right(wd)
                time.sleep(1)
                count -= 1
        else:
            print('(Kor) intro 좌로 이동 스와이프 확인 : FAIL')
        # 다음 버튼이 보이면 오른쪽으로 1회 스와이프
        if btnStart_ele.text == '다음':
            print('(Kor) intro 우로 이동 스와이프 확인 : PASS')
            window_swipe_right(wd)
            time.sleep(2)
        else:
            print('(Kor) intro 우로 이동 스와이프 확인 : FAIL')
    except:
        print('(Kor) intro 좌우 스와이프 확인 testcase 실패')
    finally:
        time.sleep(2)

# (Kor) 시작하기 버튼 로그인 진입 확인
def intro_startBtn_kor(wd):
    print('>> intro_startBtn_kor')
    try:
        btnStart_id = 'com.claf.InstaWash:id/btnStart'
        btnStart_ele = get_elementId(wd, btnStart_id)
        # 시작하기 버튼일 경우 클릭
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
            print('(Kor) 시작하기 버튼 로그인 진입 확인 : PASS')
        else:
            print('(Kor) 시작하기 버튼 로그인 진입 확인 : FAIL')
    except:
        print('(Kor) 시작하기 버튼 로그인 진입 확인 testcase 실패')
    finally:
        time.sleep(2)




# testcase 1
# test 가 붙은 def 만 단독으로 실행이 가능한 testcase 이다
# (임시) 의 경우 앱 액티비티가 해결될 경우 필요없는 기능이다 (테스트 시작 지점으로 가기 위한 임시 코드)
# (사전조건 : 디바이스 언어 설정 (한국어))
def test_intro_kor(wd):
    # (임시) 서비스 권한 확인
    temp(wd)
    # 국가 설정 확인
    check_country_kor(wd)
    # 슬라이드 기능 확인
    intro_swipe_kor(wd)
    # intro 이미지 확인 & 다음 버튼 기능 확인
    intro_image_check_kor(wd)
    # 시작하기 버튼 기능 확인
    intro_startBtn_kor(wd)

    # 약관동의부터는 로그인과 연결하는 것이 좋다 (로그인 후 확인이 이어지기 때문)

# 테스트 실패 시 재시작하는 기능 만들고 싶다


# testcase 2
# 국가 변경 (사전조건 : 디바이스 언어 설정 (일본어))
# 슬라이드 이미지 확인
# 슬라이드 기능 확인
# 다음 버튼 기능 확인
# 시작하기 버튼 기능 확인
# 로그인 화면 진입 확인