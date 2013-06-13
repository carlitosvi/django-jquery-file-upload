from django.db import models
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class Picture(models.Model):

    user = models.ForeignKey(User)
    file = models.ImageField(upload_to="pictures")
    slug = models.SlugField(max_length=50, blank=True)

    def __unicode__(self):
        return '%s' % (self.file)

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        self.slug = self.file.name
        super(Picture, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(Picture, self).delete(*args, **kwargs)


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['file', ]

    def UploadImage(request):
        """Upload Images"""
        if request.method == 'POST':
            form = PictureForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return HttpResponseRedirect(".")
        else:
            form = PictureForm()

        return render(request, 'picture_form.html', {
        'form': form,
        })
