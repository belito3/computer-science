class MultiStackFixed:
    def __init__(self, stack_capacity, num_of_stack):
        self.num_of_stack = num_of_stack
        self.stack_capacity = stack_capacity
        self.sizes = [0] * self.num_of_stack
        self.values = [0] * self.num_of_stack * self.stack_capacity

    def push(self, stack_num, value) -> None:
        if self.is_full(stack_num):
            raise StackFullError("Push failed. Stack {} is full".format(stack_num))
        index = self.get_index_of_top_stack(stack_num)
        self.values[index+1] = value
        self.sizes[stack_num] += 1

    def pop(self, stack_num) -> int:
        if self.is_empty(stack_num):
            raise StackEmptyError("Pop failed. Stack {} is empty".format(stack_num))
        index = self.get_index_of_top_stack(stack_num)
        value = self.values[index]
        self.values[index] = 0
        self.sizes[stack_num] -=1
        return value

    def peek(self, stack_num) -> int:
        if self.is_empty(stack_num):
            raise StackEmptyError("Peek failed. Stack {} is empty".format(stack_num))
        index = self.get_index_of_top_stack(stack_num)
        return self.values[index]
    
    def is_full(self, stack_num) -> bool:
        return self.sizes[stack_num] == stack_capacity

    def is_empty(self, stack_num) -> bool:
        return self.sizes[stack_num] == 0

    def get_index_of_top_stack(self, stack_num) -> int:
        index = self.stack_capacity * stack_num + self.sizes[stack_num] - 1
        return index

    def _assert_valid_stack_num(self, stack_num):
        if stack_num >= self.num_of_stack:
            raise StackNumInvalidError("Stack number must less than {}".format(self.num_of_stack))


class MultiStackError(Exception):
    """MultiStack error operation"""

class StackFullError(MultiStackError):
    """Stackfull error operation"""

class StackEmptyError(MultiStackError):
    """Stackempty error operation"""

class StackNumInvalidError(MultiStackError):
    """StackNum invalid error operation"""


if __name__ == "__main__":
    num_of_stack = 3
    stack_capacity = 5

    mstack = MultiStackFixed(stack_capacity=stack_capacity, num_of_stack=num_of_stack)

    # Test push
    for i in range(num_of_stack):
        for j in range(stack_capacity):
            mstack.push(stack_num=i, value=j)

    # Test pop 
    for i in range(num_of_stack):
        for j in range(stack_capacity):
            value = mstack.pop(stack_num=i)
            print(f"pop stack={i} value={value}")

    mstack.push(stack_num=1, value=10)
    print("peek: ", mstack.peek(stack_num=1))
    mstack.pop(stack_num=1)
    mstack.pop(stack_num=1)
