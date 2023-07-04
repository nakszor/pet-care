from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from rest_framework.pagination import PageNumberPagination
from pets.serializers import PetSerializer
from pets.models import Pet
from groups.models import Group
from traits.models import Trait
from django.forms.models import model_to_dict

class PetView(APIView, PageNumberPagination):
    def post(self, request):
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pet_data = serializer.validated_data
        pet_obj = {
                "name": pet_data["name"],
                "age": pet_data["age"],
                "weight": pet_data["weight"],
                "sex": pet_data["sex"]
            }
        group_name = serializer.validated_data.pop("group")
        group_data, created = Group.objects.get_or_create(**group_name)
        pet = Pet(**pet_obj, group=group_data)
        pet.save()
        
        traits_data = serializer.validated_data.pop("traits")
        traits_obj = []
        print(traits_data)
        for trait in traits_data:
           name = trait["name"] 
           trait_obj, created = Trait.objects.get_or_create(name=name.lower())
           traits_obj.append(trait_obj)
       
        pet.traits.set(traits_obj)
        serializer = PetSerializer(instance=pet)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        trait_name = request.query_params.get('trait', None)
        
        if trait_name is not None:
            pets = Pet.objects.filter(
                traits__name__exact=trait_name
            )
        else:
            pets = Pet.objects.all()

        result_page = self.paginate_queryset(pets, request, view=self)
        serializer = PetSerializer(result_page, many=True)
        serialized_data = list(serializer.data) 
        return self.get_paginated_response(serialized_data)
    
class PetDetailView(APIView):
    def patch(self, request, pet_id: int):
        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response(data={"detail": "Not found."},status=status.HTTP_404_NOT_FOUND)

        serializer = PetSerializer(pet, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        pet_data = serializer.validated_data
        pet_obj = {
            "name": pet_data.get("name", pet.name),
            "age": pet_data.get("age", pet.age),
            "weight": pet_data.get("weight", pet.weight),
            "sex": pet_data.get("sex", pet.sex)
        }
    
        group_name = serializer.validated_data.pop("group", None)
        if group_name:
            group_data, created = Group.objects.get_or_create(**group_name)
            pet.group = group_data

        traits_data = serializer.validated_data.pop("traits", None)
        if traits_data:
            traits_obj = []
            for trait in traits_data:
                name = trait["name"]
                trait_obj, created = Trait.objects.get_or_create(name=name.lower())
                traits_obj.append(trait_obj)
            pet.traits.set(traits_obj)

        pet.__dict__.update(pet_obj)
        pet.save()

        serializer = PetSerializer(instance=pet)
        return Response(serializer.data)

    def delete(self, request, pet_id:int):
        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response(data={"detail": "Not found."} ,status=status.HTTP_404_NOT_FOUND)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get(self, request, pet_id:int):
        try:
            pet = Pet.objects.get(id=pet_id)
        except Pet.DoesNotExist:
            return Response(data={"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PetSerializer(pet)
        return Response(data=serializer, status=status.HTTP_200_OK)