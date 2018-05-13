import os


def normalize(numbers):
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result


def read_visits(data_path):
  with open(data_path) as f:
    for line in f:
      yield int(line)


def normalize_copy(numbers):
  numbers = list(numbers)
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result


def normalize_func(get_iter):
  total = sum(get_iter())
  result = []
  for value in get_iter():
    percent = 100 * value / total
    result.append(percent)
  return result


class ReadVisits(object):
  def __init__(self, data_path):
    self.data_path = data_path

  def __iter__(self):
    with open(self.data_path) as f:
      for line in f:
        yield int(line)


def normalize_defensive(numbers):
  if iter(numbers) is iter(numbers):
    raise TypeError('Must supply a container.')
  total = sum(numbers)
  result = []
  for value in numbers:
    percent = 100 * value / total
    result.append(percent)
  return result


def main():
  visits = [15, 35, 80]
  percentages = normalize(visits)
  print(percentages)

  with open('test_visits.txt', 'w+') as f:
    for number in visits:
      f.write("{0}\r\n".format(number))

  it = read_visits('test_visits.txt')
  # print(list(it))
  percentages = normalize_copy(it)
  print(percentages)

  percentages = normalize_func(lambda: read_visits('test_visits.txt'))
  print(percentages)

  visits = ReadVisits('test_visits.txt')
  percentages = normalize(visits)
  print(percentages)

  try:
    os.remove('test_visits.txt')
  except OSError:
    pass


main()
