class Timer(object):
	def __init__(self,
		_t_max = 1,
		_t_step = 1):
		
		self.t_max = _t_max
		self.t_step = _t_step
	
		self.t_cur = 0
		
	
	def update(self):
	
		self.t_cur += self.t_step
		
		if self.t_cur >= self.t_max:
			self.reset()
			return True
		
		else:
			return False
		
	
	def reset(self):
		self.t_cur = 0