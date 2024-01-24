from http.client import HTTPResponse, responses
from secrets import token_bytes
import tokenize
from urllib import response
from rest_framework import viewsets
from centresante.models import *
from Urologie.serializer import *


class PatientViewSet(viewsets.ModelViewSet):

  queryset = Patient.objects.all()
  serializer_class = PatientSerializer
  filter_class = Patient


  def get_serializer_class(self):
    if self.request.method == 'GET':
        return PatientSerializer
    else:
        return self.serializer_class


  def list(self, request, *args, **kwargs):

    queryset = self.filter_queryset(self.get_queryset())

    if 'search' in request.QUERY_PARAMS:
      search = request.QUERY_PARAMS['search']
      q = Q()
      for term in search.split(' '):
          if term  :
              q = q & Q(name__icontains=term)
      q = q | Q(name__icontains=search)
      # On filtre avec l'objet Q
      queryset = queryset.filter(q)

      if search == "":
          queryset = queryset.none()

    queryset = queryset.prefetch_related("Patient")
    queryset = queryset.prefetch_related("Patient__Patient_stock")
    queryset = queryset.prefetch_related("Patient__Patient_stock__warehouse")
    queryset = queryset.prefetch_related("Patient__attribute")

    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    return responses(serializer.data)


  def get_paginated_response(self, data):
    
    for product in data:
      product['Patient']["test"] = 1

    assert self.paginator is not None
    return self.paginator.get_paginated_response(data)


class ProfessionnelsanteViewSet(viewsets.ModelViewSet):

  queryset = Professionnelsante.objects.all()
  serializer_class = ProfessionnelsanteSerializer
  filter_class = Professionnelsante


  def get_serializer_class(self):
    if self.request.method == 'GET':
        return ProfessionnelsanteSerializer
    else:
        return self.serializer_class


  def list(self, request, *args, **kwargs):

    queryset = self.filter_queryset(self.get_queryset())

    if 'search' in request.QUERY_PARAMS:
      search = request.QUERY_PARAMS['search']
      q = Q()
      for term in search.split(' '):
          if term  :
              q = q & Q(name__icontains=term)
      q = q | Q(name__icontains=search)
      # On filtre avec l'objet Q
      queryset = queryset.filter(q)

      if search == "":
          queryset = queryset.none()

    queryset = queryset.prefetch_related("Professionnelsante")
    queryset = queryset.prefetch_related("Professionnelsante__Professionnelsante_stock")
    queryset = queryset.prefetch_related("Professionnelsante__Professionnelsante_stock__warehouse")
    queryset = queryset.prefetch_related("Professionnelsante__attribute")

    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    return response(serializer.data)


  def get_paginated_response(self, data):
    
    for product in data:
      product['Professionnelsante']["test"] = 1

    assert self.paginator is not None
    return self.paginator.get_paginated_response(data)
  


