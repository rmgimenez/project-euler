# teste
import funcoes

class Collatz:
  def __init__(self):
    self.memory = {}

  def count(self, n):
    if n in self.memory:
      return self.memory[n]
    if n == 1:
      return 1
    if (n % 2) == 0:
      new_count = self.count(n / 2) + 1
      self.memory[n] = new_count
      return new_count
    else:
      new_count = self.count((3 * n) + 1) + 1
      self.memory[n] = new_count
      return new_count

maximum = -1
maximum_count = -1
collatz = Collatz()
for i in range(1, 1000000):
  count = collatz.count(i)
  if count > maximum_count:
    maximum = i
    maximum_count = count

print('Number:{}, Count:{}'.format(maximum, maximum_count))