def mars_explore(text):
    result = 0;
    for i in range(0, len(text), 3):
        if text[i:i + 3] != 'SOS':
            for j in range(3):
                if text[i + j] != 'SOS'[j]:
                    result += 1
    return result


print(mars_explore('SOSSPSSQSSOR'))
print(mars_explore('SOSSOT'))
print(mars_explore('SOSSET'))
