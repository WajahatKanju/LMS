from rest_framework import serializers
from Class.models import Class
from school.models import Schools, SchoolClasses, ClassSubject
from student.models import Student, StudentClass, Position


class SchoolsSerializer(serializers.Serializer):
    model = Schools
    fields = '__all__'


class ClassSerializer(serializers.Serializer):
    model = Class
    fields = '__all__'


class SchoolClassesSerializer(serializers.Serializer):
    model = SchoolClasses
    fields = '__all__'


class ClassSubclassSerializer(serializers.Serializer):
    model = ClassSubject
    fields = '__all__'


class StudentSerializer(serializers.Serializer):
    model = Student
    fields = '__all__'


class PositionSerializer(serializers.Serializer):
    model = Position
    fields = '__all__'


class StudentClassSerializer(serializers.Serializer):
    model = StudentClass
    fields = '__all__'
