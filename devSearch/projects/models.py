from django.db import models
import uuid

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    demo_hyperlink = models.CharField(max_length=1000, null=True, blank=True)
    source_code = models.CharField(max_length=1000, null=True, blank=True)

    tag = models.ManyToManyField('Tag', blank=True)
    voteTotal = models.IntegerField(default=0, null=True, blank=True)
    voteRatio = models.IntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    VOTE_TYPE = (("up", "upVote"), ("down", "downVote"))
    # owner =

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )  # deletes all reviews if Project is deleted / set NULL if reviews should remain untouched

    body = models.TextField(max_length=1000, null=True, blank=True)
    value = models.CharField(max_length=100, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.name
