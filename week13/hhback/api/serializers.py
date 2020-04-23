from rest_framework import serializers

from api.models import Company, Vacancy


class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = '__all__'


class VacancyShortSerializer(serializers.ModelSerializer):
  class Meta:
    model = Vacancy
    exclude = ('company',)


class VacancyFullSerializer(serializers.ModelSerializer):
  company = CompanySerializer()

  class Meta:
    model = Vacancy
    fields = '__all__'


class CompanyCreateSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  city = serializers.CharField(max_length=100)
  address = serializers.CharField(required=False)

  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    instance.city = validated_data.get('city', instance.city)
    instance.address = validated_data.get('address', instance.address)
    return instance

  def create(self, validated_data):
    company = Company.objects.create(**validated_data)
    return company
# class CompanySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     city = serializers.CharField()
#     address = serializers.CharField()
#
#     def create(self, validated_data):
#         company = Company()
#         company.name = validated_data.get('name')
#         company.description = validated_data.get('description')
#         company.city = validated_data.get('city')
#         company.address=validated_data.get('address')
#
#         company.save()
#         return company
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.city = validated_data.get('city')
#         instance.address = validated_data.get('address')
#
#         instance.save()
#         return instance
#
# class VacancySerializer(serializers.ModelSerializer):
#     company_id = CompanySerializer(read_only=True)
#     company_id_id = serializers.IntegerField(write_only=True)
#
#     class Meta:
#         model = Vacancy
#         fields = ('id', 'name','description', 'salary', 'company_id','company_id_id')
#
#     def create(self, validated_data):
#         vacancy = Vacancy()
#         vacancy.name = validated_data.get('name')
#         vacancy.description = validated_data.get('description')
#         vacancy.salary = validated_data.get('salary')
#         vacancy.company_id_id = validated_data.get('company_id_id')
#
#         vacancy.save()
#         return vacancy
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.salary = validated_data.get('salary')
#         instance.company_id_id = validated_data.get('company_id_id')
#
#         instance.save()
#         return instance
#
# class CompanySerializerWithVacancies(serializers.ModelSerializer):
#     #vacancies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     #vacancies = serializers.StringRelatedField(many=True, read_only=True)
#     vacancies = VacancySerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Company
#         fields = ('id', 'name', 'description', 'city', 'address', 'vacancies')
