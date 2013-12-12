from levsdelight_com.models import Slideshow
import csv
import datetime

with open('november-slides.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print row[1]
        print row[2]
        print row[3]
        print row[4]
        print row[5]
        print row[6]
        slide = Slideshow()
        slide.title = str(row[1])
        slide.desc = str(row[2])
        slide.pictureLocation = str(row[3])
        slide.isActive = int(row[4])
        slide.slideshow_id = int(row[5])
        slide.order_id = int(row[6])
        slide.pub_date = datetime.datetime.now()
        slide.save()
# f = open('/Users/jlevinsohn/Downloads/sllideshow-demo.csv', 'r')
# for line in f:
#     print line

# f.close()
