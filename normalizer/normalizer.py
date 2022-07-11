from pytz import timezone
from datetime import datetime

class normalizer():
    def normalize_timestamp(self, timestamp: str) -> str:
        timestamp_spilt = timestamp.split()

        date = timestamp_spilt[0]
        date_split = date.split('/')
        month = int(date_split[0])
        day = int(date_split[1])
        year = int(date_split[2]) + 2000
        
        time = timestamp_spilt[1]
        time_split = time.split(':')
        hour = int(time_split[0])
        minute = int(time_split[1])
        second = int(time_split[2])
        milisecond = 0

        if timestamp_spilt[2] == 'PM' and hour < 12:
            hour += 12

        dt = datetime(year, month, day, hour, minute, second, milisecond, tzinfo=timezone('US/Pacific'))

        return dt.astimezone(timezone('US/Eastern')).isoformat('T')

    def normalize_zipcode(self, zipcode: str) -> str:
        padding = '0' * (5 - len(zipcode))
        return padding + zipcode

    def normalize_fullname(self, name: str) -> str:
        return name.upper()

    def normalize_duration(self, duration: str) -> str:
        split_dur = duration.split(':')
        hours_in_seconds = float(split_dur[0])*3600
        minutes_in_seconds = float(split_dur[1])*60

        split_seconds = split_dur[2].split('.')
        seconds = float(split_seconds[0])
        milliseconds = float(split_seconds[1])/1000

        total_time = hours_in_seconds + minutes_in_seconds + seconds + milliseconds
        return f'{total_time:.3f}'

    def normalize_totalDuration(self, *durations: str) -> str:
        total_time = 0
        for duration in durations:
            if ':' in duration:
                duration = self.normalize_duration(duration)
            total_time += float(duration)
        return f'{total_time:.3f}'