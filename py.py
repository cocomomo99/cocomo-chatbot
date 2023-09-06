import requests
from bs4 import BeautifulSoup
from slack_sdk import WebClient
import schedule
import time

# 크롤링 함수
def get_school_menu():
    url = "https://today.jnu.ac.kr/Program/MealPlan.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 웹사이트의 구조에 따라 아래 코드 수정 필요
    menu = soup.select_one("메뉴 정보 선택자").text

    return menu

# Slack 메시지 전송 함수
def send_to_slack(menu):
    token = "YOUR_SLACK_TOKEN"
    channel = "#general"
    client = WebClient(token=token)
    client.chat_postMessage(channel=channel, text=menu)

# 스케쥴링된 작업
def scheduled_job():
    menu = get_school_menu()
    send_to_slack(menu)

# 매일 오전 7시 30분에 작업 실행
schedule.every().day.at("07:30").do(scheduled_job)

while True:
    schedule.run_pending()
    time.sleep(60)  # 1분마다 스케쥴 확인