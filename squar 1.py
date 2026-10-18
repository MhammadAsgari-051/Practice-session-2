length = 1.0
width = 1.0

for i in range(1, 21):
    side = 0.5 ** i
    length += side
    print(f"Step {i}: Length = {length:.4f}, Width = {width:.4f}")