# get the input and parse
input_candles = input('enter candles and heights of candles: ')

# code to parse

cadles_str = input_candles.split() # this is to parse the input with space delimeter
candles = [int(candl) for candl in cadles_str]

# candles = [2,3,5,2,1,4,5,3,2,2,3,5]

max_candle = max(candles)
print(candles, 'max num=', max_candle)
start = 0
count = 0
# length = len(candles)

# # option 1
# while start < length:
#     if max_candle == candles[start]:
#         count += 1
#     start += 1

#option 2
for candle in candles:
    if candle == max_candle:
        count += 1



print("There are " +str(count)+" "+str(max_candle)+"'s in list")