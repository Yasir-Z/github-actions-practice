import requests

def get_random_quote():
    url = "https://api.quotable.io/random"

    try:
        response = requests.get(url)
        data = response.json()

        quote = data["content"]
        author = data["author"]

        print("\n📖 Random Quote")
        print("----------------------------")
        print(f'"{quote}"')
        print(f"- {author}")

    except Exception as e:
        print("❌ Error fetching quote:", e)


if __name__ == "__main__":
    get_random_quote()
