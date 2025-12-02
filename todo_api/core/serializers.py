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
    project_id = serializers.IntegerField(write_only=True)
    categories_ids = serializers.ListField(child=serializers.IntegerField(), write_only=True)

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
        categories_ids = validated_data.pop('categories_ids', [])
        project_id = validated_data.pop('project_id')

        task = Task.objects.create(project_id=project_id, **validated_data) # task object creation
        task.categories.set(categories_ids)

        return task

    # PUT/PATCH method
    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            instance.project_id = validated_data.pop('project_id')

        if 'categories_ids' in validated_data:
            instance.categories.set(validated_data.pop('categories_ids'))

        return super().update(instance, validated_data) # Update other fields