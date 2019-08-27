from django.db import models
from django.utils.text import slugify
# JS ES6, JQuery and React JS

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=120)
    slug = models.SlugField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to="images/")

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_img = models.ImageField(blank=True, null=True, upload_to="images/")
    snippet_1 = models.TextField()
    snippet_2 = models.TextField(blank=True, null=True)
    snippet_3 = models.TextField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True, blank=True, null=True)

    class Meta:
        get_latest_by = 'id'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return "/{}".format(self.slug)
    

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    email = models.EmailField()
    text = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment %s by %s" %(str(self.text)[:20], self.name)
    


class ReplyComment(models.Model):
    comment_reply = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    name_reply = models.CharField(max_length=400)
    text_reply = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Reply by %s to %s" %(self.name_reply, str(self.comment_reply))