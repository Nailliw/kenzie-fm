from django.db import models


# Você pode colocar atributos nos models
# Utilizando Herança
# class ModelWithDateTime():
# added_at = models.DateTimeField(auto_now_add=True)


# N -> N entre Band e Tag


class Tag(models.Model):
    name = models.CharField(max_length=255)
    # declarar o relacionamento do lado do tag
    # é exatamente a mesma coisa
    # bands = models.ManyToManyField(Band, related_name='tags')

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=255)
    # name = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name="bands")
    # added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# 1 -> N entre Band e Album


class Album(models.Model):
    title = models.CharField(max_length=255)
    n_tracks = models.IntegerField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    # se quiserem alterar o atributo album_set para 'albums':
    # band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='albums')
