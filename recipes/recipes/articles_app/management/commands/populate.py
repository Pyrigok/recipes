
from django.core.management.base import BaseCommand

from articles_app.models import ArticleType, Article
from users_app.models import User


class Command(BaseCommand):
    help = "Populates the database with some testing data."

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Started database population process..."))

        if User.objects.filter(username="mike13").exists():
            self.stdout.write(self.style.SUCCESS("Database has already been populated. Cancelling the operation."))
            return

        # Create users
        johnny = User.objects.create_user(email="admin8@i.ua", username="some_username8", password="really_strong_password123")
        johnny.first_name = "Johnny"
        johnny.last_name = "Davis"
        johnny.save()

        # Create categories
        back_end = ArticleType.objects.create(title="back end")
        data_bases = ArticleType.objects.create(title="data bases")
        programming = ArticleType.objects.create(title="Programming")
        caching = ArticleType.objects.create(title="Caching")

        # Create articles
        website_article = Article.objects.create(
           title="How to code and deploy a website?",
           type=back_end,
           description="There are numerous ways of how you can deploy a website...",
        )
        website_article.save()

        google_article = Article.objects.create(
           title="How to improve your Google rating?",
           type=back_end,
           description="Firstly, add the correct SEO tags...",
        )
        google_article.save()

        programming_article = Article.objects.create(
           title="Which programming language is the best?",
           type=back_end,
           description="The best programming languages are:\n1) Python\n2) Java\n3) C/C++...",
        )
        programming_article.save()

        ubuntu_article = Article.objects.create(
            title="Installing the latest version of Ubuntu",
            type=programming,
            description="In this tutorial, we'll take a look at how to setup the latest version of Ubuntu. Ubuntu "
                   "(/ʊˈbʊntuː/ is a Linux distribution based on Debian and composed mostly of free and open-source"
                   " software. Ubuntu is officially released in three editions: Desktop, Server, and Core for "
                   "Internet of things devices and robots.",
        )
        ubuntu_article.save()

        django_article = Article.objects.create(
           title="Django REST Framework and Elasticsearch",
           type=back_end,
           description="In this tutorial, we'll look at how to integrate Django REST Framework with Elasticsearch. "
           "We'll use Django to model our data and DRF to serialize and serve it. Finally, we'll index the data "
           "with Elasticsearch and make it searchable.",
        )
        django_article.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))