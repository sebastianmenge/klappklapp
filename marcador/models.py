from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = u'tag'
        verbose_name_plural = u'tags'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class PublicBookmarkManager(models.Manager):
    def get_query_set(self):
        qs = super(PublicBookmarkManager, self).get_query_set()
        return qs.filter(is_public=True)


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField(u'title', max_length=255)
    description = models.TextField(u'description', blank=True)
    is_public = models.BooleanField(u'public', default=True)
    date_created = models.DateTimeField(u'date created')
    date_updated = models.DateTimeField(u'date updated')
    owner = models.ForeignKey(User, verbose_name=u'owner', related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()
    public = PublicBookmarkManager()

    class Meta:
        verbose_name = u'bookmark'
        verbose_name_plural = u'bookmarks'
        ordering = ['-date_created']

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Bookmark, self).save(*args, **kwargs)
