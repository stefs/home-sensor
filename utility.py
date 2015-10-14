import datetime
import gc
import locale
import logging
import resource
import time


def init():
	locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
	logging.basicConfig(
		format = '[%(asctime)s:%(levelname)s:%(module)s] %(message)s',
		datefmt = '%y-%m-%d-%H-%M-%S',
		level = logging.DEBUG)


def memory_check():
	gc.collect()
	memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e3
	logging.debug('using {:.0f} megabytes of memory'.format(memory))
	if memory > 100:
		raise Exception('memory leak')


def allow_every_x_seconds(interval):
	def decorating_function(user_function):
		target = int()
		def new_function(*args, **kwargs):
			nonlocal target
			now = time.perf_counter()
			if now >= target:
				target = now + interval
				user_function(*args, **kwargs)
		return new_function
	return decorating_function
