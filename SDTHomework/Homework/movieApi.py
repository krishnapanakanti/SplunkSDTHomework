import requests

class movieApi:
	def __init__(self):
		self.mapi = 'https://splunk.mocklab.io/movies'
		self.get_headers = {'Accept':'application/json'}
		self.post_headers = {'Content-Type':'application/json'}
		
	def movieGet(self, q, count = 0):
		get_params = {'q':q, 'count':count}
		res = requests.get(self.mapi, headers = self.get_headers, params = get_params)
		try: 
			return res.json()['results']
		except:
			return {'status_code':res.status_code, 'results':[]}


	def moviePost(self,**kwargs):
		post_params = {'name':name,
						'poster_path':poster_path,
						'title':title, 
						'overview':overview, 
						'release_date':release_date, 
						'popularity':popularity, 
						'original_title':original_title, 
						'backdrop_path':backdrop_path, 
						'vote_count':vote_count, 
						'video':video, 
						'adult':adult, 
						'vote_average':vote_average, 
						'original_language':original_language, 
						'id':id, 
						'genre_ids':genre_ids}
		res = requests.post(self.mapi, headers = self.post_headers, params = post_params)


if __name__ == "__main__":
	pass


	