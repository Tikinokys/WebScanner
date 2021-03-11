import os

def dirs(path):
	files = []
	_ = os.listdir(path)
	for file in _:
		if not file.endswith('.py') or file == '__init__.py':pass
		else:files.append(file)
	return files