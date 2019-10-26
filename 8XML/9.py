minLat, minLon, maxLat, maxLon = map(float, (input().split()))
n = int(input())
stepLat = (maxLat-minLat)/n
stepLon = (maxLon - minLon)/n
for i in range(n):
    for j in range(n):
        print(minLat+(i*stepLat), minLon+(j*stepLon),
              minLat+((i+1)*stepLat), minLon+((j+1)*stepLon))


#https://www.openstreetmap.org/api/0.6/map?bbox=48.9177%2C55.7982%2C49.2665%2C55.8165