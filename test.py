import requests
from bs4 import BeautifulSoup

def get_school_menu():
    url = "https://today.jnu.ac.kr/Program/MealPlan.aspx" # 여기에 실제 웹사이트 URL을 입력해주세요.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 테이블에서 메뉴 정보를 가져오기
    menu_rows = soup.select("table.type1 tbody tr")
    menu_data = []

    for row in menu_rows:
        # "emptyData" id는 제외
        if not row.has_attr("id") or row["id"] != "emptyData":
            date = row.select_one(".food_month").text
            menu_name = row.select("td")[1].text.strip()
            menu_content = row.select("td")[2].text.strip()
            
            menu_data.append({
                "date": date,
                "menu_name": menu_name,
                "menu_content": menu_content
            })

    return menu_data

# 테스트용 코드
if __name__ == "__main__":
    menu = get_school_menu()
    for item in menu:
        print(item["date"], item["menu_name"], item["menu_content"])

