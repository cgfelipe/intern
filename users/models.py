from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class EntityManager(BaseUserManager):
    def create_user(self, name, email, street, neighborhood, city, password=None):
        if not email:
            raise ValueError('Must have an email address')

        entity = self.model(
            name=name,
            email=self.normalize_email(email),
            street=street,
            neighborhood=neighborhood,
            city=city
        )

        entity.set_password(password)
        entity.save(using=self.__db)
        return entity


class Entity(AbstractBaseUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(verbose_name='email address', max_length=255, primary_key=True);
    street = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    member_since = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_school = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'street', 'neighborhood', 'city']

    objects = EntityManager()

    def get_full_name(self):
        return "{0} <{1}>".format(self.name, self.email)

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Company(Entity):
    cnpj = models.CharField(max_length=14, unique=True)


class JobPost(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    base_salary = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class JobOffer(models.Model):
    company = models.ForeignKey(Company)
    post = models.ForeignKey(JobPost)

    def __str__(self):
        return '{0} at {1}'.format(self.post, self.company)


class School(Entity):
    cnpj = models.CharField(max_length=14, unique=True)
    short_name = models.CharField(max_length=30)


class Student(Entity):
    cpf = models.CharField(max_length=11, unique=True)
    school_vinculation = models.ForeignKey(School)
    prentending_jobs = models.ManyToManyField(JobOffer, blank=True)
    date_of_birth = models.DateField()


