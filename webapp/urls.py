from django.urls import path
from . views import *


urlpatterns = [
    path('',home,name='homePage'),
    path('gallery/',gallery,name='galleryPage'),
    path('courses/',courses,name='coursesPage'),
    path('searchcourse/',searchCourse,name='searchcoursePage'),
    path('updatecourse/<course_id>',updateCourse,name='updatecoursePage'),
    path('addcourse/',addCourse,name='addcoursePage'),
    path('deletecourse/<course_id>',deleteCourse,name='deletecoursePage'),
    path('registercourse/<course_id>',registerCourse,name='registercoursePage'),
    path('viewstudents/<course_id>',viewStudents,name='viewstudentsPage'),
]


