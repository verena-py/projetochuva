# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actionannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    annotationid = models.ForeignKey('Annotations', models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionAnnotations'


class Actionby(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    affiliationid = models.ForeignKey('Affiliations', models.DO_NOTHING, db_column='AffiliationID')  # Field name made lowercase.
    isactionlead = models.TextField(db_column='IsActionLead')  # Field name made lowercase. This field type is a guess.
    roledescription = models.CharField(max_length=120, db_column='RoleDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionBy'


class Actiondirectives(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    directiveid = models.ForeignKey('Directives', models.DO_NOTHING, db_column='DirectiveID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionDirectives'


class Actionextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey('Actions', models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    propertyid = models.ForeignKey('Extensionproperties', models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(max_length=120, db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActionExtensionPropertyValues'


class Actions(models.Model):
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    actiontypecv = models.ForeignKey('CvActiontype', models.DO_NOTHING, db_column='ActionTypeCV')  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    begindatetimeutcoffset = models.IntegerField(db_column='BeginDateTimeUTCOffset')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetimeutcoffset = models.IntegerField(db_column='EndDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    actiondescription = models.CharField(max_length=120, db_column='ActionDescription', blank=True, null=True)  # Field name made lowercase.
    actionfilelink = models.CharField(max_length=120, db_column='ActionFileLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actions'


class Affiliations(models.Model):
    affiliationid = models.AutoField(db_column='AffiliationID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey('People', models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.
    organizationid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.
    isprimaryorganizationcontact = models.TextField(db_column='IsPrimaryOrganizationContact', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    affiliationstartdate = models.DateField(db_column='AffiliationStartDate')  # Field name made lowercase.
    affiliationenddate = models.DateField(db_column='AffiliationEndDate', blank=True, null=True)  # Field name made lowercase.
    primaryphone = models.CharField(max_length=120, db_column='PrimaryPhone', blank=True, null=True)  # Field name made lowercase.
    primaryemail = models.CharField(max_length=120, db_column='PrimaryEmail')  # Field name made lowercase.
    primaryaddress = models.CharField(max_length=120, db_column='PrimaryAddress', blank=True, null=True)  # Field name made lowercase.
    personlink = models.CharField(max_length=120, db_column='PersonLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Affiliations'


class Annotations(models.Model):
    annotationid = models.AutoField(db_column='AnnotationID', primary_key=True)  # Field name made lowercase.
    annotationtypecv = models.ForeignKey('CvAnnotationtype', models.DO_NOTHING, db_column='AnnotationTypeCV')  # Field name made lowercase.
    annotationcode = models.CharField(max_length=120, db_column='AnnotationCode', blank=True, null=True)  # Field name made lowercase.
    annotationtext = models.CharField(max_length=120, db_column='AnnotationText')  # Field name made lowercase.
    annotationdatetime = models.DateTimeField(db_column='AnnotationDateTime', blank=True, null=True)  # Field name made lowercase.
    annotationutcoffset = models.IntegerField(db_column='AnnotationUTCOffset', blank=True, null=True)  # Field name made lowercase.
    annotationlink = models.CharField(max_length=120, db_column='AnnotationLink', blank=True, null=True)  # Field name made lowercase.
    annotatorid = models.ForeignKey('People', models.DO_NOTHING, db_column='AnnotatorID', blank=True, null=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Annotations'


class Authorlists(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.
    personid = models.ForeignKey('People', models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.
    authororder = models.IntegerField(db_column='AuthorOrder')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AuthorLists'


class CvActiontype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_ActionType'


class CvAggregationstatistic(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_AggregationStatistic'


class CvAnnotationtype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_AnnotationType'


class CvCensorcode(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_CensorCode'


class CvDataqualitytype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_DataQualityType'


class CvDatasettype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_DatasetType'


class CvDirectivetype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_DirectiveType'


class CvElevationdatum(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_ElevationDatum'


class CvEquipmenttype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_EquipmentType'


class CvMedium(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_Medium'


class CvMethodtype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_MethodType'


class CvOrganizationtype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_OrganizationType'


class CvPropertydatatype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_PropertyDataType'


class CvQualitycode(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_QualityCode'


class CvRelationshiptype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_RelationshipType'


class CvResulttype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_ResultType'


class CvSamplingfeaturegeotype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_SamplingFeatureGeoType'


class CvSamplingfeaturetype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_SamplingFeatureType'


class CvSitetype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_SiteType'


class CvSpatialoffsettype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_SpatialOffsetType'


class CvSpeciation(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_Speciation'


class CvSpecimentype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_SpecimenType'


class CvStatus(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_Status'


class CvTaxonomicclassifiertype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_TaxonomicClassifierType'


class CvUnitstype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_UnitsType'


class CvVariablename(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_VariableName'


class CvVariabletype(models.Model):
    term = models.CharField(max_length=120, db_column='Term')  # Field name made lowercase.
    name = models.CharField(max_length=120, db_column='Name', primary_key=True)  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(max_length=120, db_column='Category', blank=True, null=True)  # Field name made lowercase.
    sourcevocabularyuri = models.CharField(max_length=120, db_column='SourceVocabularyURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CV_VariableType'


class Calibrationactions(models.Model):
    actionid = models.OneToOneField(Actions, models.DO_NOTHING, db_column='ActionID', primary_key=True)  # Field name made lowercase.
    calibrationcheckvalue = models.TextField(db_column='CalibrationCheckValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instrumentoutputvariableid = models.ForeignKey('Instrumentoutputvariables', models.DO_NOTHING, db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    calibrationequation = models.CharField(max_length=120, db_column='CalibrationEquation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalibrationActions'


class Calibrationreferenceequipment(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Calibrationactions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey('Equipment', models.DO_NOTHING, db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalibrationReferenceEquipment'


class Calibrationstandards(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Calibrationactions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials', models.DO_NOTHING, db_column='ReferenceMaterialID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CalibrationStandards'


class Categoricalresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Categoricalresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoricalResultValueAnnotations'


class Categoricalresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Categoricalresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.CharField(max_length=120, db_column='DataValue')  # Field name made lowercase.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoricalResultValues'


class Categoricalresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.IntegerField(db_column='XLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    ylocation = models.TextField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.IntegerField(db_column='YLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    zlocation = models.TextField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.IntegerField(db_column='ZLocationUnitsID', blank=True, null=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoricalResults'


class Citationextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.
    propertyid = models.ForeignKey('Extensionproperties', models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(max_length=120, db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CitationExtensionPropertyValues'


class Citationexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey('Citations', models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey('Externalidentifiersystems', models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    citationexternalidentifier = models.CharField(max_length=120, db_column='CitationExternalIdentifier')  # Field name made lowercase.
    citationexternalidentifieruri = models.CharField(max_length=120, db_column='CitationExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CitationExternalIdentifiers'


class Citations(models.Model):
    citationid = models.AutoField(db_column='CitationID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=120, db_column='Title')  # Field name made lowercase.
    publisher = models.CharField(max_length=120, db_column='Publisher')  # Field name made lowercase.
    publicationyear = models.IntegerField(db_column='PublicationYear')  # Field name made lowercase.
    citationlink = models.CharField(max_length=120, db_column='CitationLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citations'


class Dataloggerfiles(models.Model):
    dataloggerfileid = models.AutoField(db_column='DataLoggerFileID', primary_key=True)  # Field name made lowercase.
    programid = models.ForeignKey('Dataloggerprogramfiles', models.DO_NOTHING, db_column='ProgramID')  # Field name made lowercase.
    dataloggerfilename = models.CharField(max_length=120, db_column='DataLoggerFileName')  # Field name made lowercase.
    dataloggerfiledescription = models.CharField(max_length=120, db_column='DataLoggerFileDescription', blank=True, null=True)  # Field name made lowercase.
    dataloggerfilelink = models.CharField(max_length=120, db_column='DataLoggerFileLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataLoggerFiles'


class Dataquality(models.Model):
    dataqualityid = models.AutoField(db_column='DataQualityID', primary_key=True)  # Field name made lowercase.
    dataqualitytypecv = models.ForeignKey(CvDataqualitytype, models.DO_NOTHING, db_column='DataQualityTypeCV')  # Field name made lowercase.
    dataqualitycode = models.CharField(max_length=120, db_column='DataQualityCode')  # Field name made lowercase.
    dataqualityvalue = models.TextField(db_column='DataQualityValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dataqualityvalueunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='DataQualityValueUnitsID', blank=True, null=True)  # Field name made lowercase.
    dataqualitydescription = models.CharField(max_length=120, db_column='DataQualityDescription', blank=True, null=True)  # Field name made lowercase.
    dataqualitylink = models.CharField(max_length=120, db_column='DataQualityLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataQuality'


class Dataloggerfilecolumns(models.Model):
    dataloggerfilecolumnid = models.AutoField(db_column='DataloggerFileColumnID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID', blank=True, null=True)  # Field name made lowercase.
    dataloggerfileid = models.ForeignKey(Dataloggerfiles, models.DO_NOTHING, db_column='DataLoggerFileID')  # Field name made lowercase.
    instrumentoutputvariableid = models.ForeignKey('Instrumentoutputvariables', models.DO_NOTHING, db_column='InstrumentOutputVariableID')  # Field name made lowercase.
    columnlabel = models.CharField(max_length=120, db_column='ColumnLabel')  # Field name made lowercase.
    columndescription = models.CharField(max_length=120, db_column='ColumnDescription', blank=True, null=True)  # Field name made lowercase.
    measurementequation = models.CharField(max_length=120, db_column='MeasurementEquation', blank=True, null=True)  # Field name made lowercase.
    scaninterval = models.TextField(db_column='ScanInterval', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    scanintervalunitsid = models.ForeignKey('Units',verbose_name="scan interval units",related_name='+', blank=True, null=True,on_delete=models.CASCADE)  # Field name made lowercase.
    recordinginterval = models.TextField(db_column='RecordingInterval', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    recordingintervalunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='RecordingIntervalUnitsID', blank=True, null=True)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataloggerFileColumns'


class Dataloggerprogramfiles(models.Model):
    programid = models.AutoField(db_column='ProgramID', primary_key=True)  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliations, models.DO_NOTHING, db_column='AffiliationID')  # Field name made lowercase.
    programname = models.CharField(max_length=120, db_column='ProgramName')  # Field name made lowercase.
    programdescription = models.CharField(max_length=120, db_column='ProgramDescription', blank=True, null=True)  # Field name made lowercase.
    programversion = models.CharField(max_length=120, db_column='ProgramVersion', blank=True, null=True)  # Field name made lowercase.
    programfilelink = models.CharField(max_length=120, db_column='ProgramFileLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataloggerProgramFiles'


class Datasetcitations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey('Datasets', models.DO_NOTHING, db_column='DataSetID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DatasetCitations'


class Datasets(models.Model):
    datasetid = models.AutoField(db_column='DatasetID', primary_key=True)  # Field name made lowercase.
    datasetuuid = models.CharField(max_length=120, db_column='DatasetUUID')  # Field name made lowercase.
    datasettypecv = models.ForeignKey(CvDatasettype, models.DO_NOTHING, db_column='DatasetTypeCV')  # Field name made lowercase.
    datasetcode = models.CharField(max_length=120, db_column='DatasetCode')  # Field name made lowercase.
    datasettitle = models.CharField(max_length=120, db_column='DatasetTitle')  # Field name made lowercase.
    datasetabstract = models.CharField(max_length=120, db_column='DatasetAbstract')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Datasets'


class Datasetsresults(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Datasets, models.DO_NOTHING, db_column='DatasetID')  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DatasetsResults'


class Derivationequations(models.Model):
    derivationequationid = models.AutoField(db_column='DerivationEquationID', primary_key=True)  # Field name made lowercase.
    derivationequation = models.CharField(max_length=120, db_column='DerivationEquation')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DerivationEquations'


class Directives(models.Model):
    directiveid = models.AutoField(db_column='DirectiveID', primary_key=True)  # Field name made lowercase.
    directivetypecv = models.ForeignKey(CvDirectivetype, models.DO_NOTHING, db_column='DirectiveTypeCV')  # Field name made lowercase.
    directivedescription = models.CharField(max_length=120, db_column='DirectiveDescription')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Directives'


class Equipment(models.Model):
    equipmentid = models.AutoField(db_column='EquipmentID', primary_key=True)  # Field name made lowercase.
    equipmentcode = models.CharField(max_length=120, db_column='EquipmentCode')  # Field name made lowercase.
    equipmentname = models.CharField(max_length=120, db_column='EquipmentName')  # Field name made lowercase.
    equipmenttypecv = models.ForeignKey(CvEquipmenttype, models.DO_NOTHING, db_column='EquipmentTypeCV')  # Field name made lowercase.
    equipmentmodelid = models.ForeignKey('Equipmentmodels', models.DO_NOTHING, db_column='EquipmentModelID')  # Field name made lowercase.
    equipmentserialnumber = models.CharField(max_length=120, db_column='EquipmentSerialNumber')  # Field name made lowercase.
    equipmentownerid = models.ForeignKey('People', models.DO_NOTHING, db_column='EquipmentOwnerID')  # Field name made lowercase.
    equipmentvendorid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='EquipmentVendorID')  # Field name made lowercase.
    equipmentpurchasedate = models.DateTimeField(db_column='EquipmentPurchaseDate')  # Field name made lowercase.
    equipmentpurchaseordernumber = models.CharField(max_length=120, db_column='EquipmentPurchaseOrderNumber', blank=True, null=True)  # Field name made lowercase.
    equipmentdescription = models.CharField(max_length=120, db_column='EquipmentDescription', blank=True, null=True)  # Field name made lowercase.
    equipmentdocumentationlink = models.CharField(max_length=120, db_column='EquipmentDocumentationLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Equipment'


class Equipmentannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='EquipmentID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentAnnotations'


class Equipmentmodels(models.Model):
    equipmentmodelid = models.AutoField(db_column='EquipmentModelID', primary_key=True)  # Field name made lowercase.
    modelmanufacturerid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='ModelManufacturerID')  # Field name made lowercase.
    modelpartnumber = models.CharField(max_length=120, db_column='ModelPartNumber', blank=True, null=True)  # Field name made lowercase.
    modelname = models.CharField(max_length=120, db_column='ModelName')  # Field name made lowercase.
    modeldescription = models.CharField(max_length=120, db_column='ModelDescription', blank=True, null=True)  # Field name made lowercase.
    isinstrument = models.TextField(db_column='IsInstrument')  # Field name made lowercase. This field type is a guess.
    modelspecificationsfilelink = models.CharField(max_length=120, db_column='ModelSpecificationsFileLink', blank=True, null=True)  # Field name made lowercase.
    modellink = models.CharField(max_length=120, db_column='ModelLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentModels'


class Equipmentused(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='EquipmentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentUsed'


class Extensionproperties(models.Model):
    propertyid = models.AutoField(db_column='PropertyID', primary_key=True)  # Field name made lowercase.
    propertyname = models.CharField(max_length=120, db_column='PropertyName')  # Field name made lowercase.
    propertydescription = models.CharField(max_length=120, db_column='PropertyDescription', blank=True, null=True)  # Field name made lowercase.
    propertydatatypecv = models.ForeignKey(CvPropertydatatype, models.DO_NOTHING, db_column='PropertyDataTypeCV')  # Field name made lowercase.
    propertyunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='PropertyUnitsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExtensionProperties'


class Externalidentifiersystems(models.Model):
    externalidentifiersystemid = models.AutoField(db_column='ExternalIdentifierSystemID', primary_key=True)  # Field name made lowercase.
    externalidentifiersystemname = models.CharField(max_length=120, db_column='ExternalIdentifierSystemName')  # Field name made lowercase.
    identifiersystemorganizationid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='IdentifierSystemOrganizationID')  # Field name made lowercase.
    externalidentifiersystemdescription = models.CharField(max_length=120, db_column='ExternalIdentifierSystemDescription', blank=True, null=True)  # Field name made lowercase.
    externalidentifiersystemurl = models.CharField(max_length=120, db_column='ExternalIdentifierSystemURL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExternalIdentifierSystems'


class Featureactions(models.Model):
    featureactionid = models.AutoField(db_column='FeatureActionID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FeatureActions'


class Instrumentoutputvariables(models.Model):
    instrumentoutputvariableid = models.AutoField(db_column='InstrumentOutputVariableID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Equipmentmodels, models.DO_NOTHING, db_column='ModelID')  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    instrumentmethodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='InstrumentMethodID')  # Field name made lowercase.
    instrumentresolution = models.CharField(max_length=120, db_column='InstrumentResolution', blank=True, null=True)  # Field name made lowercase.
    instrumentaccuracy = models.CharField(max_length=120, db_column='InstrumentAccuracy', blank=True, null=True)  # Field name made lowercase.
    instrumentrawoutputunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='InstrumentRawOutputUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InstrumentOutputVariables'


class Maintenanceactions(models.Model):
    actionid = models.OneToOneField(Actions, models.DO_NOTHING, db_column='ActionID', primary_key=True)  # Field name made lowercase.
    isfactoryservice = models.TextField(db_column='IsFactoryService')  # Field name made lowercase. This field type is a guess.
    maintenancecode = models.CharField(max_length=120, db_column='MaintenanceCode', blank=True, null=True)  # Field name made lowercase.
    maintenancereason = models.CharField(max_length=120, db_column='MaintenanceReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaintenanceActions'


class Measurementresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Measurementresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementResultValueAnnotations'


class Measurementresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Measurementresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementResultValues'


class Measurementresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units", related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    ylocation = models.TextField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units", related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    zlocation = models.TextField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units", related_name='+',
                                          blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.ForeignKey('Units', verbose_name="time aggregation interval units", related_name='+',
                                                        blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MeasurementResults'


class Methodannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodAnnotations'


class Methodcitations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodCitations'


class Methodextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(max_length=120, db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodExtensionPropertyValues'


class Methodexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Methods', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    methodexternalidentifier = models.CharField(max_length=120, db_column='MethodExternalIdentifier')  # Field name made lowercase.
    methodexternalidentifieruri = models.CharField(max_length=120, db_column='MethodExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethodExternalIdentifiers'


class Methods(models.Model):
    methodid = models.AutoField(db_column='MethodID', primary_key=True)  # Field name made lowercase.
    methodtypecv = models.ForeignKey(CvMethodtype, models.DO_NOTHING, db_column='MethodTypeCV')  # Field name made lowercase.
    methodcode = models.CharField(max_length=120, db_column='MethodCode')  # Field name made lowercase.
    methodname = models.CharField(max_length=120, db_column='MethodName')  # Field name made lowercase.
    methoddescription = models.CharField(max_length=120, db_column='MethodDescription', blank=True, null=True)  # Field name made lowercase.
    methodlink = models.CharField(max_length=120, db_column='MethodLink', blank=True, null=True)  # Field name made lowercase.
    organizationid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='OrganizationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Methods'


class Modelaffiliations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey('Models', models.DO_NOTHING, db_column='ModelID')  # Field name made lowercase.
    affiliationid = models.ForeignKey(Affiliations, models.DO_NOTHING, db_column='AffiliationID')  # Field name made lowercase.
    isprimary = models.TextField(db_column='IsPrimary')  # Field name made lowercase. This field type is a guess.
    roledescription = models.CharField(max_length=120, db_column='RoleDescription', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ModelAffiliations'


class Models(models.Model):
    modelid = models.AutoField(db_column='ModelID', primary_key=True)  # Field name made lowercase.
    modelcode = models.CharField(max_length=120, db_column='ModelCode')  # Field name made lowercase.
    modelname = models.CharField(max_length=120, db_column='ModelName')  # Field name made lowercase.
    modeldescription = models.CharField(max_length=120, db_column='ModelDescription', blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=120, db_column='Version', blank=True, null=True)  # Field name made lowercase.
    modellink = models.CharField(max_length=120, db_column='ModelLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Models'


class Organizations(models.Model):
    organizationid = models.AutoField(db_column='OrganizationID', primary_key=True)  # Field name made lowercase.
    organizationtypecv = models.ForeignKey(CvOrganizationtype, models.DO_NOTHING, db_column='OrganizationTypeCV')  # Field name made lowercase.
    organizationcode = models.CharField(max_length=120, db_column='OrganizationCode')  # Field name made lowercase.
    organizationname = models.CharField(max_length=120, db_column='OrganizationName')  # Field name made lowercase.
    organizationdescription = models.CharField(max_length=120, db_column='OrganizationDescription', blank=True, null=True)  # Field name made lowercase.
    organizationlink = models.CharField(max_length=120, db_column='OrganizationLink', blank=True, null=True)  # Field name made lowercase.
    parentorganizationid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentOrganizationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organizations'


class People(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    personfirstname = models.CharField(max_length=120, db_column='PersonFirstName')  # Field name made lowercase.
    personmiddlename = models.CharField(max_length=120, db_column='PersonMiddleName', blank=True, null=True)  # Field name made lowercase.
    personlastname = models.CharField(max_length=120, db_column='PersonLastName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'People'


class Personexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    personid = models.ForeignKey(People, models.DO_NOTHING, db_column='PersonID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    personexternalidentifier = models.CharField(max_length=120, db_column='PersonExternalIdentifier')  # Field name made lowercase.
    personexternalidentifieruri = models.CharField(max_length=120, db_column='PersonExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonExternalIdentifiers'


class Pointcoverageresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Pointcoverageresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointCoverageResultValueAnnotations'


class Pointcoverageresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Pointcoverageresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation')  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    ylocation = models.TextField(db_column='YLocation')  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointCoverageResultValues'


class Pointcoverageresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.TextField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units", related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedxspacing = models.TextField(db_column='IntendedXSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedxspacingunitsid = models.ForeignKey('Units', verbose_name="intended x spacing units", related_name='+',
                                                 blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    intendedyspacing = models.TextField(db_column='IntendedYSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedyspacingunitsid = models.ForeignKey('Units', verbose_name="intended y spacing units", related_name='+',
                                                 blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.IntegerField(db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PointCoverageResults'


class Processinglevels(models.Model):
    processinglevelid = models.AutoField(db_column='ProcessingLevelID', primary_key=True)  # Field name made lowercase.
    processinglevelcode = models.CharField(max_length=120, db_column='ProcessingLevelCode')  # Field name made lowercase.
    definition = models.CharField(max_length=120, db_column='Definition', blank=True, null=True)  # Field name made lowercase.
    explanation = models.CharField(max_length=120, db_column='Explanation', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProcessingLevels'


class Profileresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Profileresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileResultValueAnnotations'


class Profileresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Profileresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    zlocation = models.TextField(db_column='ZLocation')  # Field name made lowercase. This field type is a guess.
    zaggregationinterval = models.TextField(db_column='ZAggregationInterval')  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.ForeignKey('Units',verbose_name="time aggregation interval units", related_name='+',
                                                        blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileResultValues'


class Profileresults(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    ylocation = models.TextField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedzspacing = models.TextField(db_column='IntendedZSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedzspacingunitsid = models.ForeignKey('Units', verbose_name="intended z spacing units",
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    intendedtimespacing = models.TextField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedtimespacingunitsid = models.ForeignKey('Units', verbose_name="intended time spacing units", related_name='+',
                                                    blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProfileResults'


class Referencematerialexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials', models.DO_NOTHING, db_column='ReferenceMaterialID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    referencematerialexternalidentifier = models.CharField(max_length=120, db_column='ReferenceMaterialExternalIdentifier')  # Field name made lowercase.
    referencematerialexternalidentifieruri = models.CharField(max_length=120, db_column='ReferenceMaterialExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceMaterialExternalIdentifiers'


class Referencematerialvalues(models.Model):
    referencematerialvalueid = models.AutoField(db_column='ReferenceMaterialValueID', primary_key=True)  # Field name made lowercase.
    referencematerialid = models.ForeignKey('Referencematerials', models.DO_NOTHING, db_column='ReferenceMaterialID')  # Field name made lowercase.
    referencematerialvalue = models.TextField(db_column='ReferenceMaterialValue')  # Field name made lowercase. This field type is a guess.
    referencematerialaccuracy = models.TextField(db_column='ReferenceMaterialAccuracy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='UnitsID')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceMaterialValues'


class Referencematerials(models.Model):
    referencematerialid = models.AutoField(db_column='ReferenceMaterialID', primary_key=True)  # Field name made lowercase.
    referencematerialmediumcv = models.ForeignKey(CvMedium, models.DO_NOTHING, db_column='ReferenceMaterialMediumCV')  # Field name made lowercase.
    referencematerialorganizationid = models.ForeignKey(Organizations, models.DO_NOTHING, db_column='ReferenceMaterialOrganizationID')  # Field name made lowercase.
    referencematerialcode = models.CharField(max_length=120, db_column='ReferenceMaterialCode')  # Field name made lowercase.
    referencemateriallotcode = models.CharField(max_length=120, db_column='ReferenceMaterialLotCode', blank=True, null=True)  # Field name made lowercase.
    referencematerialpurchasedate = models.DateTimeField(db_column='ReferenceMaterialPurchaseDate', blank=True, null=True)  # Field name made lowercase.
    referencematerialexpirationdate = models.DateTimeField(db_column='ReferenceMaterialExpirationDate', blank=True, null=True)  # Field name made lowercase.
    referencematerialcertificatelink = models.CharField(max_length=120, db_column='ReferenceMaterialCertificateLink', blank=True, null=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceMaterials'


class Relatedactions(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, verbose_name="action id", related_name="relatedActionID",
                                 db_column='ActionID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedactionid = models.ForeignKey(Actions, verbose_name="related action id",related_name="relatedRelatedActionID",
                                        db_column='RelatedActionID', blank=True, null=True, on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedActions'


class Relatedannotations(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, verbose_name="annotation id", related_name="relatedAnnotationID",
                                 db_column='AnnotationID', blank=True, null=True, on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
     # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedAnnotations'


class Relatedcitations(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, verbose_name="citation id", related_name="relatedCitationID",
                                    db_column='CitatationID', blank=True, null=True, on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedcitationid = models.ForeignKey(Citations, verbose_name="related citation id",
                                            related_name="relatedRelatedCitationID",
                                            db_column='RelatedCitationID', blank=True, null=True,
                                            on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'RelatedCitations'


class Relateddatasets(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    datasetid = models.ForeignKey(Datasets, verbose_name="dataset id", related_name="relatedDatasetID",
                                  db_column='DatasetID', blank=True, null=True, on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relateddatasetid = models.ForeignKey(Datasets, verbose_name="related dataset id",
                                          related_name="relatedRelatedDatasetID",
                                          db_column='RelatedDatasetID', blank=True, null=True,
                                          on_delete=models.CASCADE)
    versioncode = models.CharField(max_length=120, db_column='VersionCode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedDatasets'


class Relatedequipment(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    equipmentid = models.ForeignKey(Equipment, verbose_name="equipment id",
                                           related_name="relatedEquipmentID",
                                           db_column='EquipmentID', blank=True, null=True,
                                           on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedequipmentid = models.ForeignKey(Equipment, verbose_name="related equipment id",
                                         related_name="relatedRelatedEquipmentID",
                                         db_column='RelatedEquipmentID', blank=True, null=True,
                                         on_delete=models.CASCADE)
    relationshipstartdatetime = models.DateTimeField(db_column='RelationshipStartDateTime')  # Field name made lowercase.
    relationshipstartdatetimeutcoffset = models.IntegerField(db_column='RelationshipStartDateTimeUTCOffset')  # Field name made lowercase.
    relationshipenddatetime = models.DateTimeField(db_column='RelationshipEndDateTime', blank=True, null=True)  # Field name made lowercase.
    relationshipenddatetimeutcoffset = models.IntegerField(db_column='RelationshipEndDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedEquipment'


class Relatedfeatures(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', verbose_name="sampling feature id",
                                         related_name="relatedSamplingFeatureid",
                                         db_column='RelatedSamplingID', blank=True, null=True,
                                         on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedfeatureid = models.ForeignKey('Samplingfeatures', verbose_name="related feature id",
                                           related_name="relatedRelatedFeatureid",
                                           db_column='RelatedFeatureID', blank=True, null=True,
                                           on_delete=models.CASCADE)
    spatialoffsetid = models.ForeignKey('Spatialoffsets', models.DO_NOTHING, db_column='SpatialOffsetID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedFeatures'


class Relatedmodels(models.Model):
    relatedid = models.AutoField(db_column='RelatedID', primary_key=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Models, models.DO_NOTHING, db_column='ModelID')  # Field name made lowercase.
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedmodelid = models.IntegerField(db_column='RelatedModelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedModels'


class Relatedresults(models.Model):
    relationid = models.AutoField(db_column='RelationID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', verbose_name="result id",
                                          related_name="relatedResultid",
                                          db_column='ResultID', blank=True, null=True,
                                          on_delete=models.CASCADE)
    relationshiptypecv = models.ForeignKey(CvRelationshiptype, models.DO_NOTHING, db_column='RelationshipTypeCV')  # Field name made lowercase.
    relatedresultid = models.ForeignKey('Results', verbose_name="related result id",
                                 related_name="relatedRelatedResultid",
                                 db_column='RelatedResultID', blank=True, null=True,
                                 on_delete=models.CASCADE)
    versioncode = models.CharField(max_length=120, db_column='VersionCode', blank=True, null=True)  # Field name made lowercase.
    relatedresultsequencenumber = models.IntegerField(db_column='RelatedResultSequenceNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RelatedResults'


class Resultannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.
    begindatetime = models.DateTimeField(db_column='BeginDateTime')  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultAnnotations'


class Resultderivationequations(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    derivationequationid = models.ForeignKey(Derivationequations, models.DO_NOTHING, db_column='DerivationEquationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultDerivationEquations'


class Resultextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Results', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(max_length=120, db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultExtensionPropertyValues'


class Resultnormalizationvalues(models.Model):
    resultid = models.OneToOneField('Results', models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    normalizedbyreferencematerialvalueid = models.ForeignKey(Referencematerialvalues, models.DO_NOTHING, db_column='NormalizedByReferenceMaterialValueID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultNormalizationValues'


class Results(models.Model):
    resultid = models.AutoField(db_column='ResultID', primary_key=True)  # Field name made lowercase.
    resultuuid = models.CharField(max_length=120, db_column='ResultUUID')  # Field name made lowercase.
    featureactionid = models.ForeignKey(Featureactions, models.DO_NOTHING, db_column='FeatureActionID')  # Field name made lowercase.
    resulttypecv = models.ForeignKey(CvResulttype, models.DO_NOTHING, db_column='ResultTypeCV')  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    unitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='UnitsID')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers', models.DO_NOTHING, db_column='TaxonomicClassifierID', blank=True, null=True)  # Field name made lowercase.
    processinglevelid = models.ForeignKey(Processinglevels, models.DO_NOTHING, db_column='ProcessingLevelID')  # Field name made lowercase.
    resultdatetime = models.DateTimeField(db_column='ResultDateTime', blank=True, null=True)  # Field name made lowercase.
    resultdatetimeutcoffset = models.IntegerField(db_column='ResultDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    validdatetime = models.DateTimeField(db_column='ValidDateTime', blank=True, null=True)  # Field name made lowercase.
    validdatetimeutcoffset = models.IntegerField(db_column='ValidDateTimeUTCOffset', blank=True, null=True)  # Field name made lowercase.
    statuscv = models.ForeignKey(CvStatus, models.DO_NOTHING, db_column='StatusCV', blank=True, null=True)  # Field name made lowercase.
    sampledmediumcv = models.ForeignKey(CvMedium, models.DO_NOTHING, db_column='SampledMediumCV')  # Field name made lowercase.
    valuecount = models.IntegerField(db_column='ValueCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Results'


class Resultsdataquality(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Results, models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    dataqualityid = models.ForeignKey(Dataquality, models.DO_NOTHING, db_column='DataQualityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultsDataQuality'


class Samplingfeatureannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatureAnnotations'


class Samplingfeatureextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(max_length=120, db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatureExtensionPropertyValues'


class Samplingfeatureexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Samplingfeatures', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    samplingfeatureexternalidentifier = models.CharField(max_length=120, db_column='SamplingFeatureExternalIdentifier')  # Field name made lowercase.
    samplingfeatureexternalidentifieruri = models.CharField(max_length=120, db_column='SamplingFeatureExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatureExternalIdentifiers'


class Samplingfeatures(models.Model):
    samplingfeatureid = models.AutoField(db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    samplingfeatureuuid = models.CharField(max_length=120, db_column='SamplingFeatureUUID')  # Field name made lowercase.
    samplingfeaturetypecv = models.ForeignKey(CvSamplingfeaturetype, models.DO_NOTHING, db_column='SamplingFeatureTypeCV')  # Field name made lowercase.
    samplingfeaturecode = models.CharField(max_length=120, db_column='SamplingFeatureCode')  # Field name made lowercase.
    samplingfeaturename = models.CharField(max_length=120, db_column='SamplingFeatureName', blank=True, null=True)  # Field name made lowercase.
    samplingfeaturedescription = models.CharField(max_length=120, db_column='SamplingFeatureDescription', blank=True, null=True)  # Field name made lowercase.
    samplingfeaturegeotypecv = models.ForeignKey(CvSamplingfeaturegeotype, models.DO_NOTHING, db_column='SamplingFeatureGeotypeCV', blank=True, null=True)  # Field name made lowercase.
    featuregeometry = models.TextField(db_column='FeatureGeometry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    featuregeometrywkt = models.CharField(max_length=120, db_column='FeatureGeometryWKT', blank=True, null=True)  # Field name made lowercase.
    elevation_m = models.TextField(db_column='Elevation_m', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    elevationdatumcv = models.ForeignKey(CvElevationdatum, models.DO_NOTHING, db_column='ElevationDatumCV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SamplingFeatures'


class Sectionresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Sectionresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectionResultValueAnnotations'


class Sectionresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Sectionresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation')  # Field name made lowercase. This field type is a guess.
    xaggregationinterval = models.TextField(db_column='XAggregationInterval')  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)

    zlocation = models.IntegerField(db_column='ZLocation')  # Field name made lowercase.
    zaggregationinterval = models.TextField(db_column='ZAggregationInterval')  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.ForeignKey('Units', verbose_name="time aggregation interval units",
                                                       related_name='+',
                                                       blank=True, null=True,
                                                       on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectionResultValues'


class Sectionresults(models.Model):
    resultid = models.OneToOneField(Results, models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    ylocation = models.TextField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedxspacing = models.TextField(db_column='IntendedXSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedzxpacingunitsid = models.ForeignKey('Units', verbose_name="intended x spacing units",
                                                related_name='+',
                                                blank=True, null=True, on_delete=models.CASCADE)
    intendedzspacing = models.TextField(db_column='IntendedZSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedzspacingunitsid = models.ForeignKey('Units', verbose_name="intended z spacing units",
                                                related_name='+',
                                                blank=True, null=True, on_delete=models.CASCADE)
    # Field name made lowercase.
    intendedtimespacing = models.TextField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedtimespacingunitsid = models.ForeignKey('Units', verbose_name="intended time spacing units",
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SectionResults'


class Simulations(models.Model):
    simulationid = models.AutoField(db_column='SimulationID', primary_key=True)  # Field name made lowercase.
    actionid = models.ForeignKey(Actions, models.DO_NOTHING, db_column='ActionID')  # Field name made lowercase.
    simulationname = models.CharField(max_length=120, db_column='SimulationName')  # Field name made lowercase.
    simulationdescription = models.CharField(max_length=120, db_column='SimulationDescription', blank=True, null=True)  # Field name made lowercase.
    simulationstartdatetime = models.DateTimeField(db_column='SimulationStartDateTime')  # Field name made lowercase.
    simulationstartdatetimeutcoffset = models.IntegerField(db_column='SimulationStartDateTimeUTCOffset')  # Field name made lowercase.
    simulationenddatetime = models.DateTimeField(db_column='SimulationEndDateTime')  # Field name made lowercase.
    simulationenddatetimeutcoffset = models.IntegerField(db_column='SimulationEndDateTimeUTCOffset')  # Field name made lowercase.
    timestepvalue = models.TextField(db_column='TimeStepValue')  # Field name made lowercase. This field type is a guess.
    timestepunitsid = models.IntegerField(db_column='TimeStepUnitsID')  # Field name made lowercase.
    inputdatasetid = models.IntegerField(db_column='InputDataSetID', blank=True, null=True)  # Field name made lowercase.
    modelid = models.ForeignKey(Models, models.DO_NOTHING, db_column='ModelID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Simulations'


class Sites(models.Model):
    samplingfeatureid = models.OneToOneField(Samplingfeatures, models.DO_NOTHING, db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    sitetypecv = models.ForeignKey(CvSitetype, models.DO_NOTHING, db_column='SiteTypeCV')  # Field name made lowercase.
    latitude = models.TextField(db_column='Latitude')  # Field name made lowercase. This field type is a guess.
    longitude = models.TextField(db_column='Longitude')  # Field name made lowercase. This field type is a guess.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sites'


class Spatialoffsets(models.Model):
    spatialoffsetid = models.AutoField(db_column='SpatialOffsetID', primary_key=True)  # Field name made lowercase.
    spatialoffsettypecv = models.ForeignKey(CvSpatialoffsettype, models.DO_NOTHING, db_column='SpatialOffsetTypeCV')  # Field name made lowercase.
    offset1value = models.TextField(db_column='Offset1Value')  # Field name made lowercase. This field type is a guess.
    offset1unitid = models.ForeignKey('Units', verbose_name="off set1 units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    offset2value = models.TextField(db_column='Offset2Value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offset2unitid = models.ForeignKey('Units', verbose_name="off set2 units",
                                      related_name='+',
                                      blank=True, null=True, on_delete=models.CASCADE)
    offset3value = models.TextField(db_column='Offset3Value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    offset2unitid = models.ForeignKey('Units', verbose_name="off set3 units",
                                      related_name='+',
                                      blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'SpatialOffsets'


class Spatialreferenceexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey('Spatialreferences', models.DO_NOTHING, db_column='SpatialReferenceID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    spatialreferenceexternalidentifier = models.CharField(max_length=120, db_column='SpatialReferenceExternalIdentifier')  # Field name made lowercase.
    spatialreferenceexternalidentifieruri = models.CharField(max_length=120, db_column='SpatialReferenceExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpatialReferenceExternalIdentifiers'


class Spatialreferences(models.Model):
    spatialreferenceid = models.AutoField(db_column='SpatialReferenceID', primary_key=True)  # Field name made lowercase.
    srscode = models.CharField(max_length=120, db_column='SRSCode', blank=True, null=True)  # Field name made lowercase.
    srsname = models.CharField(max_length=120, db_column='SRSName')  # Field name made lowercase.
    srsdescription = models.CharField(max_length=120, db_column='SRSDescription', blank=True, null=True)  # Field name made lowercase.
    srslink = models.CharField(max_length=120, db_column='SRSLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpatialReferences'


class Specimenbatchpostions(models.Model):
    featureactionid = models.OneToOneField(Featureactions, models.DO_NOTHING, db_column='FeatureActionID', primary_key=True)  # Field name made lowercase.
    batchpositionnumber = models.IntegerField(db_column='BatchPositionNumber')  # Field name made lowercase.
    batchpositionlabel = models.CharField(max_length=120, db_column='BatchPositionLabel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpecimenBatchPostions'


class Specimentaxonomicclassifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    samplingfeatureid = models.ForeignKey('Specimens', models.DO_NOTHING, db_column='SamplingFeatureID')  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers', models.DO_NOTHING, db_column='TaxonomicClassifierID')  # Field name made lowercase.
    citationid = models.ForeignKey(Citations, models.DO_NOTHING, db_column='CitationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpecimenTaxonomicClassifiers'


class Specimens(models.Model):
    samplingfeatureid = models.OneToOneField(Samplingfeatures, models.DO_NOTHING, db_column='SamplingFeatureID', primary_key=True)  # Field name made lowercase.
    specimentypecv = models.ForeignKey(CvSpecimentype, models.DO_NOTHING, db_column='SpecimenTypeCV')  # Field name made lowercase.
    specimenmediumcv = models.ForeignKey(CvMedium, models.DO_NOTHING, db_column='SpecimenMediumCV')  # Field name made lowercase.
    isfieldspecimen = models.TextField(db_column='IsFieldSpecimen')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Specimens'


class Spectraresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Spectraresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpectraResultValueAnnotations'


class Spectraresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Spectraresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    excitationwavelength = models.TextField(db_column='ExcitationWavelength')  # Field name made lowercase. This field type is a guess.
    emissionwavelength = models.TextField(db_column='EmissionWavelength')  # Field name made lowercase. This field type is a guess.
    wavelengthunitsid = models.ForeignKey('Units', verbose_name="wave length units",
                                                       related_name='+',
                                                       blank=True, null=True, on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.ForeignKey('Units', verbose_name="time aggregation interval units",
                                                         related_name='+',
                                                         blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'SpectraResultValues'


class Spectraresults(models.Model):
    resultid = models.OneToOneField(Results, models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    ylocation = models.TextField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    zlocation = models.TextField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey(Spatialreferences, models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedwavelengthspacing = models.TextField(db_column='IntendedWavelengthSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedwavelengthspacingunitsid = models.ForeignKey('Units', verbose_name="intended wave length spacing units",
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SpectraResults'


class Taxonomicclassifierexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    taxonomicclassifierid = models.ForeignKey('Taxonomicclassifiers', models.DO_NOTHING, db_column='TaxonomicClassifierID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    taxonomicclassifierexternalidentifier = models.CharField(max_length=120, db_column='TaxonomicClassifierExternalIdentifier')  # Field name made lowercase.
    taxonomicclassifierexternalidentifieruri = models.CharField(max_length=120, db_column='TaxonomicClassifierExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxonomicClassifierExternalIdentifiers'


class Taxonomicclassifiers(models.Model):
    taxonomicclassifierid = models.AutoField(db_column='TaxonomicClassifierID', primary_key=True)  # Field name made lowercase.
    taxonomicclassifiertypecv = models.ForeignKey(CvTaxonomicclassifiertype, models.DO_NOTHING, db_column='TaxonomicClassifierTypeCV')  # Field name made lowercase.
    taxonomicclassifiername = models.CharField(max_length=120, db_column='TaxonomicClassifierName')  # Field name made lowercase.
    taxonomicclassifiercommonname = models.CharField(max_length=120, db_column='TaxonomicClassifierCommonName', blank=True, null=True)  # Field name made lowercase.
    taxonomicclassifierdescription = models.CharField(max_length=120, db_column='TaxonomicClassifierDescription', blank=True, null=True)  # Field name made lowercase.
    parenttaxonomicclassifierid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentTaxonomicClassifierID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaxonomicClassifiers'


class Timeseriesresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Timeseriesresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeSeriesResultValueAnnotations'


class Timeseriesresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Timeseriesresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.ForeignKey('Units', models.DO_NOTHING, db_column='TimeAggregationIntervalUnitsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeSeriesResultValues'


class Timeseriesresults(models.Model):
    resultid = models.OneToOneField(Results, models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         related_name='+',
                                         db_column='XLocationUnitsID', blank=True, null=True, on_delete=models.CASCADE)
    ylocation = models.TextField(db_column='YLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         db_column='YLocationUnitsID', related_name='+',blank=True, null=True, on_delete=models.CASCADE)
    zlocation = models.TextField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units",
                                         db_column='ZLocationUnitsID',
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)

    spatialreferenceid = models.ForeignKey(Spatialreferences, models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedtimespacing = models.TextField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedtimespacingunitsid = models.ForeignKey('Units', verbose_name="intended time spacing units",
                                                   db_column='IntendedTimeSpacingUnitsID',
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TimeSeriesResults'


class Trajectoryresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Trajectoryresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrajectoryResultValueAnnotations'


class Trajectoryresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Trajectoryresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation')  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         db_column='XLocationUnitsID',
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    ylocation = models.TextField(db_column='YLocation')  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         db_column='YLocationUnitsID',
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    zlocation = models.TextField(db_column='ZLocation')  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units",
                                         related_name='+',
                                         db_column='ZLocationUnitsID',
                                         blank=True, null=True, on_delete=models.CASCADE)
    trajectorydistance = models.TextField(db_column='TrajectoryDistance')  # Field name made lowercase. This field type is a guess.
    trajectorydistanceaggregationinterval = models.TextField(db_column='TrajectoryDistanceAggregationInterval')  # Field name made lowercase. This field type is a guess.
    trajectorydistanceunitsid = models.ForeignKey('Units', verbose_name="trajectory distance units",
                                                  db_column='TrajectoryDistanceAggregationIntervalUnitsID',
                                                  related_name='+',
                                                  blank=True, null=True, on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.ForeignKey('Units', verbose_name="time aggregation interval units",
                                                       db_column='TimeAggregationIntervalUnitsID',
                                                       related_name='+',
                                                       blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'TrajectoryResultValues'


class Trajectoryresults(models.Model):
    resultid = models.OneToOneField(Results, models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    spatialreferenceid = models.ForeignKey(Spatialreferences, models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedtrajectoryspacing = models.TextField(db_column='IntendedTrajectorySpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedtrajectoryspacingunitsid = models.ForeignKey('Units', verbose_name="intended trajectory spacing units",
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)
    intendedtimespacing = models.TextField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedtimespacingunitsid = models.ForeignKey('Units', verbose_name="intended time spacing units",
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrajectoryResults'


class Transectresultvalueannotations(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    valueid = models.ForeignKey('Transectresultvalues', models.DO_NOTHING, db_column='ValueID')  # Field name made lowercase.
    annotationid = models.ForeignKey(Annotations, models.DO_NOTHING, db_column='AnnotationID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransectResultValueAnnotations'


class Transectresultvalues(models.Model):
    valueid = models.AutoField(db_column='ValueID', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey('Transectresults', models.DO_NOTHING, db_column='ResultID')  # Field name made lowercase.
    datavalue = models.TextField(db_column='DataValue')  # Field name made lowercase. This field type is a guess.
    valuedatetime = models.DateTimeField(db_column='ValueDateTime')  # Field name made lowercase.
    valuedatetimeutcoffset = models.IntegerField(db_column='ValueDateTimeUTCOffset')  # Field name made lowercase.
    xlocation = models.TextField(db_column='XLocation')  # Field name made lowercase. This field type is a guess.
    xlocationunitsid = models.ForeignKey('Units', verbose_name="x location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    ylocation = models.TextField(db_column='YLocation')  # Field name made lowercase. This field type is a guess.
    ylocationunitsid = models.ForeignKey('Units', verbose_name="y location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    transectdistance = models.TextField(db_column='TransectDistance')  # Field name made lowercase. This field type is a guess.
    transectdistanceaggregationinterval = models.TextField(db_column='TransectDistanceAggregationInterval')  # Field name made lowercase. This field type is a guess.
    transectdistanceunitsid = models.ForeignKey('Units', verbose_name="transect distance units",
                                                       related_name='+',
                                                       blank=True, null=True, on_delete=models.CASCADE)
    censorcodecv = models.ForeignKey(CvCensorcode, models.DO_NOTHING, db_column='CensorCodeCV')  # Field name made lowercase.
    qualitycodecv = models.ForeignKey(CvQualitycode, models.DO_NOTHING, db_column='QualityCodeCV')  # Field name made lowercase.
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.
    timeaggregationinterval = models.TextField(db_column='TimeAggregationInterval')  # Field name made lowercase. This field type is a guess.
    timeaggregationintervalunitsid = models.ForeignKey('Units', verbose_name="time aggregation interval units",
                                                       related_name='+',
                                                       blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'TransectResultValues'


class Transectresults(models.Model):
    resultid = models.OneToOneField(Results, models.DO_NOTHING, db_column='ResultID', primary_key=True)  # Field name made lowercase.
    zlocation = models.TextField(db_column='ZLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zlocationunitsid = models.ForeignKey('Units', verbose_name="z location units",
                                         related_name='+',
                                         blank=True, null=True, on_delete=models.CASCADE)
    spatialreferenceid = models.ForeignKey(Spatialreferences, models.DO_NOTHING, db_column='SpatialReferenceID', blank=True, null=True)  # Field name made lowercase.
    intendedtransectspacing = models.TextField(db_column='IntendedTransectSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedtransectspacingunitsid = models.ForeignKey('Units', verbose_name="intended transect spacing units",
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)
    intendedtimespacing = models.TextField(db_column='IntendedTimeSpacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    intendedtimespacingunitsid = models.ForeignKey('Units', verbose_name="intended time spacing units",
                                                   related_name='+',
                                                   blank=True, null=True, on_delete=models.CASCADE)
    aggregationstatisticcv = models.ForeignKey(CvAggregationstatistic, models.DO_NOTHING, db_column='AggregationStatisticCV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransectResults'


class Units(models.Model):
    unitsid = models.AutoField(db_column='UnitsID', primary_key=True)  # Field name made lowercase.
    unitstypecv = models.ForeignKey(CvUnitstype, models.DO_NOTHING, db_column='UnitsTypeCV')  # Field name made lowercase.
    unitsabbreviation = models.CharField(max_length=120, db_column='UnitsAbbreviation')  # Field name made lowercase.
    unitsname = models.CharField(max_length=120, db_column='UnitsName')  # Field name made lowercase.
    unitslink = models.CharField(max_length=120, db_column='UnitsLink', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Units'


class Variableextensionpropertyvalues(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    propertyid = models.ForeignKey(Extensionproperties, models.DO_NOTHING, db_column='PropertyID')  # Field name made lowercase.
    propertyvalue = models.CharField(max_length=120, db_column='PropertyValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VariableExtensionPropertyValues'


class Variableexternalidentifiers(models.Model):
    bridgeid = models.AutoField(db_column='BridgeID', primary_key=True)  # Field name made lowercase.
    variableid = models.ForeignKey('Variables', models.DO_NOTHING, db_column='VariableID')  # Field name made lowercase.
    externalidentifiersystemid = models.ForeignKey(Externalidentifiersystems, models.DO_NOTHING, db_column='ExternalIdentifierSystemID')  # Field name made lowercase.
    variableexternalidentifer = models.CharField(max_length=120, db_column='VariableExternalIdentifer')  # Field name made lowercase.
    variableexternalidentifieruri = models.CharField(max_length=120, db_column='VariableExternalIdentifierURI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VariableExternalIdentifiers'


class Variables(models.Model):
    variableid = models.AutoField(db_column='VariableID', primary_key=True)  # Field name made lowercase.
    variabletypecv = models.ForeignKey(CvVariabletype, models.DO_NOTHING, db_column='VariableTypeCV')  # Field name made lowercase.
    variablecode = models.CharField(max_length=120, db_column='VariableCode')  # Field name made lowercase.
    variablenamecv = models.ForeignKey(CvVariablename, models.DO_NOTHING, db_column='VariableNameCV')  # Field name made lowercase.
    variabledefinition = models.CharField(max_length=120, db_column='VariableDefinition', blank=True, null=True)  # Field name made lowercase.
    speciationcv = models.ForeignKey(CvSpeciation, models.DO_NOTHING, db_column='SpeciationCV', blank=True, null=True)  # Field name made lowercase.
    nodatavalue = models.TextField(db_column='NoDataValue')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Variables'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField( max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField( max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
