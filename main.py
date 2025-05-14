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
           self.LinearRegression_PipelineInitiate()

       def LinearRegression_PipelineInitiate(self):
            linearRegressionModelResult = LinearRegression_Execution(self.x, self.y, self.TargetValue)
            self.predicted_value = linearRegressionModelResult.predicted_value

   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "LogisticRegressionSelected"

class LogisticRegression_RunCommand:
    def __init__(self, x, y, ValueToPredict, weight_LogReg, bias_LogReg,
                 LearningRate, Epochs):
        self.x = x
        self.y = y
        self.ValueToPredict = ValueToPredict
        self.weights = weight_LogReg
        self.bias = bias_LogReg
        self.learning_rate = LearningRate
        self.epochs = Epochs
        self.predicted_value = None
        self.LogisticRegression_PipelineInitiate()

    def LogisticRegression_PipelineInitiate(self):
        # You probably want to call a LogisticRegression_Execution instead of LinearRegression_Execution
        logisticModelResult = LinearRegression_Execution(  # <-- FIX this if needed
            self.x, self.y, self.ValueToPredict,
            self.weights, self.bias,
            self.learning_rate, self.epochs
        )
        self.predicted_value = logisticModelResult.predicted_value


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    # You can test-run the class here if needed, like:
    # model = LogisticRegression_RunCommand(...)
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

# STAGE_NAME = "LogisticRegressionSelected"
# try:
#    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#    class LogisticRegression_RunCommand:
#        def __init__(self,x,y, ValueToPredict, weight_LogReg, bias_LogReg,
#                     LearningRate, Epochs):
#            self.x = x
#            self.y = y
#            self.ValueToPredict = ValueToPredict
#            # Initialize weights (slope and intercept)
#            self.weights = weight_LogReg
#            self.bias = bias_LogReg  # bias/intercept
#            self.learning_rate = LearningRate # 0.1
#            self.epochs = Epochs# 1000
#            self.predicted_value = None
#            # print(self.x, self.y, self.ValueToPredict, self.weights, self.bias, self.learning_rate, self.epochs)
#            self.LinearRegression_PipelineInitiate()
#
#        def LinearRegression_PipelineInitiate(self):
#            # print(self.x, self.y, self.ValueToPredict, self.weights, self.bias, self.learning_rate,
#            #       self.epochs)
#            linearRegressionModelResult = LinearRegression_Execution(self.x, self.y, self.ValueToPredict,
#                                                                      self.weights, self.bias, self.learning_rate,
#                                                                      self.epochs
#                                                                      )
#            self.predicted_value = linearRegressionModelResult.predicted_value
#
#    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#         logger.exception(e)
#         raise e
