import requests

BASE_URL = "https://catfact.ninja/facts"

def main():
    # 1. Получаем первую страницу фактов
    response = requests.get(BASE_URL)
    response.raise_for_status()
    data = response.json()

    # 2. Выясняем, сколько всего фактов
    total = data["total"]
    per_page = data["per_page"]

    # 3. Вычисляем номер последней страницы
    last_page = (total + per_page - 1) // per_page

    print(f"Всего фактов: {total}")
    print(f"Фактов на странице: {per_page}")
    print(f"Номер последней страницы: {last_page}")

    # 4. Получаем последнюю страницу
    response_last = requests.get(BASE_URL, params={"page": last_page})
    response_last.raise_for_status()
    last_data = response_last.json()

    print(f"Запрос к последней странице: {response_last.url}")

    # 5. Находим самый короткий факт
    facts = [fact["fact"] for fact in last_data["data"]]
    shortest_fact = min(facts, key=len)

    print("Самый короткий факт на последней странице:")
    print(shortest_fact)


if __name__ == "__main__":
    main()
