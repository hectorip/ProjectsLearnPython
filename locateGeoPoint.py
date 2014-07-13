

samplePartition = {
	'one' : [1,2,4],
	'two' : [1,2,4],
}

def locatePoint(point, partition):
	for part in partition:
		return isPointInPolygon(part)
