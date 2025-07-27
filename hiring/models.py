from django.contrib.auth.models import User
from django.db import models


# --- Modelos de Catálogos ---
class AreasConocimiento(models.Model):
    id_area_conocimiento = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "areas_conocimiento"  # Nombre exacto de la tabla en la base de datos
        verbose_name = "Área de Conocimiento"
        verbose_name_plural = "Áreas de Conocimiento"

    def __str__(self):
        return self.nombre_area


class Bancos(models.Model):
    id_banco = models.AutoField(primary_key=True)
    nombre_banco = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "bancos"
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"

    def __str__(self):
        return self.nombre_banco


class Universidades(models.Model):
    id_universidad = models.AutoField(primary_key=True)
    nombre_universidad = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = "universidades"
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"

    def __str__(self):
        return self.nombre_universidad


class Profesiones(models.Model):
    id_profesion = models.AutoField(primary_key=True)
    nombre_profesion = models.CharField(max_length=100)
    # Relación con AreasConocimiento
    id_area_conocimiento = models.ForeignKey(
        AreasConocimiento,
        models.SET_NULL,
        db_column="ID_Area_Conocimiento",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "profesiones"
        verbose_name = "Profesión"
        verbose_name_plural = "Profesiones"

    def __str__(self):
        return self.nombre_profesion


# --- Modelos Principales (Usuarios y Roles) ---
class Usuarios(User):
    class TipoUsuario(models.TextChoices):
        HIRING_GROUP = "HiringGroup", "Hiring Group"
        EMPRESA = "Empresa", "Empresa"
        POSTULANTE = "Postulante", "Postulante"

    class EstatusUsuario(models.TextChoices):
        ACTIVO = "Activo", "Activo"
        INACTIVO = "Inactivo", "Inactivo"

    id_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(
        max_length=15,
        choices=TipoUsuario.choices,
        help_text="Discriminador para identificar el tipo de usuario.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Django maneja automáticamente el DEFAULT CURRENT_TIMESTAMP
    estatus = models.CharField(
        max_length=10, choices=EstatusUsuario.choices, default=EstatusUsuario.ACTIVO
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.Meta.db_table = "usuarios"
    #     verbose_name = "Usuario"
    #     verbose_name_plural = "Usuarios"

    # class Meta:
    #     db_table = "usuarios"
    #     verbose_name = "Usuario"
    #     verbose_name_plural = "Usuarios"

    def __str__(self):
        return f"{self.email} ({self.get_tipo_usuario_display()})"


class Empresas(models.Model):
    # Relación 1-a-1 con Usuarios (ID_Empresa es FK y PK a Usuarios)
    id_empresa = models.OneToOneField(
        Usuarios,
        models.CASCADE,
        primary_key=True,
        db_column="ID_Empresa",
        help_text="Clave primaria y foránea que referencia a Usuarios (relación 1-a-1).",
    )
    nombre_empresa = models.CharField(max_length=150)
    rif = models.CharField(max_length=20, unique=True, blank=True, null=True)
    sector_industrial = models.CharField(max_length=100, blank=True, null=True)
    persona_contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=20, blank=True, null=True)
    email_contacto = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre_empresa


class Postulantes(models.Model):
    # Relación 1-a-1 con Usuarios (ID_Postulante es FK y PK a Usuarios)
    id_postulante = models.OneToOneField(
        Usuarios,
        models.CASCADE,
        primary_key=True,
        db_column="ID_Postulante",
        help_text="Clave primaria y foránea que referencia a Usuarios (relación 1-a-1).",
    )
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula_identidad = models.CharField(
        max_length=20, unique=True, blank=True, null=True
    )
    fecha_nacimiento = models.DateField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    # Relación con Universidades
    id_universidad = models.ForeignKey(
        Universidades,
        models.SET_NULL,
        db_column="ID_Universidad",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "postulantes"
        verbose_name = "Postulante"
        verbose_name_plural = "Postulantes"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# --- Modelos de Procesos de Contratación ---
class Vacantes(models.Model):
    class EstatusVacante(models.TextChoices):
        ACTIVA = "Activa", "Activa"
        INACTIVA = "Inactiva", "Inactiva"
        CERRADA = "Cerrada", "Cerrada"

    id_vacante = models.AutoField(primary_key=True)
    # Relación con Empresas
    id_empresa = models.ForeignKey(Empresas, models.CASCADE, db_column="ID_Empresa")
    cargo_vacante = models.CharField(max_length=150)
    descripcion_perfil = models.TextField()
    salario_ofrecido = models.DecimalField(max_digits=12, decimal_places=2)
    # Relación con Profesiones
    id_profesion = models.ForeignKey(
        Profesiones, models.SET_NULL, db_column="ID_Profesion", blank=True, null=True
    )
    fecha_publicacion = models.DateTimeField(
        auto_now_add=True
    )  # Django maneja automáticamente el DEFAULT CURRENT_TIMESTAMP
    estatus = models.CharField(
        max_length=10, choices=EstatusVacante.choices, default=EstatusVacante.ACTIVA
    )

    class Meta:
        db_table = "vacantes"
        verbose_name = "Vacante"
        verbose_name_plural = "Vacantes"

    def __str__(self):
        return f"{self.cargo_vacante} ({self.id_empresa.nombre_empresa})"


class Postulaciones(models.Model):
    class EstatusPostulacion(models.TextChoices):
        RECIBIDA = "Recibida", "Recibida"
        EN_REVISION = "En Revision", "En Revisión"
        ACEPTADA = "Aceptada", "Aceptada"
        RECHAZADA = "Rechazada", "Rechazada"

    id_postulacion = models.AutoField(primary_key=True)
    # Relación con Postulantes
    id_postulante = models.ForeignKey(
        Postulantes, models.CASCADE, db_column="ID_Postulante"
    )
    # Relación con Vacantes
    id_vacante = models.ForeignKey(Vacantes, models.CASCADE, db_column="ID_Vacante")
    fecha_postulacion = models.DateTimeField(
        auto_now_add=True
    )  # Django maneja automáticamente el DEFAULT CURRENT_TIMESTAMP
    estatus = models.CharField(
        max_length=12,
        choices=EstatusPostulacion.choices,
        default=EstatusPostulacion.RECIBIDA,
    )

    class Meta:
        db_table = "postulaciones"
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"
        unique_together = (
            ("id_postulante", "id_vacante"),
        )  # Un postulante solo puede aplicar una vez a la misma vacante.

    def __str__(self):
        return f"Postulación de {self.id_postulante} a {self.id_vacante.cargo_vacante}"


class Contratos(models.Model):
    class TipoContrato(models.TextChoices):
        UN_MES = "Un mes", "Un mes"
        SEIS_MESES = "Seis meses", "Seis meses"
        UN_ANIO = "Un año", "Un año"
        INDEFINIDO = "Indefinido", "Indefinido"

    class EstatusContrato(models.TextChoices):
        ACTIVO = "Activo", "Activo"
        FINALIZADO = "Finalizado", "Finalizado"

    id_contrato = models.AutoField(primary_key=True)
    # Relación con Postulaciones (UNIQUE KEY en DB, OneToOneField en Django si la relación es 1 a 1 y es clave única)
    # Aquí se modela como OneToOneField porque la DB tiene UNIQUE KEY en ID_Postulacion
    id_postulacion = models.OneToOneField(
        Postulaciones,
        models.DO_NOTHING,
        db_column="ID_Postulacion",
        unique=True,
        help_text="Un contrato se origina de una única postulación aceptada.",
    )  # DO_NOTHING porque la lógica de negocio debe evitar la eliminación en cascada si no hay contrato.
    fecha_contratacion = models.DateField()
    tipo_contrato = models.CharField(max_length=15, choices=TipoContrato.choices)
    salario_acordado = models.DecimalField(max_digits=12, decimal_places=2)
    tipo_sangre = models.CharField(max_length=5, blank=True, null=True)
    contacto_emergencia_nombre = models.CharField(max_length=100, blank=True, null=True)
    contacto_emergencia_telefono = models.CharField(
        max_length=20, blank=True, null=True
    )
    numero_cuenta = models.CharField(max_length=30, blank=True, null=True)
    # Relación con Bancos
    id_banco = models.ForeignKey(
        Bancos, models.SET_NULL, db_column="ID_Banco", blank=True, null=True
    )
    estatus = models.CharField(
        max_length=10, choices=EstatusContrato.choices, default=EstatusContrato.ACTIVO
    )

    class Meta:
        db_table = "contratos"
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

    def __str__(self):
        return (
            f"Contrato {self.id_contrato} ({self.id_postulacion.id_postulante.nombres})"
        )


class ExperienciasLaborales(models.Model):
    id_experiencia = models.AutoField(primary_key=True)
    # Relación con Postulantes
    id_postulante = models.ForeignKey(
        Postulantes, models.CASCADE, db_column="ID_Postulante"
    )
    empresa = models.CharField(max_length=150)
    cargo_ocupado = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(
        blank=True, null=True, help_text="Nulo si es el trabajo actual."
    )
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "experiencias_laborales"
        verbose_name = "Experiencia Laboral"
        verbose_name_plural = "Experiencias Laborales"

    def __str__(self):
        return f"{self.cargo_ocupado} en {self.empresa} ({self.id_postulante.nombres})"


# --- Modelos de Nómina ---


class Nominas(models.Model):
    class EstatusNomina(models.TextChoices):
        GENERADA = "Generada", "Generada"
        PAGADA = "Pagada", "Pagada"

    id_nomina = models.AutoField(primary_key=True)
    # Relación con Empresas
    id_empresa = models.ForeignKey(Empresas, models.CASCADE, db_column="ID_Empresa")
    mes = models.IntegerField()
    anio = models.IntegerField()
    fecha_generacion = models.DateTimeField(
        auto_now_add=True
    )  # Django maneja automáticamente el DEFAULT CURRENT_TIMESTAMP
    estatus = models.CharField(
        max_length=10, choices=EstatusNomina.choices, default=EstatusNomina.GENERADA
    )

    class Meta:
        db_table = "nominas"
        verbose_name = "Nómina"
        verbose_name_plural = "Nóminas"
        unique_together = (
            ("id_empresa", "mes", "anio"),
        )  # Solo puede existir una nómina por empresa para un mes y año específico.

    def __str__(self):
        return f"Nómina de {self.id_empresa.nombre_empresa} - {self.mes}/{self.anio}"


class Recibos(models.Model):
    id_recibo = models.AutoField(primary_key=True)
    # Relación con Nominas
    id_nomina = models.ForeignKey(Nominas, models.CASCADE, db_column="ID_Nomina")
    # Relación con Contratos
    id_contrato = models.ForeignKey(
        Contratos, models.DO_NOTHING, db_column="ID_Contrato"
    )  # Usamos DO_NOTHING porque no tiene ON DELETE en la DB original.
    salario_base = models.DecimalField(max_digits=12, decimal_places=2)
    monto_deduccion_inces = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Calculado como el 0.5% del salario."
    )
    monto_deduccion_ivss = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Calculado como el 1% del salario."
    )
    comision_hiring_group = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Calculado como el 2% del salario."
    )
    salario_neto_pagado = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pago = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "recibos"
        verbose_name = "Recibo"
        verbose_name_plural = "Recibos"

    def __str__(self):
        return f"Recibo {self.id_recibo} para {self.id_contrato.id_postulacion.id_postulante.nombres}"
