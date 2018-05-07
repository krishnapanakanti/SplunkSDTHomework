from movieApi import movieApi

class SPL001:
	def __init__():
		self.mapi_object = movieApi()

	def get_init():
		resp = self.mapi_object.movieGet('batman')
		keys = {'id','poster_path'}
		req_res = [{key:i[key] for key in keys} for i in resp]


	def post_init():
		self.post = self.mapi_object.moviePost('batman')

	def test_
