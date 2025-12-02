from rest_framework import serializers
from .models import Project, Category, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description']

class ProjectNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class TaskSerializer(serializers.ModelSerializer):
    # GET fields
    project = ProjectNestedSerializer(read_only=True) # GET nested representation
    categories = CategoryNestedSerializer(many=True, read_only=True) # GET nested representation

    # POST/PUT fields
    # project_id = serializers.IntegerField(write_only=True)
    # categories_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    project_id = serializers.PrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        source='project',
        write_only=True,
        required=False
    )

    categories_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        source='categories',
        write_only=True,
        required=False
    )

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'status', 'due_date',
            'project', 'project_id',
            'categories', 'categories_ids',
            'created_at', 'updated_at',
        ]

    # POST method
    def create(self, validated_data):
        categories = validated_data.pop('categories', [])
        project = validated_data.pop('project', None)

        task = Task.objects.create(project=project, **validated_data) # task object creation
        task.categories.set(categories)

        return task

    # PUT/PATCH method
    def update(self, instance, validated_data):
        categories = validated_data.pop('categories', None)
        project = validated_data.pop('project', None)

        if project is not None:
            instance.project = project

        super().update(instance, validated_data) # Update other fields

        if categories is not None:
            instance.categories.set(categories)

        return instance