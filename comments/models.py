from djongo import models


class Comments(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    review = models.TextField()
    sentiment = models.CharField(max_length=25)
    

    class Meta:
        db_table = "comments"
        app_label = "comments"
