from django.db import models


class UrlQueue(models.Model):
    url = models.CharField(verbose_name='URL для парсинга', null=False, blank=False, max_length=256)
    timeshift = models.PositiveIntegerField(verbose_name='Время ожидания перед началом парсинга в секундах', default=0)
    done = models.BooleanField(verbose_name='Флаг выполнения', default=False)

    class Meta:
        verbose_name = 'Очередь парсинга'
        verbose_name_plural = 'Очередь парсинга'

    def __str__(self):
        return '{s.pk}: {s.url}'.format(s=self)


class Results(models.Model):
    url = models.ForeignKey(UrlQueue, on_delete=models.CASCADE)
    executed_at = models.DateTimeField(verbose_name='Дата получения данных страницы', auto_now=True)
    title = models.CharField(verbose_name='Заголовок страницы', max_length=256)
    header = models.CharField(verbose_name='Заголовок H1 на странице', null=True, max_length=256)
    charset = models.CharField(verbose_name='Кодировка страницы', max_length=256)
    fail = models.BooleanField(verbose_name='Была ли ошибка при обработке', default=False)
