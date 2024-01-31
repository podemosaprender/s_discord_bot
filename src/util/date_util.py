import datetime

def dateFromMidnight(since: datetime.datetime):
    return since.replace(hour=0, minute=0, second=1, microsecond=0)

def dateToMidnight(until: datetime.datetime):
    return until.replace(hour=23, minute=59, second=59, microsecond=0)

def datetime_without_tz(dt):  #U: e.g postgres require SIN tzinfo
	return dt.replace(tzinfo=None)

def datetime_with_tz(dt):  #U: add tzinfo
	logm("datetime_with_tz",l=9, dt=dt, tzinfo=dt.tzinfo)
	if ( 
		dt.tzinfo == None 
		or dt.tzinfo.utcoffset(dt) == None
	):
		return dt.replace(tzinfo=datetime.timezone.utc)
	else:
		return dt



