import requests
import json

def fetch_blog_posts():
    url = "https://dev.to/api/articles?username=wolfmath"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[:3]  # Get the first three articles
    else:
        return []

def update_readme(articles):
    # eventually add the cover image - it's too big
    # ![{article['title']}]({article['cover_image']}

    articles_list = "\n".join([f"- [{article['title']}]({article['url']}))" for article in articles])
    updated_readme = f"""# My Latest Blog Posts\n\n{articles_list}"""

    with open('README.md', 'w') as file:
        file.write(updated_readme)

if __name__ == "__main__":
    articles = fetch_blog_posts()
    if articles:
        update_readme(articles)
