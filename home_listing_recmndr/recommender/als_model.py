import numpy as np
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder, TrainValidationSplit
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
!pip install pyspark

class als_mf():
	def __init__(self, ratings, verbose = True):
		"""
		Recommend listsings under the assumption that a predicted rating R is approximate to the user matrix multiplied by its transpose times the item matrix multiplied by it's transpose

		Parameters
		----------
		ratings: (array)
			User x Item matrix for approximate ratings

		latent_factors: (int)
			Dimension k- hyperparameter that can be optimized using grid search

		verbose: (bool)
			To Print Training Progress or not to Print Training Progress
		"""

		spark= SparkSession.builder \  
		.master("local[1]"") \
		.appName("ALS_Recommender") \
		.getOrCreate()

		data = spark.read.format("csv").option("header", "true").load("data.csv")

		train, test = data.randomSplit([.75, .25], seed = 42)

	def train(self, als, userCol = 'id_user', itemCol = 'power_rankings'):


		als = ALS(implicitPrefs = False, userCol = 'id_user', itemCol = 'power_rankings'
		, coldStartStrategy = 'drop')

		model = als.fit(train)

	def hyperparameters(params):


		params = ParamGridBuilder() \
				.addGrid(model.rank, [5, 10]) \
				.addGrid(model.maxIter, [10, 25]) \
				.addGrid(model.regParam, [.01, .001]) \
				.build()

		evaluator = RegressionEvaluator(metricName = "rmse", labelCol = "rmse_scores")

		cv = CrossValidator(estimator = model
			, estimatorParamMaps = params
			, evaluator = evaluator)

		cv_run = cv.fit(train)


	def predict():

		predict_test= cv_run.bestModel.transform(test)

		userRecs = predict_test.recommendForAllUsers(10)
		itemRecs = predict_test.recommendForAllUsers(10)

	def save_model(model):

		path = "/models"

		cv_run.write().overwrite().save(path)

	pool.close()
	spark.stop()


