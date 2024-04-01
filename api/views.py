from django.shortcuts import render
from rest_framework import generics

import requests 
from projectstart.models import Admin,User,Account_admin,Account_handle,Discount, Premium_student, Student, Payment, Instructor, Instructor_review, Course_intro, Course_review, Certificate, Course_details

from .serializers import AdminSerializers, UserSerializers, Account_adminSerializers, Account_handleSerializers, DiscountSerializer, PremiumStudentSerializer, StudentSerializer, PaymentSerializer, InstructorSerializer, InstructorReviewSerializer, CourseIntroSerializer, CourseReviewSerializer, CertificateSerializer, CourseDetailsSerializer

#Admin
class SeeAdmin(generics.ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializers

class UpdateAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AdminSerializers

class CreateAdmin(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')[:1] 
    serializer_class = AdminSerializers


#User
class SeeUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-id')[:1] 
    serializer_class = UserSerializers


#Account_admin
class SeeAccount_admin(generics.ListAPIView):
    queryset = Account_admin.objects.all()
    serializer_class = Account_adminSerializers

class UpdateAccount_admin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account_admin.objects.all()
    serializer_class = Account_adminSerializers

class CreateAccount_admin(generics.ListCreateAPIView):
    queryset = Account_admin.objects.all().order_by('-id')[:1] 
    serializer_class = Account_adminSerializers



#Account_handle
class SeeAccount_handle(generics.ListAPIView):
    queryset = Account_handle.objects.all()
    serializer_class = Account_handleSerializers

class UpdateAccount_handle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account_handle.objects.all()
    serializer_class = Account_handleSerializers

class CreateAccount_handle(generics.ListCreateAPIView):
    queryset = Account_handle.objects.all().order_by('-id')[:1] 
    serializer_class = Account_handleSerializers


# Discount
class SeeDiscountList(generics.ListAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class UpdateDiscount(generics.UpdateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class CreateDiscount(generics.CreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


# Premium_student
class SeePremiumStudentList(generics.ListAPIView):
    queryset = Premium_student.objects.all()
    serializer_class = PremiumStudentSerializer

class UpdatePremiumStudent(generics.UpdateAPIView):
    queryset = Premium_student.objects.all()
    serializer_class = PremiumStudentSerializer

class CreatePremiumStudent(generics.CreateAPIView):
    queryset = Premium_student.objects.all()
    serializer_class = PremiumStudentSerializer

# Student
class SeeStudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudent(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CreateStudent(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Payment
class SeePaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class UpdatePayment(generics.UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class CreatePayment(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

# Instructor
class SeeInstructorList(generics.ListAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class UpdateInstructor(generics.UpdateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class CreateInstructor(generics.CreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# Instructor_review
class SeeInstructorReviewList(generics.ListAPIView):
    queryset = Instructor_review.objects.all()
    serializer_class = InstructorReviewSerializer

class UpdateInstructorReview(generics.UpdateAPIView):
    queryset = Instructor_review.objects.all()
    serializer_class = InstructorReviewSerializer

class CreateInstructorReview(generics.CreateAPIView):
    queryset = Instructor_review.objects.all()
    serializer_class = InstructorReviewSerializer

# Course_intro
class SeeCourseIntroList(generics.ListAPIView):
    queryset = Course_intro.objects.all()
    serializer_class = CourseIntroSerializer

class UpdateCourseIntro(generics.UpdateAPIView):
    queryset = Course_intro.objects.all()
    serializer_class = CourseIntroSerializer

class CreateCourseIntro(generics.CreateAPIView):
    queryset = Course_intro.objects.all()
    serializer_class = CourseIntroSerializer

# Course_review
class SeeCourseReviewList(generics.ListAPIView):
    queryset = Course_review.objects.all()
    serializer_class = CourseReviewSerializer

class UpdateCourseReview(generics.UpdateAPIView):
    queryset = Course_review.objects.all()
    serializer_class = CourseReviewSerializer

class CreateCourseReview(generics.CreateAPIView):
    queryset = Course_review.objects.all()
    serializer_class = CourseReviewSerializer

# Certificate
class SeeCertificateList(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class UpdateCertificate(generics.UpdateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CreateCertificate(generics.CreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

# Course_details
class SeeCourseDetailsList(generics.ListAPIView):
    queryset = Course_details.objects.all()
    serializer_class = CourseDetailsSerializer

class UpdateCourseDetails(generics.UpdateAPIView):
    queryset = Course_details.objects.all()
    serializer_class = CourseDetailsSerializer

class CreateCourseDetails(generics.CreateAPIView):
    queryset = Course_details.objects.all()
    serializer_class = CourseDetailsSerializer
