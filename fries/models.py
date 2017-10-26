from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'documents/{0}_{1}'.format(instance.user_name, filename)


class User(models.Model):
    user_name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    image = models.FileField(upload_to=user_directory_path)

    def values(self):
    	return {
    		'username': self.user_name,
    		'name': self.name,
    		'email': self.email,
    		'image': self.image
    	}
