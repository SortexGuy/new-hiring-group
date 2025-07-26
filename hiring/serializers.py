from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    AreasConocimiento,
    Bancos,
    Universidades,
    Profesiones,
    Usuarios,
    Empresas,
    Postulantes,
    Vacantes,
    Postulaciones,
    Contratos,
    ExperienciasLaborales,
    Nominas,
    Recibos,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class AreasConocimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreasConocimiento
        fields = ["id_area_conocimiento", "nombre_area"]

    def create(self, validated_data):
        return AreasConocimiento.objects.create(**validated_data)


class BancosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bancos
        fields = ["id_banco", "nombre_banco"]

    def create(self, validated_data):
        return Bancos.objects.create(**validated_data)


class UniversidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universidades
        fields = ["id_universidad", "nombre_universidad"]

    def create(self, validated_data):
        return Universidades.objects.create(**validated_data)


class ProfesionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesiones
        fields = ["id_profesion", "nombre_profesion", "id_area_conocimiento"]

    def create(self, validated_data):
        return Profesiones.objects.create(**validated_data)


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = [
            "id_usuario",
            "email",
            "password",
            "tipo_usuario",
            "fecha_creacion",
            "estatus",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return Usuarios.objects.create(**validated_data)


class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresas
        fields = [
            "id_empresa",
            "nombre_empresa",
            "rif",
            "sector_industrial",
            "persona_contacto",
            "telefono_contacto",
            "email_contacto",
        ]

    def create(self, validated_data):
        return Empresas.objects.create(**validated_data)


class PostulantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulantes
        fields = [
            "id_postulante",
            "nombres",
            "apellidos",
            "cedula_identidad",
            "fecha_nacimiento",
            "direccion",
            "telefono",
            "id_universidad",
        ]

    def create(self, validated_data):
        return Postulantes.objects.create(**validated_data)


class VacantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacantes
        fields = [
            "id_vacante",
            "id_empresa",
            "cargo_vacante",
            "descripcion_perfil",
            "salario_ofrecido",
            "id_profesion",
            "fecha_publicacion",
            "estatus",
        ]

    def create(self, validated_data):
        return Vacantes.objects.create(**validated_data)


class PostulacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulaciones
        fields = [
            "id_postulacion",
            "id_postulante",
            "id_vacante",
            "fecha_postulacion",
            "estatus",
        ]

    def create(self, validated_data):
        return Postulaciones.objects.create(**validated_data)


class ContratosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratos
        fields = [
            "id_contrato",
            "id_postulacion",
            "fecha_contratacion",
            "tipo_contrato",
            "salario_acordado",
            "tipo_sangre",
            "contacto_emergencia_nombre",
            "contacto_emergencia_telefono",
            "numero_cuenta",
            "id_banco",
            "estatus",
        ]

    def create(self, validated_data):
        return Contratos.objects.create(**validated_data)


class ExperienciasLaboralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciasLaborales
        fields = [
            "id_experiencia",
            "id_postulante",
            "empresa",
            "cargo_ocupado",
            "fecha_inicio",
            "fecha_fin",
            "descripcion",
        ]

    def create(self, validated_data):
        return ExperienciasLaborales.objects.create(**validated_data)


class NominasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nominas
        fields = [
            "id_nomina",
            "id_empresa",
            "mes",
            "anio",
            "fecha_generacion",
            "estatus",
        ]

    def create(self, validated_data):
        return Nominas.objects.create(**validated_data)


class RecibosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recibos
        fields = [
            "id_recibo",
            "id_nomina",
            "id_contrato",
            "salario_base",
            "monto_deduccion_inces",
            "monto_deduccion_ivss",
            "comision_hiring_group",
            "salario_neto_pagado",
            "fecha_pago",
        ]

    def create(self, validated_data):
        return Recibos.objects.create(**validated_data)


# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = [
#             'id',
#             'title',
#             'description',
#             'priority',
#             'completed',
#             'created_at',
#             'updated_at',
#         ]
