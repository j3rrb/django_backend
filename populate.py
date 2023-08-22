import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atividade3.settings")

import django

django.setup()


from main.models import Access, Page, Topic
from faker import Faker
import random


topics_names = ["Esportes", "Entretenimento", "Games", "Política", "Economia"]

fake = Faker()

for page in topics_names:
    topic = Topic(name=page)
    topic.save()

    page = Page(name=f"Página sobre {page.lower()}", topic=topic)
    page.save()
    

for i in range(10):
    access = Access(
        page=Page.objects.get(name=f"Página sobre {random.choice(topics_names).lower()}"),
    )
    access.save()
