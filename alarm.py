def program_alarm(i, j, nums):
    index = 0
    nums[1] = i
    nums[2] = j
    while nums[index] != 99:
        num = nums[index]
        val1 = nums[index + 1]
        val2 = nums[index + 2]
        index3 = nums[index + 3]
        if num == 1:
            nums[index3] = nums[val1] + nums[val2]
        elif num == 2:
            nums[index3] = nums[val1] * nums[val2]
        index += 4
    return nums[0]

with open('day_02\input2.txt', 'r') as file:
    nums = [int(num) for num in file.read().split(",")]
    #print(program_alarm(12,2, nums))

    valor = 19690720
    for noun in range(100):
        for verb in range(100):
            resultado = program_alarm(noun, verb, nums[:])
            if (resultado == valor):
                print(100 * noun + verb)
                break

            