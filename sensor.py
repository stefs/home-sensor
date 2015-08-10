import logging
import datetime
import collections
import random
import config

class Sensor:
	def __init__(self, name, file, floor, ceiling):
		self.name = name
		self.file = file
		self.floor = floor
		self.ceiling = ceiling
		self.history = collections.deque()
		self.current = None
		self.minimum = None
		self.maximum = None
		self.problem = None

	def __str__(self):
		return ' | '.join([
			self.name,
			'{:.1f} °C'.format(self.current) if self.current else 'Fehler',
			format_measurement(self.minimum),
			format_measurement(self.maximum),
			'{:.1f} °C – {:.1f} °C'.format(self.floor, self.ceiling),
			'Warnung' if self.problem else 'Ok'])

	def update(self, now):
		try:
			# TODO parse self.file
			self.current = random.randrange(200, 400) / 10
		except Exception:
			self.current = None
		else:
			self.history.append((self.current, now))
		while self.history[0][1] < now - config.history_seconds:
			self.history.popleft()
		self.minimum = min(self.history)
		self.maximum = max(self.history)
		if self.minimum[0] < self.floor:
			self.problem = self.minimum
		elif self.maximum[0] > self.ceiling:
			self.problem = self.maximum
		else:
			self.problem = None

def format_measurement(m):
	return '{:.1f} °C / {:%X}'.format(
		m[0],
		datetime.datetime.fromtimestamp(m[1]))

