from djongo import models


class Ratings(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    tconst = models.CharField(max_length=25)
    averageRating = models.FloatField()
    numVotes = models.IntegerField()

    class Meta:
        db_table = "ratings"
        app_label = "movies"
