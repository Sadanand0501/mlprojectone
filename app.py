from src.mlprojectfirst.logger import logging
from src.mlprojectfirst.exception import CustomException
from src.mlprojectfirst.components.data_ingestion import DataIngestion
from src.mlprojectfirst.components.data_ingestion import DataIngestionConfig
from src.mlprojectfirst.components.data_transformation import DataTransformationConfig,DataTransformation
import sys





if __name__=="__main__":
    logging.info("The execution has started")
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)