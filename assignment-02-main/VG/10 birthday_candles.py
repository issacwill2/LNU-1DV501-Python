remained_candle = 0
all_boxes = 0
buy = 0
candles_in_box = 24

for age in range(1, 101):
    while True:
        if remained_candle < age:
            buy += 1
            remained_candle += candles_in_box
        else:
            break
    all_boxes += buy

    remained_candle -= age

    if buy != 0:
        print(f'Before birthday {age}, buy {buy} box(es)')
    buy = 0

print(f'\nTotal number of boxes: {all_boxes}, Remaining candles: {remained_candle}')
