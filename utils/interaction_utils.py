# 전체 화면 오른쪽에서 왼쪽으로 스와이프
def window_swipe_left(wd):
    size = wd.get_window_size()
    start_x = size['width'] * 0.9
    end_x = size['width'] * 0.1
    y = size['height'] * 0.5
    duration = 800  # 밀리초 단위

    wd.swipe(start_x, y, end_x, y, duration)

# 전체 화면 왼쪽에서 오른쪽으로 스와이프
def window_swipe_right(wd):
    size = wd.get_window_size()
    start_x = size['width'] * 0.1
    end_x = size['width'] * 0.9
    y = size['height'] * 0.5
    duration = 800  # 밀리초 단위

    wd.swipe(start_x, y, end_x, y, duration)