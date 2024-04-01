class Admin(models.Model):
    ID = models.BigAutoField(primary_key=True)
    admin_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)

Class User(models.Model):
     ID = models.BigAutoField(primary_key=True)
     user_id = models.CharField(max_length=255)
     user_role = models.CharField(max_length=255)
     user_name = models.CharField(max_length=255)
     user_email = models.EmailField(unique=True)
     password = models.CharField(max_length=255)
     account_creationTime = models.CharField(max_length=255)
     account_creationLocation = models.CharField(max_length=255)

Class Account_admin(models.Model):
      ID = models.BigAutoField(primary_key=True)
      account_admin_id = models.CharField(max_length=255)
      user_id = models.CharField(max_length=255)
      user_name = models.CharField(max_length=255)

Class Account_handle(models.Model):
       ID = models.BigAutoField(primary_key=True)
       account_ID = models.CharField(max_length=255)
       account_admin_id = models.CharField(max_length=255)
       payment_check = models.CharField(max_length=255)
       payment_issue = models.CharField(max_length=255)
       payment_info = models.CharField(max_length=255)
       payment_Time = models.CharField(max_length=255)
       payment_Location = models.CharField(max_length=255)

Class Discount(models.Model):
      ID = models.BigAutoField(primary_key=True)
      discount_id = models.CharField(max_length=255)
      coupon_code = models.CharField(max_length=255)
      premium_student_account = models.CharField(max_length=255)
       
Class Premium_student(models.Model):      
       ID = models.BigAutoField(primary_key=True)
       premium_student_id = models.CharField(max_length=255)
       student_Id= models.CharField(max_length=255)
       user_name = models.CharField(max_length=255)
       number_of_courseTaken= models.CharField(max_length=255)
       
Class Student(models.Model):
     ID = models.BigAutoField(primary_key=True)
     student_id = models.CharField(max_length=255)
     user_id = models.CharField(max_length=255)
     user_name = models.CharField(max_length=255)
     user_image = models.CharField(max_length=255)
     user_phone = models.CharField(max_length=255)
     user_address= models.CharField(max_length=255)
     user_role= models.CharField(max_length=255)
     course_taken = models.CharField(max_length=255)
     course_doing = models.CharField(max_length=255)
     course_routine = models.CharField(max_length=255)
     result= models.CharField(max_length=255)
     course_payment = models.CharField(max_length=255)
     account_creationTime = models.CharField(max_length=255)
     account_creationLocation = models.CharField(max_length=255)


Class Payment(models.Model):   
      ID = models.BigAutoField(primary_key=True)
      payment_Id = models.CharField(max_length=255)
      account_admin_id = models.CharField(max_length=255)
      course_id = models.CharField(max_length=255)
      course_name = models.CharField(max_length=255)
      student_Id = models.CharField(max_length=255)
      user_name = models.CharField(max_length=255)
      payment_method = models.CharField(max_length=255)
      amount = models.CharField(max_length=255)
      status = models.CharField(max_length=255)
      payment_Time = models.CharField(max_length=255)
      payment_Location = models.CharField(max_length=255)


Class Instructor(models.Model):
     ID = models.BigAutoField(primary_key=True)
     instructor_Id = models.CharField(max_length=255)
     user_id = models.CharField(max_length=255)
     user_name = models.CharField(max_length=255)
     user_image = models.CharField(max_length=255)
     user_role = models.CharField(max_length=255)
     course_taken= models.CharField(max_length=255)
     class_routine= models.CharField(max_length=255)
     instructor_review = models.CharField(max_length=255)
     rating= models.CharField(max_length=255)
     salary = models.CharField(max_length=255)
     socialmedia_account= models.CharField(max_length=255)
     account_creationTime = models.CharField(max_length=255)
     account_creationLocation = models.CharField(max_length=255)
      
      
Class Instructor_review(models.Model):
       ID = models.BigAutoField(primary_key=True)
       instructor_name = models.CharField(max_length=255)
       course_name = models.CharField(max_length=255)
       reviewer_user_id= models.CharField(max_length=255)
       reviewer_name= models.CharField(max_length=255)
       rating = models.CharField(max_length=255)
       description_review = models.CharField(max_length=255)
       is_varified = models.CharField(max_length=255)
       helpful_course_instructor = models.CharField(max_length=255)
       not_helpful_course_instructor = models.CharField(max_length=255)
       reviewer_location = models.CharField(max_length=255)
       instructor_review_creationTime = models.CharField(max_length=255)
       instructor_review_creationLocation = models.CharField(max_length=255)
       updated_at = models.CharField(max_length=255)


Class Course_intro(models.Model):
       ID = models.BigAutoField(primary_key=True)
       course_id = models.CharField(max_length=255)
       course_name = models.CharField(max_length=255)
       user_name = models.CharField(max_length=255)
       course_summary = models.CharField(max_length=255)
       course_video = models.CharField(max_length=255)
       description = models.CharField(max_length=255)
       course_catagory = models.CharField(max_length=255)
       certification = models.CharField(max_length=255)
       price = models.CharField(max_length=255)
       discount_catagory = models.CharField(max_length=255)
       discount_amount = models.CharField(max_length=255)
       course_review = models.CharField(max_length=255)
       rating = models.CharField(max_length=255)
       course_creationTime = models.CharField(max_length=255)
       course_creationLocation = models.CharField(max_length=255)
       updates_at = models.CharField(max_length=255)
       

Class Course_review(models.Model):
       ID = models.BigAutoField(primary_key=True)
       course_name = models.CharField(max_length=255)
       reviewer_user_id= models.CharField(max_length=255)
       reviewer_name= models.CharField(max_length=255)
       rating = models.CharField(max_length=255)
       description_review = models.CharField(max_length=255)
       is_varified = models.CharField(max_length=255)
       helpful_course_course = models.CharField(max_length=255)
       not_helpful_course_course = models.CharField(max_length=255)
       reviewer_location = models.CharField(max_length=255)
       course_review_creationTime = models.CharField(max_length=255)
       course_review_creationLocation = models.CharField(max_length=255)
       updated_at = models.CharField(max_length=255)



Class Certificate(models.Model):
       ID = models.BigAutoField(primary_key=True)
       course_id = models.CharField(max_length=255)
       course_name = models.CharField(max_length=255)
       user_name(instructor)= models.CharField(max_length=255)
       user_name(student)= models.CharField(max_length=255)
       grade = models.CharField(max_length=255)
       sign = models.CharField(max_length=255)
       course_startTime = models.CharField(max_length=255)
       course_creationLocation = models.CharField(max_length=255)
       updated_at = models.CharField(max_length=255)


Class Course_details(models.Model):
       ID = models.BigAutoField(primary_key=True)
       course_id = models.CharField(max_length=255)
       course_name = models.CharField(max_length=255)
       user_name(instructor)= models.CharField(max_length=255)
       course_lecturevideo= models.CharField(max_length=255)
       course_lecturedescription = models.CharField(max_length=255)
       course_catagory = models.CharField(max_length=255)
       course_creationTime = models.CharField(max_length=255)
       course_creationLocation = models.CharField(max_length=255)
       updated_at = models.CharField(max_length=255)

       


      