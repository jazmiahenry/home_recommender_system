import numpy as np
import pandas as pd
from functions import * 

class power_rankings(df):
	"""
	Creates power rankings of each listing. Following rankings:
	Holiday: .8
	Pro Pictures: 1.2
	Num Books 90 day: 
	Weekly Discount:  1.2
	Monthly Discount: 1.2

	"""

	def w_review(df):
		"""
		Reduce review ranking if total number of reviews are in bottom quantile. 
		Multiply review ratings by .5 for middle quantile. Multiply by .75 for third quantile. 
		Multiply by 1 if ratings in top quantile. Assumption is that top 
		"""

		cont_to_ord(df)
		w_review = []

		for i in len(df['review_rank']):
			if review_rank == 'MIN':
				new_rank = listing_review_rating * .1
				w_review.append(new_rank)

			elif review_rank == '25%':
				new_rank = listing_review_rating * .25
				w_review.append(new_rank)

			elif review_rank == 'AVG':
				new_rank = listing_review * .5
				w_review.append(new_rank)

			elif review_rank == '75%':
				new_rank = listing_review_rating * .75
				w_review.append(new_rank)

			else:
				new_rank = listing_review_rating
				w_review.append(new_rank)

	def user_prefs():
		"""Capture User Preferences by matching queries with listing"""


		if query_center_lat == listing_lat & query_center_lng == listing_lat:
			return listing_review_rating * 2

		else:
			return listing_review_rating

		return ' '

	def holiday_rank(df):
		df['ds_book'] = pd.to_datetime(df['ds_book'])
		date_1 = 
		date_2 =

		for date in len(df['ds_book']):
			if date_1 < date < date_2:
				w_date = listing_review_rating * .8
				return w_date
			else:
				return listing_review_rating

	def pro_pic_rank():

		for i in len(df['listing_has_pro_pictures'])
			if 'listing_has_pro_pictures' == 1:
				return listing_review_rating * 1.2
			else:
				return listing_review_rating

	def w_books_rank():

		df['num_book_quantile'] = cont_to_ord(df['listing_num_books_90day'])
		book_rank = df['num_book_quantile']
		w_books = []

		for i in len(book_rank):
			if book_rank == 'MIN':
				new_rank = listing_review_rating * .25
				w_books.append(new_rank)

			elif book_rank == '25%':
				new_rank = listing_review_rating * .5
				w_books.append(new_rank)

			elif book_rank == 'AVG':
				new_rank = listing_review * .75
				w_books.append(new_rank)

			elif book_rank == '75%':
				new_rank = listing_review_rating * 1
				w_books.append(new_rank)

			else:
				new_rank = listing_review_rating * 1.25
				w_books.append(new_rank)






	

