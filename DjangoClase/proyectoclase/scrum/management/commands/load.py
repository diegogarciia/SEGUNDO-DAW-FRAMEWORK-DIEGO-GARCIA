from django.core.management.base import BaseCommand
from ...models import *
from faker import Faker

class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker('es_ES')

        help = 'Comando inicial'

        for _ in range(5):
            usuario = Usuario(nombre= fake.first_name(), apellido= fake.last_name())
            usuario.save()
            tarea = Tarea(nombre="Revisar código", usuario=usuario, descripcion="Mirar errores de la APP", dificultad="Media")
            tarea.save()

        self.stdout.write(self.style.SUCCESS('Usuario(s) creado correctamente'))
        self.stdout.write(self.style.SUCCESS('Tarea creada correctamente'))

        cantidad = Usuario.objects.filter(nombre='Cristiano', apellido='Ronaldo').update(nombre='Aurelien', apellido="Tchouameni")

        if cantidad > 0:
            self.stdout.write(self.style.SUCCESS(f'Se actualizaron {cantidad} usuario(s) a Tchouameni'))
        else:
            self.stdout.write(self.style.WARNING('No se encontraron usuarios para actualizar'))
