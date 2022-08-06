from django.db import models


class Entrance(models.Model):
    """"Класс ДВ подъезда"""

    WALL_MATERIAL = [
        ('Panel', 'Панельный'),
        ('brick', 'Кирпичный'),
        ('wood', 'Деревянный'),
    ]
    address = models.CharField(max_length=100, verbose_name='Адрес')
    floor = models.IntegerField(default=0, verbose_name='Этажность')
    walls = models.CharField(max_length=30, verbose_name='Материал стен', choices=WALL_MATERIAL, default='panel')
    vestibule = models.BooleanField(default=True, verbose_name='Тамбура')
    number_of_vestibules = models.IntegerField(blank=True, verbose_name='Количество тамбуров')
    ceiling = models.FloatField(default=0, verbose_name='Объём потолка подъезда')
    ceiling_vestibule = models.FloatField(default=0, verbose_name='Объём потолка тамбура')
    painted_walls = models.FloatField(default=0, verbose_name='Объём окрашенных стен подъезда')
    painted_walls_vestibule = models.FloatField(default=0, verbose_name='Объём окрашенных стен тамбура')
    whitewash_walls = models.FloatField(blank=True, verbose_name='Объём побелки стен подъезда')
    whitewash_walls_vestibule = models.FloatField(blank=True, verbose_name='Объём побелки стен тамбура')
    number_windows = models.IntegerField(blank=True, verbose_name='Количество окон')
    windows_size = models.FloatField(blank=True, verbose_name='размер окна')
    railing = models.FloatField(blank=True, verbose_name='площадь перил')
    butt_stairs = models.FloatField(blank=True, verbose_name='площадь торца лестницы')
    pipe_coloring = models.FloatField(blank=True, verbose_name='площадь окраски труб')

    def save(self, *args, **kwargs):
        self.duration = ['address']
        super(Entrance, self).save(*args, **kwargs)

    def __str__(self):
        return self.address


    class Meta:
        verbose_name = 'Подъезд'
        verbose_name_plural = 'Подъезды'
