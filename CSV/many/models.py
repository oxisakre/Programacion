from django.db import models
class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    LEARNER = 1
    IA = 1000
    GSI = 2000
    INSTRUCTOR = 5000
    ADMIN = 10000

    MEMBER_CHOICES = (
        (LEARNER, 'Learner')
        (IA, 'Instructional Assistant')
        (GSI, 'Grad Student Instructor')
        (INSTRUCTOR, 'Instructor')
        (ADMIN, 'Administrator')
    )

    role = models.IntegerField(
        choices = MEMBER_CHOICES
        default= LEARNER,
    )

    def __str__(self):
        return 'Person '+ str(self.person.id) + " <--> Course " + str(self.course.id)