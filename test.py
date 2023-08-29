from Currency_Detection.components.data_ingestion import DataIngestion
from Currency_Detection.components.data_validation import DataValidation
from Currency_Detection.entity.config_entity import DataValidationConfig
from Currency_Detection.entity.artifacts_entity import (DataIngestionArtifact,
                                                 DataValidationArtifact)


data_ingestion=DataIngestion()
data_igestion_artifacts=data_ingestion.initiate_data_ingestion()
data_validation_config=DataValidationConfig()
data_validation=DataValidation(data_ingestion_artifact=data_igestion_artifacts,data_validation_config=data_validation_config)
data_validation.initiate_data_validation()



