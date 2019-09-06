import datetime


def calculate_gmst(dt):
    j2000date = datetime.datetime(2000, 1, 1, 12, 0, 0)
    day_diff = (dt - j2000date).days
    c_time = dt.time()
    t = (day_diff + (c_time.hour * 3600 + c_time.minute * 60 + c_time.second)
         / (24 * 3600)) / 36525
    ams_in_seconds = int(
        18 * 3600 + 41 * 60 + 50.54841 + 8640184.812866 * t +
        0.093104 * t * t - 6.2 * 10 ** (-6) * t ** 3)

    gmst = dt - datetime.timedelta(hours=12) + datetime.timedelta(seconds=ams_in_seconds)
    return gmst


def calculate_star_time_in_seconds(current_datetime, timezone, longitude):
    ut = current_datetime - datetime.timedelta(hours=timezone)
    gmst = calculate_gmst(ut)
    longitude_time = 12 * longitude / 180
    result = gmst + datetime.timedelta(hours=longitude_time)
    return result.hour * 3600 + result.minute * 60 + result.second


def time_in_seconds_to_degrees(seconds):
    return seconds * 360 / (24 * 3600)
