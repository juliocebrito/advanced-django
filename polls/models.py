import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.utils import timezone
from advanced_django.utils import BaseModel


class ExampleModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'example'
        verbose_name_plural = 'examples'



class QuestionManager(models.Manager):
    def votes_yes(self, question_text):
        return self.filter(question_text=question_text, choices__choice_text='Y').count()

    def votes_no(self, question_text):
        return self.filter(question_text=question_text, choices__choice_text='N').count()

    def votes_blank(self, question_text):
        return self.filter(question_text=question_text, choices__choice_text='B').count()


class Question(BaseModel):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    count_choices = models.IntegerField(default=0)

    objects = QuestionManager()

    class Meta(BaseModel.Meta):
        verbose_name = 'question'
        verbose_name_plural = 'questions'

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    @property
    def full_info(self):
        "Returns the question's full info"
        return 'id:{}, {}, {}'.format(self.id, self.question_text,
                                      self.pub_date.strftime("%m/%d/%Y, %H:%M:%S"))

class Choice(BaseModel):
    CHOICE_TEXT_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('B', 'Blank'),
        ('1', 'One'),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=1, choices=CHOICE_TEXT_CHOICES) # max_length=1
    votes = models.IntegerField(default=0, editable=False) # editable=False

    class Meta(BaseModel.Meta):
        verbose_name = 'choice'
        verbose_name_plural = 'choices'

    def __str__(self):
        return self.choice_text


    def clean(self, *args, **kwargs):
        if self.choice_text.isdigit():
            raise ValidationError(('Invalid value: %s' % self.choice_text), code='invalid')
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.choice_text:
            self.votes+= 1
        super().save(*args, **kwargs)

    @receiver(post_save, sender=Question)
    def update_count_choices(sender, instance, created, **kwargs):
        if not created:
            # instance.count_choices = instance.choices.count()
            # instance.save()
            obj = Question.objects.filter(id=instance.id)
            obj.update(count_choices=instance.choices.count())