def timeConversion(s):
    ampm = ''.join(list(s)[-2:])
    hours, mins, secs = s.replace(ampm,'').split(':')
    if int(hours) <12 and int(mins) <=59 and int(secs) <=59:
        if ampm == 'PM':
            hours = int(hours) + 12
        elif ampm == 'AM' and int(hours)==12:
            hours = 0

    return '{0}:{1}:{2}'.format(str(hours).zfill(2),str(mins).zfill(2),str(secs).zfill(2))

print(timeConversion('12:45:54PM'))
print(timeConversion('01:45:54AM'))
print(timeConversion('00:45:54AM'))