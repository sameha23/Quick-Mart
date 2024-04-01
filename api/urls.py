from django.urls import path


from .views import (
    SeeAdmin, SeeUser, SeeAccount_admin, SeeAccount_handle,
    SeeDiscountList, SeePremiumStudentList, SeeStudentList,
    SeePaymentList, SeeInstructorList, SeeInstructorReviewList,
    SeeCourseIntroList, SeeCourseReviewList, SeeCertificateList,
    SeeCourseDetailsList,
)

from .views import (
    UpdateAdmin, UpdateUser, UpdateAccount_admin, UpdateAccount_handle,
    UpdateDiscount, UpdatePremiumStudent, UpdateStudent, UpdatePayment,
    UpdateInstructor, UpdateInstructorReview, UpdateCourseIntro,
    UpdateCourseReview, UpdateCertificate, UpdateCourseDetails,
)

from .views import (
    CreateAdmin, CreateUser, CreateAccount_admin, CreateAccount_handle,
    CreateDiscount, CreatePremiumStudent, CreateStudent, CreatePayment,
    CreateInstructor, CreateInstructorReview, CreateCourseIntro,
    CreateCourseReview, CreateCertificate, CreateCourseDetails,
)


urlpatterns = [
    path('admin/', SeeAdmin.as_view()),
    path('admin/<int:pk>/', UpdateAdmin.as_view()),
    path('admin/new/', CreateAdmin.as_view()),

    path('user/', SeeUser.as_view()),
    path('user/<int:pk>/', UpdateUser.as_view()),
    path('user/new/', CreateUser.as_view()),

    path('account_admin/', SeeAccount_admin.as_view()),
    path('account_admin/<int:pk>/', UpdateAccount_admin.as_view()),
    path('account_admin/new/', CreateAccount_admin.as_view()),

    path('account_handle/', SeeAccount_handle.as_view()),
    path('account_handle/<int:pk>/', UpdateAccount_handle.as_view()),
    path('account_handle/new/', CreateAccount_handle.as_view()),

    path('discount/', SeeDiscountList.as_view()),
    path('discount/<int:pk>/', UpdateDiscount.as_view()),
    path('discount/new/', CreateDiscount.as_view()),

    path('premium_student/', SeePremiumStudentList.as_view()),
    path('premium_student/<int:pk>/', UpdatePremiumStudent.as_view()),
    path('premium_student/new/', CreatePremiumStudent.as_view()),

    path('student/', SeeStudentList.as_view()),
    path('student/<int:pk>/', UpdateStudent.as_view()),
    path('student/new/', CreateStudent.as_view()),

    path('payment/', SeePaymentList.as_view()),
    path('payment/<int:pk>/', UpdatePayment.as_view()),
    path('payment/new/', CreatePayment.as_view()),

    path('instructor/', SeeInstructorList.as_view()),
    path('instructor/<int:pk>/', UpdateInstructor.as_view()),
    path('instructor/new/', CreateInstructor.as_view()),

    path('instructor_review/', SeeInstructorReviewList.as_view()),
    path('instructor_review/<int:pk>/', UpdateInstructorReview.as_view()),
    path('instructor_review/new/', CreateInstructorReview.as_view()),

    path('course_intro/', SeeCourseIntroList.as_view()),
    path('course_intro/<int:pk>/', UpdateCourseIntro.as_view()),
    path('course_intro/new/', CreateCourseIntro.as_view()),

    path('course_review/', SeeCourseReviewList.as_view()),
    path('course_review/<int:pk>/', UpdateCourseReview.as_view()),
    path('course_review/new/', CreateCourseReview.as_view()),

    path('certificate/', SeeCertificateList.as_view()),
    path('certificate/<int:pk>/', UpdateCertificate.as_view()),
    path('certificate/new/', CreateCertificate.as_view()),

    path('course_details/', SeeCourseDetailsList.as_view()),
    path('course_details/<int:pk>/', UpdateCourseDetails.as_view()),
    path('course_details/new/', CreateCourseDetails.as_view()),
]


