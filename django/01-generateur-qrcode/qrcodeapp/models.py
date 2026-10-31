from django.db import models
from django.core.files import File
import qrcode
from io import BytesIO
from PIL import Image, ImageDraw

# Create your models here.

class QR_code(models.Model):
    data = models.CharField(max_length=250)
    qr_code = models.ImageField(upload_to='qr_code', null=True, blank=True )
    
    def save(self, *args, **kwargs):
        # Vérifier si l'objet existe déjà pour éviter la regénération inutile
        if not self.pk:
            # Générer le code QR
            qr_image = qrcode.make(self.data)
            canvas = Image.new('RGB', (qr_image.pixel_size, qr_image.pixel_size), 'white')
            draw = ImageDraw.Draw(canvas)
            canvas.paste(qr_image)
            file_name = f'qr_code-{self.data.replace("/", "_")}.png'
            buffer = BytesIO()
            canvas.save(buffer, 'PNG')
            self.qr_code.save(file_name, File(buffer), save=False)
            canvas.close()
        return super().save(*args, **kwargs)
    
