from calendar import month
from django.db import models
# Create your models here.

from datetime import datetime



class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.CharField(max_length= 20,default="",blank=True,null=True)
    password = models.CharField(max_length= 10,default="",blank=True,null=True)
    name = models.CharField(max_length= 50,blank=True,null=True,default="")    
    email = models.CharField(max_length= 30,blank=True,null=True,default="")
    city = models.CharField(max_length= 50,blank=True,null=True,default="")
    area = models.CharField(max_length= 50,blank=True,null=True,default="")
    postcode = models.CharField(max_length= 10,blank=True,null=True,default="")
    streetaddress = models.CharField(max_length= 200,blank=True,null=True,default="")
    houseno = models.CharField(max_length= 10,blank=True,null=True,default="")

    nid = models.CharField(max_length= 50,blank=True,null=True,default="")
    permanent_address = models.CharField(max_length=300,blank=True,null=True,default="")
    
    image = models.ImageField(upload_to= "user_img",blank=True,null=True,default="")
    
    duerentstatus = models.BooleanField(blank=True,null=True,default=False)
    dueorderstatus = models.BooleanField(blank=True,null=True,default=False)
    
    totaladd = models.CharField(max_length= 20,default="",blank=True,null=True)
    totalrenders = models.CharField(max_length= 20,default="",blank=True,null=True)
    totalorders = models.CharField(max_length= 20,default="",blank=True,null=True)
    


class Admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_role = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, default="", blank=True, null=True)
    account_creationTime = models.CharField(max_length=255, default="", blank=True, null=True)
    account_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)

class Account_admin(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_admin_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)

class Account_handle(models.Model):
    id = models.BigAutoField(primary_key=True)
    account_ID = models.CharField(max_length=255, default="", blank=True, null=True)
    account_admin_id = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_check = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_issue = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_info = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_Time = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_Location = models.CharField(max_length=255, default="", blank=True, null=True)

class Discount(models.Model):
    id = models.BigAutoField(primary_key=True)
    discount_id = models.CharField(max_length=255, default="", blank=True, null=True)
    coupon_code = models.CharField(max_length=255, default="", blank=True, null=True)
    premium_student_account = models.CharField(max_length=255, default="", blank=True, null=True)


class Premium_student(models.Model):
    id = models.BigAutoField(primary_key=True)
    premium_student_id = models.CharField(max_length=255, default="", blank=True, null=True)
    student_Id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)
    number_of_courseTaken = models.CharField(max_length=255, default="", blank=True, null=True)

class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    student_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)
    user_image = models.CharField(max_length=255, default="", blank=True, null=True)
    user_phone = models.CharField(max_length=255, default="", blank=True, null=True)
    user_address = models.CharField(max_length=255, default="", blank=True, null=True)
    user_role = models.CharField(max_length=255, default="", blank=True, null=True)
    course_taken = models.CharField(max_length=255, default="", blank=True, null=True)
    course_doing = models.CharField(max_length=255, default="", blank=True, null=True)
    course_routine = models.CharField(max_length=255, default="", blank=True, null=True)
    result = models.CharField(max_length=255, default="", blank=True, null=True)
    course_payment = models.CharField(max_length=255, default="", blank=True, null=True)
    account_creationTime = models.CharField(max_length=255, default="", blank=True, null=True)
    account_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)

class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    payment_Id = models.CharField(max_length=255, default="", blank=True, null=True)
    account_admin_id = models.CharField(max_length=255, default="", blank=True, null=True)
    course_id = models.CharField(max_length=255, default="", blank=True, null=True)
    course_name = models.CharField(max_length=255, default="", blank=True, null=True)
    student_Id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_method = models.CharField(max_length=255, default="", blank=True, null=True)
    amount = models.CharField(max_length=255, default="", blank=True, null=True)
    status = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_Time = models.CharField(max_length=255, default="", blank=True, null=True)
    payment_Location = models.CharField(max_length=255, default="", blank=True, null=True)

class Instructor(models.Model):
    id = models.BigAutoField(primary_key=True)
    instructor_Id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_id = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)
    user_image = models.CharField(max_length=255, default="", blank=True, null=True)
    user_role = models.CharField(max_length=255, default="", blank=True, null=True)
    course_taken = models.CharField(max_length=255, default="", blank=True, null=True)
    class_routine = models.CharField(max_length=255, default="", blank=True, null=True)
    instructor_review = models.CharField(max_length=255, default="", blank=True, null=True)
    rating = models.CharField(max_length=255, default="", blank=True, null=True)
    salary = models.CharField(max_length=255, default="", blank=True, null=True)
    socialmedia_account = models.CharField(max_length=255, default="", blank=True, null=True)
    account_creationTime = models.CharField(max_length=255, default="", blank=True, null=True)
    account_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)

class Instructor_review(models.Model):
    id = models.BigAutoField(primary_key=True)
    instructor_name = models.CharField(max_length=255, default="", blank=True, null=True)
    course_name = models.CharField(max_length=255, default="", blank=True, null=True)
    reviewer_user_id = models.CharField(max_length=255, default="", blank=True, null=True)
    reviewer_name = models.CharField(max_length=255, default="", blank=True, null=True)
    rating = models.CharField(max_length=255, default="", blank=True, null=True)
    description_review = models.CharField(max_length=255, default="", blank=True, null=True)
    is_varified = models.CharField(max_length=255, default="", blank=True, null=True)
    helpful_course_instructor = models.CharField(max_length=255, default="", blank=True, null=True)
    not_helpful_course_instructor = models.CharField(max_length=255, default="", blank=True, null=True)
    reviewer_location = models.CharField(max_length=255, default="", blank=True, null=True)
    instructor_review_creationTime = models.CharField(max_length=255, default="", blank=True, null=True)
    instructor_review_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)
    updated_at = models.CharField(max_length=255, default="", blank=True, null=True)

class Course_intro(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.CharField(max_length=255, default="", blank=True, null=True)
    course_name = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name = models.CharField(max_length=255, default="", blank=True, null=True)
    course_summary = models.CharField(max_length=255, default="", blank=True, null=True)
    course_video = models.CharField(max_length=255, default="", blank=True, null=True)
    description = models.CharField(max_length=255, default="", blank=True, null=True)
    course_catagory = models.CharField(max_length=255, default="", blank=True, null=True)
    certification = models.CharField(max_length=255, default="", blank=True, null=True)
    price = models.CharField(max_length=255, default="", blank=True, null=True)
    discount_catagory = models.CharField(max_length=255, default="", blank=True, null=True)
    discount_amount = models.CharField(max_length=255, default="", blank=True, null=True)
    course_review = models.CharField(max_length=255, default="", blank=True, null=True)
    rating = models.CharField(max_length=255, default="", blank=True, null=True)
    course_creationTime = models.CharField(max_length=255, default="", blank=True, null=True)
    course_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)
    updates_at = models.CharField(max_length=255, default="", blank=True, null=True)

class Course_review(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=255, default="", blank=True, null=True)
    reviewer_user_id = models.CharField(max_length=255, default="", blank=True, null=True)
    reviewer_name = models.CharField(max_length=255, default="", blank=True, null=True)
    rating = models.CharField(max_length=255, default="", blank=True, null=True)
    description_review = models.CharField(max_length=255, default="", blank=True, null=True)
    is_varified = models.CharField(max_length=255, default="", blank=True, null=True)
    helpful_course_course = models.CharField(max_length=255, default="", blank=True, null=True)
    not_helpful_course_course = models.CharField(max_length=255, default="", blank=True, null=True)
    reviewer_location = models.CharField(max_length=255, default="", blank=True, null=True)
    course_review_creationTime = models.CharField(max_length=255, default="", blank=True, null=True)
    course_review_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)
    updated_at = models.CharField(max_length=255, default="", blank=True, null=True)

class Certificate(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.CharField(max_length=255, default="", blank=True, null=True)
    course_name = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name_instructor = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name_student = models.CharField(max_length=255, default="", blank=True, null=True)
    grade = models.CharField(max_length=255, default="", blank=True, null=True)
    sign = models.CharField(max_length=255, default="", blank=True, null=True)
    course_startTime = models.CharField(max_length=255, default="", blank=True, null=True)
    course_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)
    updated_at = models.CharField(max_length=255, default="", blank=True, null=True)

class Course_details(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.CharField(max_length=255, default="", blank=True, null=True)
    course_name = models.CharField(max_length=255, default="", blank=True, null=True)
    user_name_instructor = models.CharField(max_length=255, default="", blank=True, null=True)
    course_lecturevideo = models.CharField(max_length=255, default="", blank=True, null=True)
    course_lecturedescription = models.CharField(max_length=255, default="", blank=True, null=True)
    course_catagory = models.CharField(max_length=255, default="", blank=True, null=True)
    course_creationTime = models.CharField(max_length=255, default="", blank=True, null=True)
    course_creationLocation = models.CharField(max_length=255, default="", blank=True, null=True)
    updated_at = models.CharField(max_length=255, default="", blank=True, null=True)

    
    def register(self):
        self.save()

