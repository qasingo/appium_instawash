from appium import webdriver
from appium.webdriver.common.appiumby import By
from appium.options.android import UiAutomator2Options
import time

# 테스트 빌드 경로
instawashTestApp = r'C:/Workspace/2024/appium_instawash/apk/Instawash-5.65.5.apk'
# 테스트 디바이스 정보
device_s9 = '228818e4410b7ece'       # deviceName
avdevice_px3 = 'Pixel_3_API_31' # avdName
# 디바이스 환경 및 디바이스 대상 지정하여 실행
def instawash_wd(app_package, app_activity):
  # option 설정
  options = UiAutomator2Options()
  options.app = instawashTestApp
  options.auto_grant_permissions = True
  # options.language = ''
  print('APK: ' + instawashTestApp)
  if app_package is not None and app_activity is not None:
    options.app_activity = app_activity
    options.app_package = app_package
    print("앱 패키지 및 액티비티 설정 완료")
  else:
    print("앱 패키지 및 액티비티 설정 없음")

  # 물리 디바이스 사용 시 사용하는 옵션
  # options.device_name = device_s9
  # 가상 디바이스 사용 시 사용하는 옵션
  options.avd = avdevice_px3
  print(f'테스트 디바이스 : {avdevice_px3}')

  wd = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
  print("테스트 대상 실행 완료")
  time.sleep(10)
  return wd
def get_elementId(wd, id):
  element = wd.find_element(By.ID,id)
  return element
# xpath 를 통해 element 를 찾아 반환
def get_elementXpath(wd, xpath):
  element = wd.find_element(By.XPATH, xpath)
  return element
# 스크린샷 찍는 기능
def screenshot(wd,screenshot_path):
  wd.get_screenshot_as_file(screenshot_path)  # 저장할 스크린샷 파일 경로