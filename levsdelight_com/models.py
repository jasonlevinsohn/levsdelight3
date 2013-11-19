from django.db import models

class Slideshow(models.Model):
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=2000)
    pictureLocation = models.CharField(max_length=200)
    isActive = models.BooleanField()
    slideshow_id = models.IntegerField()
    order_id = models.IntegerField()
    pub_date = models.DateTimeField('date_pubished')

    def __unicode__(self):
        return "Id: \"%s\" - Title: \"%s\" for Slideshow: \"%s\" - Order: \"%s\"" % (self.slideshow_id, self.title, str(self.slideshow_id), str(self.order_id))


class MonthMap(models.Model):
    slideshow_id = models.IntegerField()
    month = models.CharField(max_length=20)
    year = models.IntegerField()

    def __unicode__(self):
        return "Id: \"%s\" - Month: \"%s\" - Year: \"%s\"" % (self.slideshow_id, self.month, self.year)

# NOTE: After you create the model here, don't forget
# to register it with the admin library. 
# Open levsdelight_com/admin.py
# admin.site.register(<model_name>)
