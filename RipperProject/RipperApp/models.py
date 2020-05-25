from django.core.validators import FileExtensionValidator
from django.db import models


class Song(models.Model):
    genreList = (("No genre", " "),
                 ("Alternative", "Alternative"),
                 ("Alternative/Indie", "Alternative/Indie"),
                 ("Blues/R&B", "Blues/R&B"),
                 ("Books & Spoken", "Books & Spoken"),
                 ("Children's Music", "Children's Music"),
                 ("Classic Rock", "Classic Rock"),
                 ("Classic Rock/Rock", "Classic Rock/Rock"),
                 ("Classical", "Classical"),
                 ("Country", "Country"),
                 ("Dance", "Dance"),
                 ("Easy Listening", "Easy Listening"),
                 ("Electronic", "Electronic"),
                 ("Folk", "Folk"),
                 ("Hip Hop/Rap", "Hip Hop/Rap"),
                 ("Holiday", "Holiday"),
                 ("House", "House"),
                 ("Industrial", "Industrial"),
                 ("Jazz", "Jazz"),
                 ("Leftfield", "Leftfield"),
                 ("New Age", "New Age"),
                 ("Other", "Other"),
                 ("Pop", "Pop"),
                 ("Pop/Rock", "Pop/Rock"),
                 ("R&B", "R&B"),
                 ("R&B/Soul", "R&B/Soul"),
                 ("Religious", "Religious"),
                 ("Rock", "Rock"),
                 ("Rock & Roll", "Rock & Roll"),
                 ("Soundtrack", "Soundtrack"),
                 ("Techno", "Techno"),
                 ("Trance", "Trance"),
                 ("Unclassifiable", "Unclassifiable"),
                 ("Vocal", "Vocal"),
                 ("World", "World"))

    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=genreList, default=" ")


def user_directory_path(instance, filename):
    return 'Users/user_{0}/{1}'.format(instance.owner.id, filename)


class Document(models.Model):
    docfile = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=['mp3'])])

