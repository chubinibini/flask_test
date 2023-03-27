'''
    메인 서비스를 구축하는 컨트롤러
        - 라우트: url과 이를 처리할 함수 연계
        - 비즈니스 로직: 사용자가 요청하는 주 내용을 처리하는곳
'''
from flask import render_template, request, url_for
from service.controllers import bp_auth as auth

# ~/auth/
@auth.route('/')
def home():
    # url_for("별칭.함수명") => url이 리턴된다
    print(url_for('auth_bp.login'))
    return "auth 홈"

# ~/auth/
@auth.route('/login')
def login():
    print(url_for('auth_bp.login'))
    return "auth login"

# ~/auth/
@auth.route('/logout')
def logout():
    return "auth logout"

# ~/auth/
@auth.route('/signup')
def signup():
    return "auth signup"

# ~/auth/
@auth.route('/delete')
def delete():
    return "auth delete"