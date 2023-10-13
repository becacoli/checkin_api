from django.db import models

class User(models.Model):
  id = models.AutoField(db_column='id', primary_key=True)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  birth_date = models.DateField()
  institution = models.CharField(max_length=255)
  user_roles = ((1, "Student"),(2, "Professor"))
  role = models.IntegerField(choices=user_roles, default=1)
  profile_picture = models.ImageField(null=True, upload_to="./static/img")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
class Classroom(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)
  code = models.CharField(max_length=255)
  period = models.CharField(max_length=255)
  max_students = models.IntegerField()
  workload = models.IntegerField()
  fault_limit = models.IntegerField()
  cover_image = models.ImageField(null=True, upload_to="./static/img")
  professor_id = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

class UserClassroom(models.Model):
  id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE)

class Frequency(models.Model):
  id = models.AutoField(primary_key=True)
  status = models.BooleanField()
  attest = models.FileField(null=True, upload_to="./static/files")
  created_at = models.DateTimeField(auto_now_add=True)
  user_classroom_id = models.ForeignKey(UserClassroom, on_delete=models.CASCADE)