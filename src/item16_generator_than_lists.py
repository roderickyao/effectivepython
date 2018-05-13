def index_words(text):
  result = []
  if text:
    result.append(0)
  for index, letter in enumerate(text):
    if letter == ' ':
      result.append(index + 1)

  return result


def index_words_iter(text):
  if text:
    yield 0
  for index, letter in enumerate(text):
    if letter == ' ':
      yield index + 1


address = 'Four score and seven year ago....'
result = index_words(address)
result2 = list(index_words_iter(address))
print(result2)
