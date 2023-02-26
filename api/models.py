from django.db import models
import random
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

class Certificate(models.Model):
    profile_pic = models.ImageField(null=True, blank = True, upload_to = "certificate/")
    certificate_number = models.CharField(unique=True, max_length=50)
    fullname = models.CharField(max_length=225)
    role = models.CharField(max_length=225)
    organization = models.CharField(default="Kartexa", max_length=255)
    internship_organizer = models.CharField(max_length=225)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    issue_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    verification_link= models.URLField(max_length=200, blank=True, null=True)
    qr_image = models.ImageField(upload_to='qrcode', blank=True, null=True)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.verification_link)
        canvas = Image.new("RGB", (400,400), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_image.save(f'image{random.randint(0,9999)}.png', File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fullname} | {self.certificate_number} "
    

