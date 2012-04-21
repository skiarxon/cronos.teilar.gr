from django.db import models

class Departments(models.Model):
    urlid = models.IntegerField(unique = True)
    name = models.CharField("Department name", max_length = 200)

class Teachers(models.Model):
    urlid = models.CharField("URL ID", max_length = 30, unique = True)
    name = models.CharField("Teacher name", max_length = 100)
    email = models.EmailField("Teacher's mail", null = True)
    department = models.CharField("Teacher's department", max_length = 100, null = True)

    def __unicode__(self):
        return self.name
