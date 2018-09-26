from flask import Flask
from flask import render_template
import requests
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///starred.sqlite3"
app.config["SECRET_KEY"] = "6f^&YG&F^rf"
db = SQLAlchemy(app)
last_update = 0


class repo(db.Model):
    repo_id = db.Column("repo_id", db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(100))
    description = db.Column(db.String(200))
    stars = db.Column(db.Integer)

    created_date = db.Column(db.String(50))
    last_push_date = db.Column(db.String(50))

    def __init__(self, repo_id, name, url, description, num_stars, created_date, last_push_date):
        self.repo_id = repo_id
        self.name = name
        self.url = url
        self.description = description
        self.stars = num_stars
        self.created_date = created_date
        self.last_push_date = last_push_date


def fetch_data():
    print("Database refreshed")
    db.session.query(repo).delete()
    api_url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&page=1&per_page=10"
    response = requests.get(api_url).json()
    for github_repo in response["items"]:
        current_repo = repo(
            github_repo["id"],
            github_repo["name"],
            github_repo["html_url"],
            github_repo["description"],
            github_repo["stargazers_count"],
            github_repo["created_at"],
            github_repo["pushed_at"],
        )
        db.session.add(current_repo)
    db.session.commit()


@app.route("/")
def list_all():
    fetch_data()
    return render_template("list.html", repos=repo.query.all())


@app.route("/<int:query_id>")
def details(query_id):
    return render_template("details.html", repo=repo.query.get(query_id))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
