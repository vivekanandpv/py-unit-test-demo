def tell_time(minutes):
    if minutes == 15:
        return 'quarter-past'
    elif minutes == 30:
        return 'half-past'
    elif minutes == 45:
        return 'quarter to'
    elif minutes >= 0 and minutes <= 60:
        return ''
    else:
        raise ValueError
