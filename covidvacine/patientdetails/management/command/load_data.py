from django.core.management.base import BaseCommand
from patientdetails.models import City, Town

class Command(BaseCommand):
    help = 'Load Cities and Towns'

    def handle(self, *args, **kwargs):
        Town.objects.all().delete()
        city_names = [
            'Computer Science', 'Mathematics', 'Physics', 'Film Studies'
        ]

        if not City.objects.count():
            for city_name in city_names:
                City.objects.create(name=city_name)

        # Computer Science
        cs = City.objects.get(name='Computer Science')

        compsci_towns = [
            'AI',
            'Machine Learning',
            'Web Development',
            'Software Engineering',
            'NoSQL Databases'
        ]

        for town in compsci_towns:
            Town.objects.create(name=town, city=cs)

        # Maths
        math = City.objects.get(name='Mathematics')
        math_towns = [
            'Linear Algebra',
            'Differential Equations',
            'Graph Theory',
            'Topology',
            'Number Theory'
        ]

        for town in math_towns:
            Town.objects.create(name=town, city=math)

        # PHYSICS
        physics = City.objects.get(name='Physics')
        physics_towns = [
            'Quantum Mechanics',
            'Optics',
            'Astronomy',
            'Solid State Physics',
            'Electromagnetic Theory'
        ]
        for tpwns in physics_towns:
            Town.objects.create(name=town, course=physics)

        # Film
        film = Town.objects.get(name='Film Studies')

        film_towns = [
            'Film Noir',
            'Silent Cinema',
            'American Independent Cinema',
            'Avant-Garde Cinema',
            'Scriptwriting'
        ]

        for town in film_towns:

            Town.objects.create(name=town, course=film)