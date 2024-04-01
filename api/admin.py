from ast import Assert, Assign
from django.contrib import admin


from .models import  Admin,User,Account_admin,Account_handle,Discount,Premium_student,Student,Payment,Instructor,Instructor_review,Course_intro,Course_review,Certificate,Course_details

# Register your models here
admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Account_admin)
admin.site.register(Account_handle)
admin.site.register(Discount)
admin.site.register(Premium_student)
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Instructor)
admin.site.register(Instructor_review)
admin.site.register(Course_intro)
admin.site.register(Course_review)
admin.site.register(Certificate)
admin.site.register(Course_details)

