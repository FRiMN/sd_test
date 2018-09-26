import re
from multiprocessing.pool import Pool, ThreadPool
from time import sleep

import requests
from django.core.management import BaseCommand

from sibdev.models import UrlQueue, Results


class Command(BaseCommand):
    def handle(self, *args, **options):
        pool = None
        try:
            while True:
                pool = ThreadPool(4)
                urls_queue = UrlQueue.objects.filter(done=False)
                pool.map(self.parsing, urls_queue)
                sleep(1)
                pool.close()
                pool.join()
        finally:
            if pool:
                pool.close()
                pool.join()

    @staticmethod
    def parsing(task):
        print('parse', task.url, task.id, task.timeshift)
        task.done = True
        task.save()

        if task.timeshift:
            sleep(task.timeshift)

        result = Results(url=task)
        try:
            resp = requests.get(task.url)
            if resp.ok:
                charset = resp.encoding
                title = re.search('(?<=<title>).+?(?=</title>)', resp.text, re.DOTALL).group().strip()
                header_re = re.search('(?<=<h1>).+?(?=</h1>)', resp.text, re.DOTALL)
                if header_re:
                    header = header_re.group().strip()
                else:
                    header = None

                result.charset = charset
                result.title = title
                result.header = header
            else:
                raise Exception()
        except Exception:
            result.fail = True

        result.save()
