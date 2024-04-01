from rest_framework import serializers
from projectstart.models import Admin, User, Account_admin, Account_handle, Discount, Premium_student, Student, Payment, Instructor, Instructor_review, Course_intro, Course_review, Certificate, Course_details

class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Account_adminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account_admin
        fields = '__all__'

class Account_handleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account_handle
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class PremiumStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium_student
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class InstructorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor_review
        fields = '__all__'

class CourseIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_intro
        fields = '__all__'

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_review
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class CourseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_details
        fields = '__all__'
