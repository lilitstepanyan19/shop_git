from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_txt = models.TextField('Text')
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'