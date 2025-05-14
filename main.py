from src.DataScience_Algorithms.pipeline.LinearRegression_Pipeline import LinearRegression_Execution
from src.DataScience_Algorithms.logging import logger

STAGE_NAME = "LinearRegressionSelected"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   class LinearRegression_RunCommand:
       def __init__(self,x,y, targetValue):
           self.x = x
           self.y = y
           self.TargetValue = targetValue
           self.predicted_value = None
           self.PipelineInitiate()

       def PipelineInitiate(self):
            linearRegressionModelResult = LinearRegression_Execution(self.x, self.y, self.TargetValue)
            self.predicted_value = linearRegressionModelResult.predicted_value

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
