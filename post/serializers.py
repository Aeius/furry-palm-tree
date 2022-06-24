from rest_framework import serializers
from .models import Company as CompanyModel
from .models import JobPost as JobPostModel
from .models import JobPostSkillSet as JobPostSkillSetModel


# 1. Company Serializer (model = Company) 구현**
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = "__all__"

# 2. JobPost Serializer (model = JobPost) 구현**
class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostModel
        fields = ["job_type", "company", "job_description", "salary", ]

# 3. JobPostSkillSet Serializer (model = JobPostSkillSet) 구현**
class JobPostSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSetModel
        fields = "__all__"
        


