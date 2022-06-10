from djongo import models


class Movies(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    titleId = models.CharField(max_length=25)
    title = models.TextField()
    language = models.CharField(max_length=100)

    class Meta:
        db_table = "movies"
        app_label = "movies"
